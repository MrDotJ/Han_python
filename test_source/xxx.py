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


import gurobipy as gurobi
model = gurobi.Model()
x = model.addVar(lb=-1 * 100000, ub=100000)
y = model.addVar(lb=-1 * 100000, ub=100000)
z = model.addVar(lb=-1 * 100000, ub=100000)
x1 = model.addVar(lb=-1 * 100000, ub=100000)
y1 = model.addVar(lb=-1 * 100000, ub=100000)
z1 = model.addVar(lb=-1 * 100000, ub=100000)
model.addConstr(x*x + y*y - z*z <= 0)
model.addConstr(x1*x1 + y1*y1 - z1*z1 <= 0)
model.addConstr(x == x1)
model.optimize()




   weymouth_right_auxiliary1[0,0,0] : <gurobi.LinExpr: -1.0 weymouth_relax_right_auxiliary1_0_t_0_scenario_0 + -1.0 weymouth_relax_right_soc0_t_0_scenario_0left[1]> = 0.0
   weymouth_right_auxiliary2[0,0,0] : <gurobi.LinExpr: -1.0 weymouth_relax_right_auxiliary2_0_t_0_scenario_0 + -1.0 weymouth_relax_right_soc0_t_0_scenario_0right[0]> = 0.0
   pccp_relax[0,0,0] : <gurobi.LinExpr: -1.0 weymouth_relax_right_auxiliary1_0_t_0_scenario_0 + -1.0 weymouth_relax_right_auxiliary2_0_t_0_scenario_0> = -1.0
   SOC_dualweymouth_relax_right_soc0_t_0_scenario_0 : <gurobi.QuadExpr: 0.0 + [ 0.7719999999999999 weymouth_relax_right_soc0_t_0_scenario_0left[0] ^ 2 + weymouth_relax_right_soc0_t_0_scenario_0left[1] ^ 2 + -1.0 weymouth_relax_right_soc0_t_0_scenario_0right[0] ^ 2 ]> <= 0.0




relax_2.display()
Minimize
   <gurobi.LinExpr: 0.0>
Subject To
   weymouth_right_auxiliary1[0,0,0] : <gurobi.LinExpr: -1.0 weymouth_relax_right_auxiliary1_0_t_0_scenario_0 + -1.0 weymouth_relax_right_soc0_t_0_scenario_0left[1]> = 0.0
   weymouth_right_auxiliary2[0,0,0] : <gurobi.LinExpr: -1.0 weymouth_relax_right_auxiliary2_0_t_0_scenario_0 + -1.0 weymouth_relax_right_soc0_t_0_scenario_0right[0]> = 0.0
   pccp_relax[0,0,0] : <gurobi.LinExpr: -1.0 weymouth_relax_right_auxiliary1_0_t_0_scenario_0 + -1.0 weymouth_relax_right_auxiliary2_0_t_0_scenario_0> = -1.0
   SOC_dualweymouth_relax_right_soc0_t_0_scenario_0 : <gurobi.QuadExpr: 0.0 + [ 0.7719999999999999 weymouth_relax_right_soc0_t_0_scenario_0left[0] ^ 2 + weymouth_relax_right_soc0_t_0_scenario_0left[1] ^ 2 + -1.0 weymouth_relax_right_soc0_t_0_scenario_0right[0] ^ 2 ]> <= 0.0
Bounds
   weymouth_left_auxiliary[0,0,0]  free
   weymouth_left_auxiliary[1,0,0]  free
   weymouth_left_auxiliary[2,0,0]  free
   weymouth_right_auxiliary1[0,0,0]  free
   weymouth_right_auxiliary1[1,0,0]  free
   weymouth_right_auxiliary1[2,0,0]  free
   weymouth_right_auxiliary2[0,0,0]  free
   weymouth_right_auxiliary2[1,0,0]  free
   weymouth_right_auxiliary2[2,0,0]  free
   pccp_relax[0,0,0]  free
   pccp_relax[1,0,0]  free
   pccp_relax[2,0,0]  free
   weymouth_relax_left_auxiliary_0_t_0_scenario_0  free
   weymouth_relax_left_soc_0_t_0_scenario_0dual-left[0]  free
   weymouth_relax_left_soc_0_t_0_scenario_0dual-left[1]  free
   weymouth_relax_left_auxiliary_1_t_0_scenario_0  free
   weymouth_relax_left_soc_1_t_0_scenario_0dual-left[0]  free
   weymouth_relax_left_soc_1_t_0_scenario_0dual-left[1]  free
   weymouth_relax_left_auxiliary_2_t_0_scenario_0  free
   weymouth_relax_left_soc_2_t_0_scenario_0dual-left[0]  free
   weymouth_relax_left_soc_2_t_0_scenario_0dual-left[1]  free
   weymouth_relax_right_auxiliary1_0_t_0_scenario_0  free
   weymouth_relax_right_auxiliary2_0_t_0_scenario_0  free
   weymouth_relax_right_soc0_t_0_scenario_0left[0]  free
   weymouth_relax_right_soc0_t_0_scenario_0left[1]  free
   weymouth_relax_right_auxiliary1_1_t_0_scenario_0  free
   weymouth_relax_right_auxiliary2_1_t_0_scenario_0  free
   weymouth_relax_right_soc1_t_0_scenario_0left[0]  free
   weymouth_relax_right_soc1_t_0_scenario_0left[1]  free
   weymouth_relax_right_auxiliary1_2_t_0_scenario_0  free
   weymouth_relax_right_auxiliary2_2_t_0_scenario_0  free
   weymouth_relax_right_soc2_t_0_scenario_0left[0]  free
   weymouth_relax_right_soc2_t_0_scenario_0left[1]  free