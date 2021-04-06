from utility import *
import  gurobipy as gurobi

def XXX():
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


def YYY():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')

    lower_obj = y + 0
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4

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

    model.setParam("IntegralityFocus", 1)
    model.setObjective(x - 4 * y)
    model.optimize()

def YYY2():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')

    lower_obj = y + 0
    DE = []
    Dobj = []

    expr1 = -3 + x + y  # x + y > 3
    expr2 = 0 + 2 * x - y  # 2x - y > 0
    expr3 = 12 - 2 * x - y  # 2x + y < 0
    expr4 = -4 + 3 * x - 2 * y  # 3x - 2y > 4

    Complementary_great_without_Com(expr1, model, DE, Dobj, 'e1')
    Complementary_great_without_Com(expr2, model, DE, Dobj, 'e2')
    Complementary_great_without_Com(expr3, model, DE, Dobj, 'e3')
    Complementary_great_without_Com(expr4, model, DE, Dobj, 'e4')

    model.update()

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    model.setParam("IntegralityFocus", 1)
    model.setObjective(x - 4 * y)
    model.optimize()
    print(x)
    print(y)



def SinglePro():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')

    lower_obj = 9.5 * x + 1.2 * y + 0
    DE = []
    Dobj = []

    expr1 = -3.54 + x + y  # x + y > 3
    expr2 = 0 + 2 * x - y  # 2x - y > 0
    expr3 = 12 - 2 * x - y  # 2x + y < 0
    expr4 = -4 + 3.5 * x - 2 * y  # 3x - 2y > 4
    expr5 = x
    expr6 = 10 - x
    expr7 = y
    expr8 = 10.6 - y


    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')
    Complementary_great(expr6, model, DE, Dobj, 'e6')
    Complementary_great(expr7, model, DE, Dobj, 'e7')
    Complementary_great(expr8, model, DE, Dobj, 'e8')

    model.update()

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)


    model.setParam("IntegralityFocus", 1)
    model.setObjective(0)
    model.optimize()
    print(lower_obj.getValue())
    print(sum(Dobj).getValue())
    assert (abs(lower_obj.getValue() - sum(Dobj).getValue()) < 0.0001, "Dual obj equal")

def SingleProStrongDual():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')

    lower_obj = 9.5 * x + 1.2 * y + 0
    DE = []
    Dobj = []

    expr1 = -3.54 + x + y  # x + y > 3
    expr2 = 0 + 2 * x - y  # 2x - y > 0
    expr3 = 12 - 2 * x - y  # 2x + y < 0
    expr4 = -4 + 3.5 * x - 2 * y  # 3x - 2y > 4
    expr5 = x
    expr6 = 10 - x
    expr7 = y
    expr8 = 10.6 - y


    Complementary_great_without_Com(expr1, model, DE, Dobj, 'e1')
    Complementary_great_without_Com(expr2, model, DE, Dobj, 'e2')
    Complementary_great_without_Com(expr3, model, DE, Dobj, 'e3')
    Complementary_great_without_Com(expr4, model, DE, Dobj, 'e4')
    Complementary_great_without_Com(expr5, model, DE, Dobj, 'e5')
    Complementary_great_without_Com(expr6, model, DE, Dobj, 'e6')
    Complementary_great_without_Com(expr7, model, DE, Dobj, 'e7')
    Complementary_great_without_Com(expr8, model, DE, Dobj, 'e8')

    model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    model.update()

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)


    model.setParam("IntegralityFocus", 1)
    model.setObjective(0)
    model.optimize()
    print(lower_obj.getValue())
    print(sum(Dobj).getValue())
    assert (abs(lower_obj.getValue() - sum(Dobj).getValue()) < 0.0001, "Dual obj equal")

####################################

def LowerOnlyLowerVars():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 10 - x
    expr7 = y
    expr8 = 1.6 - y


    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')
    Complementary_great(expr6, model, DE, Dobj, 'e6')
    Complementary_great(expr7, model, DE, Dobj, 'e7')
    Complementary_great(expr8, model, DE, Dobj, 'e8')
    model.update()

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    model.optimize()

def LowerOnlyLowerVarsWithoutCom():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 10 - x
    expr7 = y - 1
    expr8 = 1.6 - y


    Complementary_great_without_Com(expr1, model, DE, Dobj, 'e1')
    Complementary_great_without_Com(expr2, model, DE, Dobj, 'e2')
    Complementary_great_without_Com(expr3, model, DE, Dobj, 'e3')
    Complementary_great_without_Com(expr4, model, DE, Dobj, 'e4')
    Complementary_great_without_Com(expr5, model, DE, Dobj, 'e5')
    Complementary_great_without_Com(expr6, model, DE, Dobj, 'e6')
    Complementary_great_without_Com(expr7, model, DE, Dobj, 'e7')
    Complementary_great_without_Com(expr8, model, DE, Dobj, 'e8')
    model.update()

    model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    model.optimize()

############################################

