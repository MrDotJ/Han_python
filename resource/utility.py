import gurobipy as gurobi

M = 1e6


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

    def addConstr(self, expr, model):
        model.addConstr(expr == 0)


def Complementary_great(expr, model, dual_var_name):  # expr should be greater than zero
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(name=dual_var_name)
    var_bin = model.addVar(vtype=gurobi.GRB.BINARY, name=dual_var_name + "_binary")
    model.addConstr(expr >= 0)
    model.addConstr(expr <= M * var_bin)
    model.addConstr(var_dual >= 0)
    model.addConstr(var_dual <= M * (1 - var_bin))
    return var_dual, -1 * expr * var_dual


def Complementary_equal(expr, model, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name=dual_var_name)
    model.addConstr(expr == 0)
    return var_dual, expr * var_dual


import numpy as np


def tonp(vars) -> np.array:
    keys = vars.keys()
    key_last = keys[-1]
    dim = len(key_last)
    shape = list(map(lambda x: x + 1, list(key_last)))
    if dim == 2:
        re = np.empty(tuple(shape), dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                re[i, j] = vars[i, j]
        return re
    if dim == 3:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    re[i, j, k] = vars[i, j, k]
        return re
    if dim == 4:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        re[i, j, k, m] = vars[i, j, k, m]
        return re
    if dim == 5:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        for n in range(shape[4]):
                            re[i, j, k, m, n] = vars[i, j, k, m, n]
        return re


def to_value(vars):
    keys = vars.keys()
    key_last = keys[-1]
    dim = len(key_last)
    shape = list(map(lambda x: x + 1, list(key_last)))
    if dim == 1:
        assert 0
    if dim == 2:
        re = np.empty(tuple(shape), dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                re[i, j] = vars[i, j].getAttr('X')
        return re
    if dim == 3:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    re[i, j, k] = vars[i, j, k].getAttr('X')
        return re
    if dim == 4:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        re[i, j, k, m] = vars[i, j, k, m].getAttr('X')
        return re
    if dim == 5:
        re = np.empty(shape, dtype=object)
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    for m in range(shape[3]):
                        for n in range(shape[4]):
                            re[i, j, k, m, n] = vars[i, j, k, m, n].getAttr('X')
        return re
