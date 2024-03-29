import gurobipy as gurobi
import numpy as np

M = 1e6
N = 3

# INFINITY = gurobi.GRB.INFINITY
INF = 300

class MyExpr:
    def __init__(self, quad_expr: gurobi.QuadExpr):
        self.expr = quad_expr
        self.line_part = None
        self.line_size = 0
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
    # model.addConstr(var_dual * expr == 0)
    dual_expression.append(-1 * expr * var_dual)
    if type(expr) == gurobi.Var:
        dual_obj.append(0)
    else:
        dual_obj.append(-1 * expr.getConstant() * var_dual)
    return var_dual

def Complementary_equal(expr, model, dual_expression, dual_obj, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(lb=-1 * INF, ub=INF, name='dual_' + dual_var_name)
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
    dual_left = model.addVars(left_var_length, lb=-1*INF, ub=INF,
                              name=dual_var_name + '_left')
    # 右侧对偶变量
    dual_right = model.addVars(right_var_length, lb=0, ub=0,
                               name=dual_var_name + '_right')
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
    # model.addConstr(lhs=dual_expr_left, sense=gurobi.GRB.LESS_EQUAL, rhs=dual_expr_right, name=dual_var_name + '[Dual]')
    # 添加互补约束
    lagrange_sum = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * dual_left[i]
                                    for i in range(left_var_length)]) + \
                   gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * dual_right[i]
                                    for i in range(right_var_length)])
    # model.addConstr(lagrange_sum == 0, name=dual_var_name + '[Lagrange]')
    aux = model.addVars(3, lb=-1*INF, ub=INF, name='aux_KK_' + dual_var_name)
    var_original = [left_var[0], left_var[1], right_var[0]]
    var_dual = [dual_left[0], dual_left[1], dual_right[0]]
    coeff = [left_coeff[0], left_coeff[1], right_coeff[0]]

    # for i in range(3):
        # biGen(var_original[i], var_dual[i], aux[i], original_var_min[i], original_var_max[i], dual_var_min[i], dual_var_max[i], 5, 5, model)
        # model.addConstr(aux[i] == var_dual[i] * var_original[i])
    dddd = model.addVar()
    # model.addConstr(sum([coeff[i]**2 * aux[i] for i in range(3)]) <= dddd)
    dual_expression.append(-1 * lagrange_sum)
    dual_obj.append(0)

    cross = [var_original[i] * var_dual[i] for i in range(3)]
    auxx = [aux[0], aux[1], aux[2]]
    return cross, auxx, [var_dual, dddd]

def biGen(x, y, z, x_min, x_max, y_min, y_max, n, m, model):
    xi = np.linspace(x_min, x_max, n)
    yi = np.linspace(y_min, y_max, m)
    zi = xi.reshape((-1, 1)).dot(yi.reshape((1, -1)))

    aij = model.addVars(n, m, ub=1, name='aux_xy')
    model.addConstr(x == sum(sum(np.array([[aij[i, j] * xi[i] for j in range(m)] for i in range(n)]))))
    model.addConstr(y == sum(sum(np.array([[aij[i, j] * yi[j] for j in range(m)] for i in range(n)]))))
    model.addConstr(z == sum(sum(np.array([[aij[i, j] * zi[i][j] for j in range(m)] for i in range(n)]))))
    model.addConstr(gurobi.quicksum(aij) == 1)

    hiju = model.addVars(n, m, vtype=gurobi.GRB.BINARY, name='aux_xy_u')
    hijl = model.addVars(n, m, vtype=gurobi.GRB.BINARY, name='aux_xy_l')
    model.addConstr(1 == sum(sum(np.array([[hiju[i, j] + hijl[i, j] for j in range(m - 1)] for i in range(n - 1)]))))
    for i in range(n):
        for j in range(m):
            a = hiju[i, j]
            b = hijl[i, j]
            c = hiju[i, j-1] if (j-1) >= 0 else 0
            d = hijl[i-1, j-1] if (j-1) >= 0 and (i-1) >= 0 else 0
            e = hiju[i-1, j-1] if (j-1) >= 0 and (i-1) >= 0 else 0
            f = hijl[i-1, j] if (i-1) >= 0 else 0
            model.addConstr(aij[i, j] <= a + b + c + d + e + f)
    for oo in range(m):
        model.addConstr(hiju[n-1, oo] == 0)
        model.addConstr(hijl[n-1, oo] == 0)
    for oo in range(n):
        model.addConstr(hiju[oo, m-1] == 0)
        model.addConstr(hijl[oo, m-1] == 0)




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