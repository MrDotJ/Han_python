import gurobipy as gurobi
import numpy as np

M = 1e7
INFINITY = gurobi.GRB.INFINITY
INF = INFINITY

class MyExpr:
    def __init__(self, quad_expr: gurobi.QuadExpr):
        self.expr = quad_expr
        self.line_part = None
        self.line_size = 0
        self.line_vars = []
        self.line_coeff = []
        self.quad_size = 0
        self.quad_vars_1 = []
        self.quad_vars_2 = []
        self.quad_coeff = []
        # line part
        self.line_part: gurobi.LinExpr = self.expr.getLinExpr()
        self.line_size = self.line_part.size()
        self.line_vars = []
        self.line_coeff = []
        for i in range(self.line_size):
            self.line_vars.append(self.line_part.getVar(i))
            self.line_coeff.append(self.line_part.getCoeff(i))
        # second part
        self.quad_size = self.expr.size()
        self.quad_vars_1 = []
        self.quad_vars_2 = []
        self.quad_coeff = []
        for i in range(self.quad_size):
            self.quad_vars_1.append(self.expr.getVar1(i))
            self.quad_vars_2.append(self.expr.getVar2(i))
            self.quad_coeff.append(self.expr.getCoeff(i))
        # get var in line part

    def getCoeff(self, var):
        # get the line part
        coeff_line = []
        for i in range(self.line_size):
            if self.line_vars[i].sameAs(var):
                coeff_line.append(self.line_coeff[i])
        coeff_quad = []
        for i in range(self.quad_size):
            if self.quad_vars_1[i].sameAs(var) and self.quad_vars_2[i].sameAs(var):  # x1 x1
                coeff_quad.append(2 * var * self.quad_coeff[i])
            if self.quad_vars_1[i].sameAs(var) and not self.quad_vars_2[i].sameAs(var):  # x1 x2
                coeff_quad.append(self.quad_vars_2[i] * self.quad_coeff[i])
            if not self.quad_vars_1[i].sameAs(var) and self.quad_vars_2[i].sameAs(var):  # x2 x1
                coeff_quad.append(self.quad_vars_1[i] * self.quad_coeff[i])
        return gurobi.quicksum(coeff_line) + gurobi.quicksum(coeff_quad)

    def addConstr(self, expr, model, name):
        model.addConstr(expr == 0, name=name)


def Complementary_great(expr, model, dual_expression, dual_obj, dual_var_name):  # expr should be greater than zero
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(name=dual_var_name)
    var_bin = model.addVar(vtype=gurobi.GRB.BINARY, name=dual_var_name + "_binary")
    model.addConstr(expr >= 0, name='original_feasible_' + dual_var_name)
    model.addConstr(expr <= M * var_bin, name='original_feasible_M_' + dual_var_name)
    model.addConstr(var_dual >= 0, name='dual_feasible_' + dual_var_name)
    model.addConstr(var_dual <= M * (1 - var_bin), name='dual_feasible_M_' + dual_var_name)
    dual_expression.append(-1 * expr * var_dual)
    if type(expr) == gurobi.Var:
        dual_obj.append(0)
    else:
        dual_obj.append(-1 * expr.getConstant() * var_dual)
    return var_dual
