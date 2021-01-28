import gurobipy as gurobi

model = gurobi.Model()
INFINITY = gurobi.GRB.INFINITY
from utility import *
from math import sqrt


def Complementary_equal(expr, model, dual_var_name):
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(lb=-1 * INFINITY, ub=INFINITY, name='dual_' + dual_var_name)
    model.addConstr(-1 * expr == 0, name=dual_var_name + '_constrain_equal')
    return var_dual, -1 * expr * var_dual


def Complementary_soc(left_coeff, left_var, right_coeff, right_var, model, dual_var_name):
    left_var_length = len(left_coeff)
    right_var_length = len(right_coeff)
    dual_left = model.addVars(left_var_length, lb=-1 * INFINITY, ub=INFINITY,
                              name=dual_var_name + 'dual-left')
    dual_right = model.addVars(right_var_length, lb=0, ub=INFINITY,
                               name=dual_var_name + 'dual-right')
    expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * left_var[i] * left_var[i]
                                 for i in range(left_var_length)])
    expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * right_var[i] * right_var[i]
                                  for i in range(right_var_length)])
    model.addConstr(lhs=expr_left, sense=gurobi.GRB.LESS_EQUAL, rhs=expr_right, name=dual_var_name + 'con_original')
    dual_expr_left = gurobi.quicksum([left_coeff[i] * left_coeff[i] * dual_left[i] * dual_left[i]
                                      for i in range(left_var_length)])
    dual_expr_right = gurobi.quicksum([right_coeff[i] * right_coeff[i] * dual_right[i] * dual_right[i]
                                       for i in range(right_var_length)])
    model.addConstr(lhs=dual_expr_left, sense=gurobi.GRB.LESS_EQUAL, rhs=dual_expr_right,
                    name=dual_var_name + 'con_dual')

    lagrange_sum = gurobi.quicksum([left_coeff[i] * left_var[i] * dual_left[i] for i in range(left_var_length)]) + \
                   gurobi.quicksum([right_coeff[i] * right_var[i] * dual_right[i] for i in range(right_var_length)])
    return dual_left, dual_right, -1 * lagrange_sum


def Complementary_great(expr, model, dual_var_name):  # expr should be greater than zero
    assert (type(expr) == gurobi.LinExpr or type(expr) == gurobi.Var)
    var_dual = model.addVar(name='dual_' + dual_var_name)
    var_bin = model.addVar(vtype=gurobi.GRB.BINARY, name='dual' + dual_var_name + "_binary")
    model.addConstr(expr >= 0, name=dual_var_name + 'original_great')
    model.addConstr(expr <= M * var_bin , name=dual_var_name + 'original_M_great')
    model.addConstr(var_dual >= 0, name=dual_var_name + 'dual_great')
    model.addConstr(var_dual <= M * (1 - var_bin), name=dual_var_name + 'dual_M_great')
    return var_dual, -1 * expr * var_dual


gas_node_num = 4
T = 1
K = 1
#  0     1      2
#  o-----o------o
#     0  |  2
#      1 |
#        o
#        3
upper_well_output = tonp(model.addVars(1, T, K, name='upper_well_output'))
lower_well_output = tonp(model.addVars(1, T, K, name='lower_well_output'))
gas_flow_out      = tonp(model.addVars(3, T, K, name='gas_flow_out'))
gas_flow_in       = tonp(model.addVars(3, T, K, name='gas_flow_in'))
gas_node_pressure = tonp(model.addVars(4, T, K, name='gas_node_pressure'))
aux_weymouth_left = tonp(model.addVars(3, T, K, name='aux_weymouth_left'))
gas_linepack      = tonp(model.addVars(3, T, K, name='gas_linepack'))

gas_load = np.array([[1, 1, 1]])
well_upper_connection_index = np.array([0])
well_lower_connection_index = np.array([3])
gas_pipe_end_node = np.array([1, 1, 2])
gas_pipe_start_node = np.array([0, 3, 1])
gas_load_connection_index = np.array([2])
gas_inactive_line = [0, 1, 2]
gas_weymouth = np.array([1, 1, 1, 1, 1])
gas_node_pressure_min = np.array([0, 0, 0, 0])
gas_node_pressure_max = np.array([10, 10, 10, 10])
gas_linepack_coeff = np.array([1, 1, 1, 1, 1])

dual_expr = []
all_lower_level_vars = []
all_lower_level_vars.extend(upper_well_output.flatten().tolist())
all_lower_level_vars.extend(lower_well_output.flatten().tolist())
all_lower_level_vars.extend(gas_flow_out.flatten().tolist())
all_lower_level_vars.extend(gas_flow_in.flatten().tolist())
all_lower_level_vars.extend(gas_node_pressure.flatten().tolist())
all_lower_level_vars.extend(aux_weymouth_left.flatten().tolist())

