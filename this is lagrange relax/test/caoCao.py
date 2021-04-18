import gurobipy as gurobi
import numpy as np

M = 1e4
N = 3

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
    model.addConstr(expr >= 0, name='original_feasible_' + dual_var_name)
    return None

def Complementary_equal(expr, model, dual_expression, dual_obj, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    model.addConstr(-1 * expr == 0, name=dual_var_name + '[EqualFeasible]')
    return None



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


def addGenConstrPWL(x_var, y_var, x_value, y_value, model):
    #                         [0,1,2,3] [0,1,4,9]
    segment_num = len(x_value)      # 4
    x_con = model.addVars(segment_num, ub=1)
    model.addConstr(x_var == sum([x_value[i] * x_con[i] for i in range(segment_num)]))
    model.addConstr(y_var == sum([y_value[i] * x_con[i] for i in range(segment_num)]))
    model.addConstr(gurobi.quicksum(x_con) == 1)
    binary = model.addVars(segment_num, vtype=gurobi.GRB.BINARY)  # bin[0]  bin[1]  bin[2]  bin[3]
    for k in range(segment_num):
        model.addConstr(x_con[k] <= binary[k])
    model.addConstr(sum([binary[k] for k in range(segment_num)]) <= 2)
    for sta in range(segment_num):         # 0 1 2 3
        for end in range(segment_num):     # 0 1 2 3
            if end - sta >= 2:             # 0-2 0-3 1-3
                model.addConstr((binary[sta] + binary[end]) <= 1)
    # return [x_con, binary, x_value, y_value]
    return tonp(binary).tolist()