def Complementary_equal(expr, model, dual_expression, dual_obj, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(lb=-1 * INFINITY, ub=INFINITY, name='dual_' + dual_var_name)
    model.addConstr(-1 * expr == 0, name=dual_var_name + '[EqualFeasible]')
    dual_expression.append(-1 * expr * var_dual)
    if type(expr) == gurobi.Var:
        dual_obj.append(0)
    else:
        dual_obj.append(-1 * expr.getConstant() * var_dual)
    return var_dual
def Complementary_soc(left_coeff, left_var, right_coeff, right_var, model, dual_expression, dual_obj, dual_var_name,
                       original_var_min, original_var_max, dual_var_min, dual_var_max):
    left_var_length = len(left_coeff)
    right_var_length = len(right_coeff)
    # 左侧对偶变量
    dual_left = model.addVars(left_var_length, lb=-1*INFINITY, ub=INFINITY,
                              name=dual_var_name + '_dual_left')
    # 右侧对偶变量
    dual_right = model.addVars(right_var_length, lb=0, ub=INFINITY,
                               name=dual_var_name + '_dual_right')
    # 添加原锥约束
    expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * left_var[i]
                                 for i in range(left_var_length)])
    expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * right_var[i]
                                  for i in range(right_var_length)])
    model.addConstr(lhs=expr_left, sense=gurobi.GRB.LESS_EQUAL, rhs=expr_right, name=dual_var_name + '[Original]')
    # 添加对偶锥约束
    dual_expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * dual_left[i] * dual_left[i]
                                      for i in range(left_var_length)])
    dual_expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * dual_right[i] * dual_right[i]
                                       for i in range(right_var_length)])
    model.addConstr(lhs=dual_expr_left, sense=gurobi.GRB.LESS_EQUAL, rhs=dual_expr_right, name=dual_var_name + '[Dual]')
    # 添加互补约束
    lagrange_sum = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * dual_left[i]
                                    for i in range(left_var_length)]) + \
                   gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * dual_right[i]
                                    for i in range(right_var_length)])
    # model.addConstr(lagrange_sum == 0, name=dual_var_name + '[Lagrange]')

    # # =============== deal with lagrange sum equal zero ==============
    # xi is dual variables, xj is original variables
    # xj_min , xj_max, N
    # xj_min = 0
    # xj_max = 10
    # xi_min = 0
    # xi_max = 10
    # N = 20
    # xjn_min = np.arange(N) / N * (xj_max - xj_min) + xj_min
    # xjn_max = (np.arange(N) + 1) / N * (xj_max - xj_min) + xj_min
    #
    # binary = model.addVars(N, vtype=gurobi.GRB.BINARY)
    # wij = model.addVar(lb=-1*INF, ub=INF)
    # model.addConstr(xi >= xi_min)
    # model.addConstr(xi <= xi_max)
    #
    # for n in range(N):
    #     model.addConstr((binary[n] == 1) >> (wij >= (xi * xjn_min[n] + xj * xi_min - xi_min * xjn_min[n])))
    #     model.addConstr((binary[n] == 1) >> (wij >= (xi * xjn_max[n] + xj * xi_max - xi_max * xjn_max[n])))
    #     model.addConstr((binary[n] == 1) >> (wij <= (xi * xjn_min[n] + xj * xi_max - xi_max * xjn_min[n])))
    #     model.addConstr((binary[n] == 1) >> (wij <= (xi * xjn_max[n] + xj * xi_min - xi_min * xjn_max[n])))
    #     model.addConstr((binary[n] == 1) >> (xjn_min[n] <= xj))
    #     model.addConstr((binary[n] == 1) >> (xj <= xjn_max[n]))
    # model.addConstr(gurobi.quicksum(binary) == 1)

    original_var = left_var + right_var
    dual_var = tonp(dual_left).tolist() + tonp(dual_right).tolist()
    coeff = left_coeff + right_coeff
    w = model.addVars(left_var_length + right_var_length, lb=-1*INF, ub=INF)
    N = 20
    measurement = []
    for i in range(left_var_length + right_var_length):
        wij = w[i]
        binary = model.addVars(N, vtype=gurobi.GRB.BINARY)
        xi = dual_var[i]
        xj = original_var[i]
        measurement.append(wij - xi * xj)
        xi_min = dual_var_min[i]
        xi_max = dual_var_max[i]
        xj_min = original_var_min[i]
        xj_max = original_var_max[i]
        N = 20
        xjn_min = np.arange(N) / N * (xj_max - xj_min) + xj_min
        xjn_max = (np.arange(N) + 1) / N * (xj_max - xj_min) + xj_min
        model.addConstr(xi >= xi_min)
        model.addConstr(xi <= xi_max)
        for n in range(N):
            model.addConstr((binary[n] == 1) >> (wij >= (xi * xjn_min[n] + xj * xi_min - xi_min * xjn_min[n])))
            model.addConstr((binary[n] == 1) >> (wij >= (xi * xjn_max[n] + xj * xi_max - xi_max * xjn_max[n])))
            model.addConstr((binary[n] == 1) >> (wij <= (xi * xjn_min[n] + xj * xi_max - xi_max * xjn_min[n])))
            model.addConstr((binary[n] == 1) >> (wij <= (xi * xjn_max[n] + xj * xi_min - xi_min * xjn_max[n])))
            model.addConstr((binary[n] == 1) >> (xj >= xjn_min[n]))
            model.addConstr((binary[n] == 1) >> (xj <= xjn_max[n]))
        model.addConstr(gurobi.quicksum(binary) == 1)
    model.addConstr(sum([coeff[i]**2 * w[i] for i in range(left_var_length + right_var_length)]) == 0,
                    name=dual_var_name + '[Lagrange]')
    # # =============== END

    dual_expression.append(-1 * lagrange_sum)
    dual_obj.append(0)
    return dual_left, dual_right, measurement
