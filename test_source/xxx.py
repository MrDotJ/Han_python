import gurobipy as gurobi

model = gurobi.Model()
x = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
y = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
z = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
x1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
y1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
z1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)

m = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
n = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
p = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)

model.addConstr(x*x + 0.193*y*y-0.193*z*z <= 0)
model.addConstr(x1*x1 + 0.193*y1*y1-0.193*z1*z1 <= 0)
model.addConstr(-1 * m + x == 0)
model.addConstr(-1 * n + x1 == 0)
model.addConstr(-1 * p + 0.5*m == 0)
model.addConstr(-1 * p + 0.5*n == 0)

model.optimize()



model = gurobi.Model()
x = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
y = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
z = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
x1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
y1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
z1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY)
model.addConstr(x*x + y*y - z*z <= 0)
model.addConstr(x1*x1 + y1*y1 - z1*z1 <= 0)
model.addConstr(x == x1)
model.optimize()
