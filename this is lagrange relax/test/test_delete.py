import numpy as np
import gurobipy as gurobi

def biGen(x, y, z, x_min, x_max, y_min, y_max, n, m, model):
    xi = np.linspace(x_min, x_max, n)
    yi = np.linspace(y_min, y_max, m)
    zi = xi.reshape((-1, 1)).dot(yi.reshape((1, -1)))

    aij = model.addVars(n, m)
    model.addConstr(x == sum(sum(np.array([[aij[i, j] * xi[i] for j in range(m)] for i in range(n)]))))
    model.addConstr(y == sum(sum(np.array([[aij[i, j] * yi[j] for j in range(m)] for i in range(n)]))))
    model.addConstr(z == sum(sum(np.array([[aij[i, j] * zi[i][j] for j in range(m)] for i in range(n)]))))
    model.addConstr(gurobi.quicksum(aij) == 1)

    hiju = model.addVars(n, m, vtype=gurobi.GRB.BINARY)
    hijl = model.addVars(n, m, vtype=gurobi.GRB.BINARY)
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

if __name__ == '__main__':
    model = gurobi.Model()
    x = model.addVar(ub=10)
    y = model.addVar(ub=10)
    z = model.addVar(ub=10)
    biGen(x, y, z, 0, 10, 0, 10, 10, 10, model)
    model.addConstr(z >= 5)
    model.setObjective(x)
    model.optimize()