def LowerOnlyLowerVarsSOC():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')
    z = model.addVar(name='z')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 5 - x
    expr7 = y - 1
    expr8 = 1.6 - y
    expr9 = z - 3


    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')
    Complementary_great(expr6, model, DE, Dobj, 'e6')
    Complementary_great(expr7, model, DE, Dobj, 'e7')
    Complementary_great(expr8, model, DE, Dobj, 'e8')
    Complementary_great(expr9, model, DE, Dobj, 'e9')

    Complementary_soc([3, 4], [x, y], [5], [z], model, DE, Dobj, 'e10')
    Complementary_soc([4, 4], [x, y], [3], [z], model, DE, Dobj, 'e11')

    model.update()

    # model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    model.setParam('NonConvex', 2)
    model.optimize()

def LowerOnlyLowerVarsSOCWithoutCom():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')
    z = model.addVar(name='z')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 5 - x
    expr7 = y - 1
    expr8 = 1.6 - y
    expr9 = z - 3


    Complementary_great_without_Com(expr1, model, DE, Dobj, 'e1')
    Complementary_great_without_Com(expr2, model, DE, Dobj, 'e2')
    Complementary_great_without_Com(expr3, model, DE, Dobj, 'e3')
    Complementary_great_without_Com(expr4, model, DE, Dobj, 'e4')
    Complementary_great_without_Com(expr5, model, DE, Dobj, 'e5')
    Complementary_great_without_Com(expr6, model, DE, Dobj, 'e6')
    Complementary_great_without_Com(expr7, model, DE, Dobj, 'e7')
    Complementary_great_without_Com(expr8, model, DE, Dobj, 'e8')
    Complementary_great_without_Com(expr9, model, DE, Dobj, 'e9')

    Complementary_soc_without_Com([3, 4], [x, y], [5], [z], model, DE, Dobj, 'e10')
    Complementary_soc_without_Com([4, 4], [x, y], [3], [z], model, DE, Dobj, 'e11')

    model.update()

    model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    # model.setParam('NonConvex', 2)
    model.optimize()

############################################

def LowerOnlyLowerVarsSOCOne():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')
    z = model.addVar(name='z')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 5 - x
    expr7 = y - 1
    expr8 = 1.6 - y
    expr9 = z - 3


    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')
    Complementary_great(expr6, model, DE, Dobj, 'e6')
    Complementary_great(expr7, model, DE, Dobj, 'e7')
    Complementary_great(expr8, model, DE, Dobj, 'e8')
    Complementary_great(expr9, model, DE, Dobj, 'e9')

    Complementary_soc([3, 4], [x, y], [5], [z], model, DE, Dobj, 'e10')

    model.update()

    # model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    model.setParam('NonConvex', 2)
    model.optimize()
    print(x)
    print(y)
    print(model.getObjective().getValue())

def LowerOnlyLowerVarsSOCWithoutComOne():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')
    z = model.addVar(name='z')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 5 - x
    expr7 = y - 1
    expr8 = 1.6 - y
    expr9 = z - 3


    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')
    Complementary_great(expr6, model, DE, Dobj, 'e6')
    Complementary_great(expr7, model, DE, Dobj, 'e7')
    Complementary_great(expr8, model, DE, Dobj, 'e8')
    Complementary_great(expr9, model, DE, Dobj, 'e9')

    Complementary_soc([3, 4], [x, y], [5], [z], model, DE, Dobj, 'e10')

    model.update()

    model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    model.setParam('NonConvex', 2)
    model.optimize()
    print(x)
    print(y)
    print(model.getObjective().getValue())


def LowerOnlyLowerVarsSOCWithoutComOneModify():
    model = gurobi.Model()

    x = model.addVar(name='x')
    y = model.addVar(name='y')
    z = model.addVar(name='z')

    lower_obj = -13.52 * y + 1.23 * x
    DE = []
    Dobj = []

    expr1 = -3 + x + y          # x + y > 3
    expr2 = 0 + 2 * x - y       # 2x - y > 0
    expr3 = 12 - 2 * x - y      # 2x + y < 0
    expr4 = -4 + 3*x - 2 * y    # 3x - 2y > 4
    expr5 = x
    expr6 = 5 - x
    expr7 = y - 1
    expr8 = 1.6 - y
    expr9 = z - 3



    Complementary_great(expr1, model, DE, Dobj, 'e1')
    Complementary_great(expr2, model, DE, Dobj, 'e2')
    Complementary_great(expr3, model, DE, Dobj, 'e3')
    Complementary_great(expr4, model, DE, Dobj, 'e4')
    Complementary_great(expr5, model, DE, Dobj, 'e5')
    Complementary_great(expr6, model, DE, Dobj, 'e6')
    Complementary_great(expr7, model, DE, Dobj, 'e7')
    Complementary_great(expr8, model, DE, Dobj, 'e8')
    Complementary_great(expr9, model, DE, Dobj, 'e9')

    Complementary_soc_without_Com([3, 4], [x, y], [5], [z], model, DE, Dobj, 'e10')

    model.update()

    model.addConstr(lower_obj == sum(Dobj), name='Strong_Dual')

    lagrange = lower_obj + sum(DE)
    myExpr = MyExpr(lagrange)
    for var in [x, y]:
        exp = myExpr.getCoeff(var)
        myExpr.addConstr(exp, model, '[Lagrange]' + var.VarName)

    model.setParam("IntegralityFocus", 1)
    model.setObjective(2.22 * x + 40 * y)
    model.setParam('NonConvex', 2)
    model.optimize()
    print(x)
    print(y)
    print(model.getObjective().getValue())


if __name__ == "__main__":
    LowerOnlyLowerVarsSOCWithoutComOne()