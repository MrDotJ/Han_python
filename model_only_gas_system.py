from resource.utility import *
from resource.config3_with_gas import T, K
from math import sqrt


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system, gas_system):
        # ------------ Gas System----------------
        self.well_upper_num                     = gas_system['well_upper_num']
        self.well_lower_num                     = gas_system['well_lower_num']
        self.well_upper_quoted_price_max        = gas_system['well_upper_quoted_price_max']
        self.well_upper_connection_index        = gas_system['well_upper_connection_index']
        self.well_lower_connection_index        = gas_system['well_lower_connection_index']

        self.well_upper_output_price            = gas_system['well_upper_output_price']
        self.well_lower_output_price            = gas_system['well_lower_output_price']
        self.well_upper_output_max              = gas_system['well_upper_output_max']
        self.well_upper_output_min              = gas_system['well_upper_output_min']
        self.well_lower_output_max              = gas_system['well_lower_output_max']
        self.well_lower_output_min              = gas_system['well_lower_output_min']

        self.gas_node_num                       = gas_system['gas_node_num']
        self.gas_node_pressure_min              = gas_system['gas_node_pressure_min']
        self.gas_node_pressure_max              = gas_system['gas_node_pressure_max']

        self.gas_line_num                       = gas_system['gas_line_num']
        self.gas_inactive_line_num              = gas_system['gas_inactive_line_num']
        self.gas_active_line_num                = gas_system['gas_active_line_num']
        self.gas_active_line                    = gas_system['gas_active_line']
        self.gas_inactive_line                  = gas_system['gas_inactive_line']

        self.gas_weymouth                       = gas_system['weymouth']
        self.gas_linepack_coeff                 = gas_system['gas_linepack_coeff']
        self.gas_pipe_start_node                = gas_system['gas_pipe_start_node']
        self.gas_pipe_end_node                  = gas_system['gas_pipe_end_node']

        self.gas_compressor_num                 = gas_system['gas_compressor_num']
        self.gas_compressor_coeff               = gas_system['gas_compressor_coeff']

        self.gas_load_num                       = gas_system['gas_load_num']
        self.gas_load                           = gas_system['gas_load']
        self.gas_load_connection_index          = gas_system['gas_load_connection_index']

        # model
        self.model = gurobi.Model()

        self.upper_well_quoted_price                        = None

        self.upper_well_quoted_price_tuple_dict             = None

        self.upper_gas_well_output                          = None
        self.lower_gas_well_output                          = None
        self.gas_node_pressure                              = None
        self.gas_flow_in                                    = None
        self.gas_flow_out                                   = None
        self.gas_linepack                                   = None
        self.aux_weymouth_left                              = None
        self.aux_weymouth_right_1                           = None
        self.aux_weymouth_right_2                           = None
        self.pccp_relax                                     = None

        self.all_lower_level_vars                           = []
        self.obj_k                                          = []
        self.do_nothing                                     = 0
        self.equivalent_cost                                = 0
        self.equivalent_revenue                             = 0
        self.old_vars_constraints                           = []
        self.dual_expression_basic                          = 0
        self.lower_objective                                = 0
        self.dual_expression_additional                     = 0

    def build_power_system(self):
        self.do_nothing = 1
    def build_gas_system(self):
        self.upper_well_quoted_price_tuple_dict = self.model.addVars(self.well_upper_num, T, K, name='upper_gas_quoted_price')
        self.upper_well_quoted_price            = tonp( self.upper_well_quoted_price_tuple_dict)

        self.upper_gas_well_output              = tonp( self.model.addVars(self.well_upper_num,        T, K, name='upper_well_output'                                                            ) )
        self.lower_gas_well_output              = tonp( self.model.addVars(self.well_lower_num,        T, K, name='lower_well_output'                                                            ) )
        self.gas_node_pressure                  = tonp( self.model.addVars(self.gas_node_num,          T, K, name='gas_node_pressure'                                                            ) )
        self.gas_flow_in                        = tonp( self.model.addVars(self.gas_line_num,          T, K, name='gas_flow_in'                                                                  ) )
        self.gas_flow_out                       = tonp( self.model.addVars(self.gas_line_num,          T, K, name='gas_flow_out'                                                                 ) )
        self.gas_linepack                       = tonp( self.model.addVars(self.gas_line_num,          T, K, name='gas_linepack'                                                                 ) )
        self.aux_weymouth_left                  = tonp( self.model.addVars(self.gas_line_num,          T, K, name='weymouth_left_auxiliary', lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY ) )
        self.aux_weymouth_right_1               = tonp( self.model.addVars(self.gas_line_num,          T, K, name='weymouth_right_auxiliary1', lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY ) )
        self.aux_weymouth_right_2               = tonp( self.model.addVars(self.gas_line_num,          T, K, name='weymouth_right_auxiliary2', lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY ) )
        self.pccp_relax                         = tonp( self.model.addVars(self.gas_line_num,          T, K, name='pccp_relax'))

        self.all_lower_level_vars.extend(self.upper_gas_well_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_gas_well_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_node_pressure.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_in.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_out.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_linepack.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_left.flatten().tolist())
        self.do_nothing = 1

    def build_heat_system(self):
        self.do_nothing = 1

    def build_power_system_original_and_dual_constraints(self):
        dual_expr = []
        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    def build_heat_system_original_and_dual_constraints(self):
        dual_expr = []
        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    def build_gas_system_original_and_dual_constrains(self):
        dual_expr = []

        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(self.upper_gas_well_output[  np.where(self.well_upper_connection_index == node), t, k].flatten()) +  \
                        sum(self.lower_gas_well_output[  np.where(self.well_lower_connection_index == node), t, k].flatten()) +  \
                        sum(self.gas_flow_out[           np.where(self.gas_pipe_end_node == node), t, k].flatten()) -  \
                        sum(self.gas_flow_in[            np.where(self.gas_pipe_start_node == node), t, k].flatten()) -   \
                        sum(self.gas_load[               np.where(self.gas_load_connection_index == node), t].flatten())
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_node_gas_balance_time_' + str(t) + '_node_' + str(node) + 'scenario_' + str(k))
                    dual_expr.append(expr1)

        for line in self.gas_inactive_line:
            for t in range(0, T-1):
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] + self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, t+1, k] - self.gas_linepack[line, t, k] - self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    _, expr2 = Complementary_equal(cons_expr2, self.model, 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in self.gas_inactive_line:
            for t in [T-1]:
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] + self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, 0, k] - self.gas_linepack[line, t, k] - self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    _, expr2 = Complementary_equal(cons_expr2, self.model, 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in self.gas_active_line:
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_out[line, t, k] - 0.97 * self.gas_flow_in[line, t, k]
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_gas_flow_active_line_' + str(line) + '_time_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for compressor, line in enumerate(self.gas_active_line):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_compressor_coeff[compressor] * self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] - \
                                 self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]
                    _, expr1 = Complementary_great(cons_expr1, self.model, 'dual_compressor_pressure_' + str(compressor) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for well in range(self.well_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.upper_gas_well_output[well, t, k] - self.well_upper_output_min[well]
                    cons_expr2 = -1 * self.upper_gas_well_output[well, t, k] + self.well_upper_output_max[well]
                    _, expr1 = Complementary_great(cons_expr1, self.model, 'dual_upper_well_output_min_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    _, expr2 = Complementary_great(cons_expr2, self.model, 'dual_upper_well_output_max_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for well in range(self.well_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.lower_gas_well_output[well, t, k] - self.well_lower_output_min[well]
                    cons_expr2 = -1 * self.lower_gas_well_output[well, t, k] + self.well_lower_output_max[well]
                    _, expr1 = Complementary_great(cons_expr1, self.model, 'dual_lower_well_output_min_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    _, expr2 = Complementary_great(cons_expr2, self.model, 'dual_lower_well_output_max_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_node_pressure[node, t, k] - self.gas_node_pressure_min[node]
                    cons_expr2 = self.gas_node_pressure_max[node] - self.gas_node_pressure[node, t, k]
                    _, expr1 = Complementary_great(cons_expr1, self.model, 'dual_node_pressure_min_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k))
                    _, expr2 = Complementary_great(cons_expr2, self.model, 'dual_node_pressure_max_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    _, expr1 = Complementary_great(cons_expr1, self.model, 'dual_gas_flow_great_zero_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for line in self.gas_inactive_line:
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.aux_weymouth_left[line, t, k] - (self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]) / 2
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'weymouth_relax_left_auxiliary_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    _, _, expr2 = Complementary_soc(
                        [1, sqrt(self.gas_weymouth[line])],
                        [self.aux_weymouth_left[line, t, k], self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]],
                        [sqrt(self.gas_weymouth[line])],
                        [self.gas_node_pressure[self.gas_pipe_start_node[line], t, k]],
                        self.model,
                        'weymouth_relax_left_soc_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    # noinspection PyArgumentList
    def update_gas_system_pccp_original_and_dual_constraints(self, pressure_end_old, flow_in_old, flow_out_old):
        self.model.remove(self.old_vars_constraints)
        self.old_vars_constraints = []
        dual_expr = []
        for line in self.gas_inactive_line:
            for t in range(T):
                for k in range(K):
                    k1 = self.gas_weymouth[line]
                    k2 = flow_in_old[line, t, k] + flow_out_old[line, t, k]
                    k3 = (flow_in_old[line, t, k] + flow_out_old[line, t, k])**2 / 4
                    k4 = self.gas_weymouth[line] * pressure_end_old[self.gas_pipe_end_node[line]] * pressure_end_old[self.gas_pipe_end_node[line]]
                    k5 = 2 * self.gas_weymouth[line] * pressure_end_old[self.gas_pipe_end_node[line]]
                    q = np.array([0, -1 * k2 / 2, -1 * k2 / 2, k5, -1])
                    r = np.array([-1 * k3 - k4])
                    d = sqrt(k1) / 2
                    x = np.array([self.gas_node_pressure[self.gas_pipe_start_node[line], t, k],
                                  self.gas_flow_in[line, t, k],
                                  self.gas_flow_out[line, t, k],
                                  self.gas_node_pressure[self.gas_pipe_end_node[line], t, k],
                                  self.pccp_relax[line, t, k]
                                  ])
                    cons_expr1 = self.aux_weymouth_right_1[line, t, k] - sum(q*x) - r - 1
                    cons_expr2 = self.aux_weymouth_right_2[line, t, k] - sum(q*x) - r + 1
                    dual_vars1, constr1, expr1 = Complementary_equal_plus(cons_expr1, self.model, 'weymouth_relax_right_auxiliary1_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_vars2, constr2, expr2 = Complementary_equal_plus(cons_expr2, self.model, 'weymouth_relax_right_auxiliary2_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_left, dual_right, constr_original, constr_dual, expr3 = Complementary_soc_plus(
                        [2 * d, 1],
                        [x, self.aux_weymouth_right_1[line, t, k]],
                        [1],
                        [self.aux_weymouth_right_2[line, t, k]],
                        self.model,
                        'weymouth_relax_right_soc' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.old_vars_constraints.extend([dual_vars1, dual_vars2, dual_left, dual_right])
                    self.old_vars_constraints.extend([constr1, constr2, constr_original, constr_dual])
                    dual_expr.extend([expr1, expr2, expr3])
        self.dual_expression_additional = sum(dual_expr)
        self.model.update()


    def build_lower_objective(self):
        lower_objs = []
        self.lower_objective = sum(lower_objs)

    def build_kkt_derivative_constraints(self):
        my_expr = MyExpr(self.dual_expression_basic + self.dual_expression_additional + self.lower_objective)
        for var in self.all_lower_level_vars:
            expr = my_expr.getCoeff(var)
            my_expr.addConstr(expr, self.model)

    def build_upper_constraints(self):
        self.do_nothing = 1


    def build_upper_objective(self):
        obj_k = []
        obj_k_p = []
        obj_k_h = []
        for k in range(K):
            objs_cost = []
            objs_revenue = []
            obj_k.append(sum(objs_cost) + sum(objs_revenue))
            obj_k_p.append(sum(objs_cost))
            obj_k_h.append(sum(objs_revenue))

        self.obj_k = obj_k
        self.equivalent_cost = obj_k_p
        self.equivalent_revenue = obj_k_h


    def optimize(self, distribution):
        self.model.setParam("IntegralityFocus", 1)
        # self.model.setParam("NonConvex", 2)
        self.model.setObjective(np.array(self.obj_k).dot(np.array(distribution)))
        self.model.optimize()

        expected_cost = []

        value_generator_quoted_price = 0
        value_chp_power_quoted_price = 0
        value_chp_heat_quoted_price = 0
        obj_k = [0] * K
        # obj_k = np.array([obj.getValue() * -1 for obj in self.obj_k])              # change to profile
        return value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price, obj_k

    def sss(self):
        self.do_nothing = 1