def Complementary_equal_plus(expr, model, dual_expression, dual_obj, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(lb=-1 * INFINITY, ub=INFINITY, name='dual_' + dual_var_name)
    constr = model.addConstr(-1 * expr == 0, name=dual_var_name + '[EqualFeasible]')
    dual_expression.append(-1 * expr * var_dual)
    if type(expr) == gurobi.Var:
        dual_obj.append(0)
    else:
        dual_obj.append(-1 * expr.getConstant() * var_dual)
    return var_dual, constr, -1 * expr.getConstant() * var_dual
def Complementary_soc_plus(left_coeff, left_var, right_coeff, right_var, model, dual_expression, dual_obj, dual_var_name,
                           original_var_min, original_var_max, dual_var_min, dual_var_max):
    left_var_length = len(left_coeff)
    right_var_length = len(right_coeff)
    # 左侧对偶变量
    dual_left = model.addVars(left_var_length, lb=-1*INFINITY, ub=INFINITY,
                              name=dual_var_name + '_dual_left')
    # 右侧对偶变量
    dual_right = model.addVars(right_var_length, lb=0, ub=INFINITY,
                               name=dual_var_name + '_dual_right')
    # 添加原锥约束
    expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * left_var[i]
                                 for i in range(left_var_length)])
    expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * right_var[i]
                                  for i in range(right_var_length)])
    constr_original = model.addConstr(expr_left <= expr_right, name=dual_var_name + '[Original]')
    # 添加对偶锥约束
    dual_expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * dual_left[i] * dual_left[i]
                                      for i in range(left_var_length)])
    dual_expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * dual_right[i] * dual_right[i]
                                       for i in range(right_var_length)])
    constr_dual = model.addConstr(dual_expr_left <= dual_expr_right, name=dual_var_name + '[Dual]')
    # 添加互补约束
    lagrange_sum = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * dual_left[i]
                                    for i in range(left_var_length)]) + \
                   gurobi.quicksum([right_coeff[i] * right_coeff[i] *  right_var[i] * dual_right[i]
                                    for i in range(right_var_length)])
    # complementary_constr = model.addConstr(lagrange_sum == 0, name=dual_var_name + '[Lagrange]')

    # # =============== deal with lagrange sum equal zero ==============
    # xi is dual variables, xj is original variables
    var_linear = []
    constrain_linear = []
    original_var = left_var + right_var
    dual_var = tonp(dual_left).tolist() + tonp(dual_right).tolist()
    coeff = left_coeff + right_coeff
    w = model.addVars(left_var_length + right_var_length, lb=-1*INF, ub=INF)
    var_linear.append(w)
    N = 20
    measurement = []
    for i in range(left_var_length + right_var_length):
        wij = w[i]
        binary = model.addVars(N, vtype=gurobi.GRB.BINARY)
        var_linear.append(binary)
        xi = dual_var[i]
        xj = original_var[i]
        measurement.append(wij - xi * xj)
        xi_min = dual_var_min[i]
        xi_max = dual_var_max[i]
        xj_min = original_var_min[i]
        xj_max = original_var_max[i]
        N = 20
        xjn_min = np.arange(N) / N * (xj_max - xj_min) + xj_min
        xjn_max = (np.arange(N) + 1) / N * (xj_max - xj_min) + xj_min
        constrain_linear.append(model.addConstr(xi >= xi_min))
        constrain_linear.append(model.addConstr(xi <= xi_max))
        for n in range(N):
            constrain_linear.append(
                model.addConstr((binary[n] == 1) >> (wij >= (xi * xjn_min[n] + xj * xi_min - xi_min * xjn_min[n]))))
            constrain_linear.append(
                model.addConstr((binary[n] == 1) >> (wij >= (xi * xjn_max[n] + xj * xi_max - xi_max * xjn_max[n]))))
            constrain_linear.append(
                model.addConstr((binary[n] == 1) >> (wij <= (xi * xjn_min[n] + xj * xi_max - xi_max * xjn_min[n]))))
            constrain_linear.append(
                model.addConstr((binary[n] == 1) >> (wij <= (xi * xjn_max[n] + xj * xi_min - xi_min * xjn_max[n]))))
            constrain_linear.append(
                model.addConstr((binary[n] == 1) >> (xj >= xjn_min[n])))
            constrain_linear.append(
                model.addConstr((binary[n] == 1) >> (xj <= xjn_max[n])))
        constrain_linear.append(model.addConstr(gurobi.quicksum(binary) == 1))
    constrain_linear.append(
        model.addConstr(sum([coeff[i]**2 * w[i] for i in range(left_var_length + right_var_length)]) == 0,
                        name=dual_var_name + '[Lagrange]'))
    # # =============== END

    dual_expression.append(-1 * lagrange_sum)
    dual_obj.append(0)
    return dual_left, dual_right, constr_original, constr_dual, var_linear, constrain_linear, measurement


# this is just original constraints for test START
def Complementary_great1(expr, model, dual_var_name):  # expr should be greater than zero
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    model.addConstr(expr >= 0, name='original_feasible_' + dual_var_name)
    return 0, 0