for node in range(gas_node_num):
    for t in range(T):
        for k in range(K):
            cons_expr1 = \
                sum(upper_well_output[np.where(well_upper_connection_index == node), t, k].flatten()) + \
                sum(lower_well_output[np.where(well_lower_connection_index == node), t, k].flatten()) + \
                sum(gas_flow_out[np.where(gas_pipe_end_node == node), t, k].flatten()) - \
                sum(gas_flow_in[np.where(gas_pipe_start_node == node), t, k].flatten()) - \
                sum(gas_load[np.where(gas_load_connection_index == node), t].flatten())
            _, expr1 = Complementary_equal(cons_expr1, model,
                   'node_gas_balance_time_' + str(t) + '_node_' + str(node) + '_scenario_' + str(k))
            dual_expr.append(expr1)
            
for node in range(gas_node_num):
    for t in range(T):
        for k in range(K):
            cons_expr1 = gas_node_pressure[node, t, k] - gas_node_pressure_min[node]
            cons_expr2 = gas_node_pressure_max[node] - gas_node_pressure[node, t, k]
            _, expr1 = Complementary_great(cons_expr1, model, 'node_pressure_min_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k))
            _, expr2 = Complementary_great(cons_expr2, model, 'node_pressure_max_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k))
            dual_expr.append(expr1)
            dual_expr.append(expr2)

for line in gas_inactive_line:
    for t in range(0, T-1):
        for k in range(K):
            cons_expr1 = gas_linepack[line, t, k] - gas_linepack_coeff[line] * (
                    gas_node_pressure[gas_pipe_start_node[line], t, k] + gas_node_pressure[gas_pipe_end_node[line], t, k]) / 2
            cons_expr2 = gas_linepack[line, t+1, k] - gas_linepack[line, t, k] - gas_flow_in[line, t, k] + gas_flow_out[line, t, k]
            _, expr1 = Complementary_equal(cons_expr1, model, 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
            _, expr2 = Complementary_equal(cons_expr2, model, 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
            dual_expr.append(expr1)
            dual_expr.append(expr2)

for line in gas_inactive_line:
    for t in [T-1]:
        for k in range(K):
            cons_expr1 = gas_linepack[line, t, k] - gas_linepack_coeff[line] * (
                    gas_node_pressure[gas_pipe_start_node[line], t, k] + gas_node_pressure[gas_pipe_end_node[line], t, k]) / 2
            cons_expr2 = gas_linepack[line, 0, k] - gas_linepack[line, t, k] - gas_flow_in[line, t, k] + gas_flow_out[line, t, k]
            _, expr1 = Complementary_equal(cons_expr1, model, 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
            _, expr2 = Complementary_equal(cons_expr2, model, 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
            dual_expr.append(expr1)
            dual_expr.append(expr2)



for line in gas_inactive_line:
    for t in range(T):
        for k in range(K):
            cons_expr1 = aux_weymouth_left[line, t, k] - (
                    gas_flow_in[line, t, k] + gas_flow_out[line, t, k]) / 2
            _, expr1 = Complementary_equal(cons_expr1, model,
                   'weymouth_relax_left_auxiliary_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
            _, _, expr2 = Complementary_soc(
                [1, sqrt(gas_weymouth[line])],
                [aux_weymouth_left[line, t, k], gas_node_pressure[gas_pipe_end_node[line], t, k]],
                [sqrt(gas_weymouth[line])],
                [gas_node_pressure[gas_pipe_start_node[line], t, k]],
                model,
                'weymouth_relax_left_soc_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
            dual_expr.append(expr1)
            dual_expr.append(expr2)

dual_expression_basic = sum(dual_expr)
my_expr = MyExpr(dual_expression_basic)
model.update()
for var in all_lower_level_vars:
    expr = my_expr.getCoeff(var)
    my_expr.addConstr(expr, model, var.VarName + '_derivation')
    
model.update()
model.optimize()
# model.setParam('OutputFlag', 0)
# cons = model.getConstrs()
# ii = 3
# print(len(cons))
# for i in range(3, 12):
#     model.remove(cons[i])
# for i in range(14, 15):
#     model.remove(cons[i])
# for i in range(16, 17):
#     model.remove(cons[i])
# for i in range(18, 19):
#     model.remove(cons[i])
# for i in range(20, 29):
#     model.remove(cons[i])
# for i in range(31, 35):
#     model.remove(cons[i])
# ii = 36
# while 1:
#     try:
#         model.remove(cons[ii])
#         model.optimize()
#         break
#     except gurobi.GurobiError:
#         print(ii)
#         ii = ii + 1
#     except IndexError:
#         print('end')
#         break
#
#
#
# model.update()
# cons = model.getConstrs()
# for i in range(0, 2):
#     model.remove(cons[i])
# for i in range(8, 9):
#     model.remove(cons[i])
# model.remove(cons[-1])
#
#
# print('all 9 constraints')
#
# model.update()
# cons = model.getConstrs()
# model.remove(cons[1])
#
#
# model.update()
# cons = model.getConstrs()
# cons2 = model.getQConstrs()
# model.remove(cons2[0])
# model.update()
#
# model = model.relax()
# cons = model.getConstrs()
# model.remove(cons[0])
# ii = 0
#
# while 1:
#     try:
#         model.remove(cons[ii])
#         model.optimize()
#         print('remove ' + str(ii) + ' success')
#         break
#     except gurobi.GurobiError:
#         print(ii)
#         ii = ii + 1
#     except IndexError:
#         print('end')
#         break