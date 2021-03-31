from utility import *
import  gurobipy as gurobi

model = gurobi.Model()

x = model.addVar(name='x')
y = model.addVar(lb=-1 * INF, ub= INF, name='y')

lower_obj = y + 0
DE = []
Dobj = []
expr1 = -3 + x + y
expr2 = 0 + 2 * x - y
expr3 = 12 - 2 * x - y
expr4 = -4 + 3*x - 2 * y
expr02 = y
Complementary_great(expr02, model, DE, Dobj, 'e02')

Complementary_great(expr1, model, DE, Dobj, 'e1')
Complementary_great(expr2, model, DE, Dobj, 'e2')
Complementary_great(expr3, model, DE, Dobj, 'e3')
Complementary_great(expr4, model, DE, Dobj, 'e4')


model.update()

lagrange = lower_obj + sum(DE)
myExpr = MyExpr(lagrange)
for var in [y]:
    exp = myExpr.getCoeff(var)
    myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

# model.setParam("IntegralityFocus", 1)
model.setObjective(x - 4 * y)
model.optimize()

#https://static1.squarespace.com/static/5492d7f4e4b00040889988bd/t/57c06dfdd482e91c235c418b/1472229009395/9_PyomoBilevel.pdf