def Complementary_equal2(expr, model, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    model.addConstr(-1 * expr == 0, name=dual_var_name + '[EqualFeasible]')
    return 0, 0
def Complementary_equal_plus2(expr, model, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    constr = model.addConstr(-1 * expr == 0, name=dual_var_name + '[EqualFeasible]')
    return 0, constr, 0
def Complementary_soc2(left_coeff, left_var, right_coeff, right_var, model, dual_var_name):
    left_var_length = len(left_coeff)
    right_var_length = len(right_coeff)
    # 左侧对偶变量
    dual_left = model.addVars(left_var_length, lb=-1*INFINITY, ub=INFINITY,
                              name=dual_var_name + '_dual_left')
    # 右侧对偶变量
    dual_right = model.addVars(right_var_length, lb=0, ub=INFINITY,
                               name=dual_var_name + '_dual_right')
    # 添加原锥约束
    expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * left_var[i]
                                 for i in range(left_var_length)])
    expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * right_var[i]
                                  for i in range(right_var_length)])
    model.addConstr(lhs=expr_left, sense=gurobi.GRB.LESS_EQUAL, rhs=expr_right, name=dual_var_name + '[Original]')


    return dual_left, dual_right, 0
def Complementary_soc_plus2(left_coeff, left_var, right_coeff, right_var, model, dual_var_name):
    left_var_length = len(left_coeff)
    right_var_length = len(right_coeff)
    # 左侧对偶变量
    dual_left = model.addVars(left_var_length, lb=-1*INFINITY, ub=INFINITY,
                              name=dual_var_name + '_dual_left')
    # 右侧对偶变量
    dual_right = model.addVars(right_var_length, lb=0, ub=INFINITY,
                               name=dual_var_name + '_dual_right')
    # 添加原锥约束
    expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * left_var[i]
                                 for i in range(left_var_length)])
    expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * right_var[i]
                                  for i in range(right_var_length)])
    constr_original = model.addConstr(expr_left <= expr_right, name=dual_var_name + '[Original]')


    return dual_left, dual_right, constr_original, 0, 0, 0
# this is just for test END


def tonp(vars_gur) -> np.array:
    keys = vars_gur.keys()
    key_last = keys[-1]
    if type(key_last) != int:
        dim = len(key_last)
        shape = list(map(lambda x: x + 1, list(key_last)))
    else:
        dim = 1
        shape = key_last + 1
    if dim == 1:
        re = np.empty(tuple([shape, ]), dtype=object)
        for i in range(shape):
            re[i] = vars_gur[i]
        return re
    if dim == 2:
        re = np.empty(tuple(shape), dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                re[i, j] = vars_gur[i, j]
        return re
    if dim == 3:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    re[i, j, k] = vars_gur[i, j, k]
        return re
    if dim == 4:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        re[i, j, k, m] = vars_gur[i, j, k, m]
        return re
    if dim == 5:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        for n in range(shape[4]):
                            re[i, j, k, m, n] = vars_gur[i, j, k, m, n]
        return re


def to_value(vars_gur):
    if vars_gur == None:
        return []
    keys = vars_gur.keys()
    key_last = keys[-1]
    if type(key_last) != int:
        dim = len(key_last)
        shape = list(map(lambda x: x + 1, list(key_last)))
    else:
        dim = 1
        shape = key_last + 1
    if dim == 1:
        re = np.empty(tuple([shape, ]), dtype=object)
        for i in range(shape):
            re[i] = vars_gur[i].getAttr('X')
        return re
    if dim == 2:
        re = np.empty(tuple(shape), dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                re[i, j] = vars_gur[i, j].getAttr('X')
        return re
    if dim == 3:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    re[i, j, k] = vars_gur[i, j, k].getAttr('X')
        return re
    if dim == 4:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        re[i, j, k, m] = vars_gur[i, j, k, m].getAttr('X')
        return re
    if dim == 5:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        for n in range(shape[4]):
                            re[i, j, k, m, n] = vars_gur[i, j, k, m, n].getAttr('X')
        return re


def to_value_np(vars_np):
    re = np.ones(vars_np.shape)
    shape = vars_np.shape
    dim = vars_np.ndim
    if dim == 1:
        for i in range(shape[0]):
            re[i] = vars_np[i].getAttr('X')
        return re
    if dim == 2:
        for i in range(shape[0]):
            for j in range(shape[1]):
                re[i, j] = vars_np[i, j].getAttr('X')
        return re
    if dim == 3:
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    re[i, j, k] = vars_np[i, j, k].getAttr('X')
        return re
    if dim == 4:
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        re[i, j, k, m] = vars_np[i, j, k, m].getAttr('X')
        return re
    if dim == 5:
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        for n in range(shape[4]):
                            re[i, j, k, m, n] = vars_np[i, j, k, m, n].getAttr('X')
        return re