from utility import *

import gurobipy as gurobi

model = gurobi.Model()
var = model.addVars(10, name='x')
model.update()

expr = var[0] * var[1] + var[1] * var[2] + var[2] * var[3] + var[3] * var[4] + var[4] * var[5] + var[5] * var[6] + var[6] * var[7] + var[7] * var[8] + var[8] * var[9]
my_expr = MyExpr(expr)

print (my_expr.getCoeff(var[0]) )
print (my_expr.getCoeff(var[1]) )
print (my_expr.getCoeff(var[2]) )
print (my_expr.getCoeff(var[3]) )

# assert (my_expr.getCoeff(var[0]) ==  (var[1] + 0))
# assert (my_expr.getCoeff(var[1]) == (var[0] + var[2]))
# assert (my_expr.getCoeff(var[2]) == (var[1] + var[3]))
# assert (my_expr.getCoeff(var[3]) == (var[2] + var[4]))

expr = var[0] * var[0] + var[0] * var[1] + var[1] * var[1] + var[2] * var[3] + 4
my_expr = MyExpr(expr)
print (my_expr.getCoeff(var[0])  )
print (my_expr.getCoeff(var[1])  )
# assert (my_expr.getCoeff(var[0]) == 2 * var[0] + var[1])
# assert (my_expr.getCoeff(var[1]) == 2 * var[1] + var[0])

expr = var[0] * var[1] + var[1] * var[0] + var[1] * var[1] + var[0] * var[0]
my_expr = MyExpr(expr)
print(my_expr.getCoeff(var[0]))
print(my_expr.getCoeff(var[1]))
# assert (my_expr.getCoeff(var[0]) == 2 * var[1] + 2 * var[0])
# assert (my_expr.getCoeff(var[1]) == 2 * var[0] + 2 * var[1])


bin = model.addVars(10, vtype=gurobi.GRB.BINARY, name='y')
model.update()
expr = (var[0] + var[1]) * bin[0] + (var[1] + var[2]) * bin[1] + (var[2] + var[3]) * bin[2] + (var[3] + var[4]) * bin[3] + (var[4] + var[5]) * bin[4] + (var[5] + var[6]) * bin[5]
my_expr = MyExpr(expr)
print(my_expr.getCoeff(var[0]))
print(my_expr.getCoeff(var[1]))
# assert (my_expr.getCoeff(var[0]) == bin[0])
# assert (my_expr.getCoeff(var[1]) == bin[0] + bin[1])

