from resource.utility import *
from resource.config3_with_gas import T, K
from math import sqrt


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system, gas_system):
        # ------------ Gas System----------------
        self.well_upper_num = gas_system['well_upper_num']
        self.well_lower_num = gas_system['well_lower_num']
        self.well_upper_quoted_price_max = gas_system['well_upper_quoted_price_max']
        self.well_upper_connection_index = gas_system['well_upper_connection_index']
        self.well_lower_connection_index = gas_system['well_lower_connection_index']

        self.well_upper_output_price = gas_system['well_upper_output_price']
        self.well_lower_output_price = gas_system['well_lower_output_price']
        self.well_upper_output_max = gas_system['well_upper_output_max']
        self.well_upper_output_min = gas_system['well_upper_output_min']
        self.well_lower_output_max = gas_system['well_lower_output_max']
        self.well_lower_output_min = gas_system['well_lower_output_min']

        self.gas_node_num = gas_system['gas_node_num']
        self.gas_node_pressure_min = gas_system['gas_node_pressure_min']
        self.gas_node_pressure_max = gas_system['gas_node_pressure_max']

        self.gas_line_num = gas_system['gas_line_num']
        self.gas_inactive_line_num = gas_system['gas_inactive_line_num']
        self.gas_active_line_num = gas_system['gas_active_line_num']
        self.gas_active_line = gas_system['gas_active_line']
        self.gas_inactive_line = gas_system['gas_inactive_line']

        self.gas_weymouth = gas_system['weymouth']
        self.gas_linepack_coeff = gas_system['gas_linepack_coeff']
        self.gas_pipe_start_node = gas_system['gas_pipe_start_node']
        self.gas_pipe_end_node = gas_system['gas_pipe_end_node']

        self.gas_compressor_num = gas_system['gas_compressor_num']
        self.gas_compressor_coeff = gas_system['gas_compressor_coeff']

        self.gas_load_num = gas_system['gas_load_num']
        self.gas_load = gas_system['gas_load']
        self.gas_load_connection_index = gas_system['gas_load_connection_index']

        # model
        self.model = gurobi.Model()

        self.upper_well_quoted_price = None

        self.upper_well_quoted_price_tuple_dict = None

        self.upper_gas_well_output = None
        self.lower_gas_well_output = None
        self.gas_node_pressure = None
        self.gas_flow_in = None
        self.gas_flow_out = None
        self.gas_linepack = None
        self.aux_weymouth_left = None
        self.aux_weymouth_right_1 = None
        self.aux_weymouth_right_2 = None
        self.pccp_relax = None

        self.dual_expression = 0
        self.dual_expression_basic = 0
        self.dual_expression_additional = 0
        self.lower_objective = 0
        self.upper_objective = 0
        self.dual_node_gas_balance = None
        self.dual_linepack_with_pressure = None
        self.dual_linepack_with_time = None
        self.dual_compressor_consume = None
        self.dual_compressor_pressure_up = None
        self.dual_well_upper_output_min = None
        self.dual_well_upper_output_max = None
        self.dual_well_lower_output_min = None
        self.dual_well_lower_output_max = None
        self.dual_gas_node_pressure_min = None
        self.dual_gas_node_pressure_max = None
        self.dual_gas_flow_in_and_out_great_zero = None
        self.dual_weymouth_aux_left = None
        self.dual_weymouth_relax_left_left = None
        self.dual_weymouth_relax_less_left_1 = None
        self.dual_weymouth_relax_less_left_2 = None
        self.dual_weymouth_relax_left_right = None
        self.dual_pccp_relax_great_zero = None

        self.all_lower_level_vars = []
        self.obj_k = []
        self.do_nothing = 0
        self.equivalent_cost = 0
        self.equivalent_revenue = 0
        self.old_vars_constraints = []

    def build_power_system(self):
        return

    def build_gas_system(self):
        self.upper_well_quoted_price_tuple_dict = self.model.addVars(self.well_upper_num, T, name='upper_gas_quoted_price')
        self.upper_well_quoted_price = tonp(self.upper_well_quoted_price_tuple_dict)

        self.upper_gas_well_output = tonp(self.model.addVars(self.well_upper_num, T, K, name='upper_well_output'))
        self.lower_gas_well_output = tonp(self.model.addVars(self.well_lower_num, T, K, name='lower_well_output'))
        self.gas_node_pressure = tonp(self.model.addVars(self.gas_node_num, T, K, name='gas_node_pressure'))
        self.gas_flow_in = tonp(self.model.addVars(self.gas_line_num, T, K, name='gas_flow_in'))
        self.gas_flow_out = tonp(self.model.addVars(self.gas_line_num, T, K, name='gas_flow_out'))
        self.aux_weymouth_left = tonp(self.model.addVars(self.gas_line_num, T, K, name='weymouth_left_auxiliary', lb=-1 * INFINITY, ub=INFINITY))
        self.aux_weymouth_right_1 = tonp(self.model.addVars(self.gas_line_num, T, K, name='weymouth_right_auxiliary1', lb=-1 * INFINITY, ub=INFINITY))
        self.aux_weymouth_right_2 = tonp(self.model.addVars(self.gas_line_num, T, K, name='weymouth_right_auxiliary2', lb=-1 * INFINITY, ub=INFINITY))
        self.pccp_relax = tonp(self.model.addVars(self.gas_line_num, T, K, name='pccp_relax', lb=-1 * INFINITY, ub=INFINITY))
        self.gas_linepack = tonp(self.model.addVars(self.gas_line_num, T, K, name='gas_linepack'))

        self.dual_node_gas_balance = np.empty((self.gas_node_num, T, K,), dtype=object)
        self.dual_linepack_with_pressure = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_linepack_with_time = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_compressor_consume = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_compressor_pressure_up = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_well_upper_output_min = np.empty((self.well_upper_num, T, K,), dtype=object)
        self.dual_well_upper_output_max = np.empty((self.well_upper_num, T, K,), dtype=object)
        self.dual_well_lower_output_min = np.empty((self.well_lower_num, T, K,), dtype=object)
        self.dual_well_lower_output_max = np.empty((self.well_lower_num, T, K,), dtype=object)
        self.dual_gas_node_pressure_min = np.empty((self.gas_node_num, T, K,), dtype=object)
        self.dual_gas_node_pressure_max = np.empty((self.gas_node_num, T, K,), dtype=object)
        self.dual_gas_flow_in_and_out_great_zero = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_weymouth_aux_left = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_weymouth_relax_left_left = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_weymouth_relax_less_left_1 = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_weymouth_relax_less_left_2 = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_weymouth_relax_left_right = np.empty((self.gas_line_num, T, K,), dtype=object)
        self.dual_pccp_relax_great_zero = np.empty((self.gas_line_num, T, K,), dtype=object)

        self.all_lower_level_vars.extend(self.upper_gas_well_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_gas_well_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_node_pressure.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_in.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_out.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_linepack.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_left.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_right_1.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_right_2.flatten().tolist())
        self.all_lower_level_vars.extend(self.pccp_relax.flatten().tolist())
        self.do_nothing = 1

    def build_heat_system(self):
        return

    def build_power_system_original_and_dual_constraints(self):
        return

    def build_heat_system_original_and_dual_constraints(self):
        return

    def build_gas_system_original_and_dual_constrains(self):
        dual_expr = []

        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(self.upper_gas_well_output[  np.where(self.well_upper_connection_index    == node), t, k].flatten()) +  \
                        sum(self.lower_gas_well_output[  np.where(self.well_lower_connection_index    == node), t, k].flatten()) +  \
                        sum(self.gas_flow_out[           np.where(self.gas_pipe_end_node              == node), t, k].flatten()) -  \
                        sum(self.gas_flow_in[            np.where(self.gas_pipe_start_node            == node), t, k].flatten()) -   \
                        sum(self.gas_load[               np.where(self.gas_load_connection_index      == node), t   ].flatten())
                        # sum((self.upper_chp_power_output[np.where(self.chp_upper_connection_gas_index == node), t, k] *
                        #     self.chp_upper_coeff_p_1[    np.where(self.chp_upper_connection_gas_index == node)      ]).flatten()) + \
                        # sum((self.upper_chp_heat_output[ np.where(self.chp_upper_connection_gas_index == node), t, k] *
                        #     self.chp_upper_coeff_h_1[    np.where(self.chp_upper_connection_gas_index == node)      ]).flatten()) - \
                        # sum((self.lower_chp_power_output[np.where(self.chp_lower_connection_gas_index == node), t, k] *
                        #     self.chp_lower_coeff_p_1[    np.where(self.chp_lower_connection_gas_index == node)      ]).flatten()) + \
                        # sum((self.lower_chp_heat_output[ np.where(self.chp_lower_connection_gas_index == node), t, k] *
                        #     self.chp_lower_coeff_h_1[    np.where(self.chp_lower_connection_gas_index == node)      ]).flatten())
                    self.dual_node_gas_balance[node, t, k], expr1 = Complementary_equal(cons_expr1, self.model, 'dual_node_gas_balance_time_' + str(t) + '_node_' + str(node) + 'scenario_' + str(k))
                    dual_expr.append(expr1)

        for line in self.gas_inactive_line:
            for t in range(0, T-1):
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] + self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, t+1, k] - self.gas_linepack[line, t, k] - self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_linepack_with_pressure[line, t, k], expr1 = Complementary_equal(cons_expr1, self.model, 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_linepack_with_time[line, t, k], expr2 = Complementary_equal(cons_expr2, self.model, 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in self.gas_inactive_line:
            for t in [T-1]:
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] + self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, 0, k] - self.gas_linepack[line, t, k] - self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_linepack_with_pressure[line, t, k], expr1 = Complementary_equal(cons_expr1, self.model, 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_linepack_with_pressure[line, t, k], expr2 = Complementary_equal(cons_expr2, self.model, 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for well in range(self.well_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.upper_gas_well_output[well, t, k] - self.well_upper_output_min[well]
                    cons_expr2 = -1 * self.upper_gas_well_output[well, t, k] + self.well_upper_output_max[well]
                    self.dual_well_upper_output_min[well, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_upper_well_output_min_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_well_upper_output_max[well, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_upper_well_output_max_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for well in range(self.well_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.lower_gas_well_output[well, t, k] - self.well_lower_output_min[well]
                    cons_expr2 = -1 * self.lower_gas_well_output[well, t, k] + self.well_lower_output_max[well]
                    self.dual_well_lower_output_min[well, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_lower_well_output_min_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_well_lower_output_max[well, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_lower_well_output_max_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_node_pressure[node, t, k] - self.gas_node_pressure_min[node]
                    cons_expr2 = self.gas_node_pressure_max[node] - self.gas_node_pressure[node, t, k]
                    self.dual_gas_node_pressure_min[node, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_node_pressure_min_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_gas_node_pressure_max[node, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_node_pressure_max_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_gas_flow_in_and_out_great_zero[line, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_gas_flow_great_zero_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        # for line in range(self.gas_line_num):
        #     for t in range(T):
        #         for k in range(K):
        #             cons_expr1 = self.gas_flow_in[line, t, k] - self.gas_flow_in_min[line]
        #             cons_expr2 = -1 * self.gas_flow_in[line, t, k] + self.gas_flow_in_max[line]
        #             cons_expr3 = self.gas_flow_out[line, t, k] - self.gas_flow_out_min[line]
        #             cons_expr4 = -1 * self.gas_flow_out[line, t, k] + self.gas_flow_out_max[line]
        #             self.dual_gas_flow_in_min[line, t, k],  expr1 = Complementary_great(cons_expr1, self.model, 'dual_gas_flow_in_min'  + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
        #             self.dual_gas_flow_in_max[line, t, k],  expr2 = Complementary_great(cons_expr2, self.model, 'dual_gas_flow_in_max'  + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
        #             self.dual_gas_flow_out_min[line, t, k], expr3 = Complementary_great(cons_expr3, self.model, 'dual_gas_flow_out_min' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
        #             self.dual_gas_flow_out_max[line, t, k], expr4 = Complementary_great(cons_expr4, self.model, 'dual_gas_flow_out_max' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
        #             dual_expr.append(expr1)
        #             dual_expr.append(expr2)
        #             dual_expr.append(expr3)
        #             dual_expr.append(expr4)

        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.pccp_relax[line, t, k]
                    self.dual_pccp_relax_great_zero[line, t, k], expr1 = \
                        Complementary_great(cons_expr1, self.model, 'dual_pccp_relax_great_zero' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for line in self.gas_inactive_line:
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.aux_weymouth_left[line, t, k] - (self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]) / 2
                    self.dual_weymouth_aux_left[line, t, k], expr1 = Complementary_equal(cons_expr1, self.model, 'SOC_less_aux_LINE[' + str(line) + ']_T[' + str(t) + ']_S[' + str(k) + ']')
                    self.dual_weymouth_relax_left_left[line, t, k], self.dual_weymouth_relax_left_right[line, t, k], expr2 = Complementary_soc(
                        [1, sqrt(self.gas_weymouth[line])],
                        [self.aux_weymouth_left[line, t, k], self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]],
                        [sqrt(self.gas_weymouth[line])],
                        [self.gas_node_pressure[self.gas_pipe_start_node[line], t, k]],
                        self.model,
                        'SOC_less_LINE[' + str(line) + ']_T[' + str(t) + ']_S[' + str(k) + ']')
                    self.dual_weymouth_relax_less_left_1[line, t, k] = self.dual_weymouth_relax_left_left[line, t, k][0]
                    self.dual_weymouth_relax_less_left_2[line, t, k] = self.dual_weymouth_relax_left_left[line, t, k][1]
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    # noinspection PyArgumentList
    def update_gas_system_pccp_original_and_dual_constraints(self, pressure_end_old, flow_in_old, flow_out_old):
        self.objection_aux_update = []
        self.model.remove(self.old_vars_constraints)
        self.old_vars_constraints = []
        dual_expr = []
        for k in range(K):
            aux_update_k = []
            for line in self.gas_inactive_line:
                for t in range(T):
                    k1 = self.gas_weymouth[line]
                    k2 = flow_in_old[line, t, k] + flow_out_old[line, t, k]
                    k3 = (flow_in_old[line, t, k] + flow_out_old[line, t, k])**2 / 4
                    k4 = self.gas_weymouth[line] * ((pressure_end_old[self.gas_pipe_end_node[line], t, k])**2)
                    k5 = 2 * self.gas_weymouth[line] * pressure_end_old[self.gas_pipe_end_node[line], t, k]
                    q = np.array([0, -1 * k2 / 2, -1 * k2 / 2, -1 * k5, -1])
                    r = np.array([-1 * k3 - k4])
                    d = sqrt(k1)
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
                        [self.gas_node_pressure[self.gas_pipe_start_node[line], t, k], self.aux_weymouth_right_1[line, t, k]],
                        [1],
                        [self.aux_weymouth_right_2[line, t, k]],
                        self.model,
                        'weymouth_relax_right_soc' + str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.old_vars_constraints.extend([dual_vars1, dual_vars2, dual_left, dual_right])
                    self.old_vars_constraints.extend([constr1, constr2, constr_original, constr_dual])
                    dual_expr.extend([expr1, expr2, expr3])
                    aux_update_k.append((-1 * r[0] - 1) * dual_vars1)
                    aux_update_k.append((-1 * r[0] + 1) * dual_vars1)
            self.objection_aux_update.append(sum(aux_update_k))
        self.dual_expression_additional = sum(dual_expr)
        self.model.update()

    def build_lower_objective(self):
        lower_objs = []
        # for well in range(self.well_upper_num):
        #     for time in range(T):
        #         for k in range(K):
        #             lower_objs.append(
        #                 self.upper_well_quoted_price[well, time] * self.upper_gas_well_output[well, time, k])
        #
        # for well in range(self.well_lower_num):
        #     for time in range(T):
        #         for k in range(K):
        #             lower_objs.append(
        #                 self.well_lower_output_price[well] * self.lower_gas_well_output[well, time, k])

        self.lower_objective = sum(lower_objs)

    def build_kkt_derivative_constraints(self, penalty):
        my_expr = MyExpr(self.dual_expression_basic +
                         self.dual_expression_additional +
                         self.lower_objective +
                         penalty * sum(self.pccp_relax.flatten()))
        self.model.update()
        for var in self.all_lower_level_vars:
            expr = my_expr.getCoeff(var)
            my_expr.addConstr(expr, self.model, var.VarName)

    def build_upper_constraints(self):
        for well in range(self.well_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_well_quoted_price_tuple_dict[well, t],
                    rhs=self.well_upper_quoted_price_max[well],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_gas_well_quoted_price_max' + str(t) + '_well_' + str(well)
                )

    def build_upper_objective(self):
        obj_k = []
        obj_k_p = []
        obj_k_h = []
        for k in range(K):
            objs_cost = []
            objs_revenue = []

            # add gas system
            for load in range(self.gas_load_num):
                for t in range(T):
                    objs_revenue.append(
                        -1 * self.dual_node_gas_balance[self.gas_load_connection_index[load], t, k] * self.gas_load[
                            load, t])

            for well in range(self.well_lower_num):
                for t in range(T):
                    objs_revenue.append(
                        -1 * self.dual_well_lower_output_min[well, t, k] * self.well_lower_output_min[well])
                    objs_revenue.append(
                        1 * self.dual_well_lower_output_max[well, t, k] * self.well_lower_output_max[well])

            for node in range(self.gas_node_num):
                for t in range(T):
                    objs_revenue.append(self.dual_gas_node_pressure_min[node, t, k] * self.gas_node_pressure_min[node])
                    objs_revenue.append(
                        -1 * self.dual_gas_node_pressure_max[node, t, k] * self.gas_node_pressure_max[node])
            # end

            obj_k.append(sum(objs_cost) + sum(objs_revenue))
            obj_k_p.append(sum(objs_cost))
            obj_k_h.append(sum(objs_revenue))

        self.obj_k = obj_k
        self.equivalent_cost = obj_k_p
        self.equivalent_revenue = obj_k_h

    def optimize(self, distribution):
        self.model.setParam("IntegralityFocus", 1)
        self.model.setParam("NonConvex", 2)
        # self.model.setParam("OutputFlag", 0)

        self.model.setObjective(np.array(self.obj_k).dot(np.array(distribution)))
        self.model.setObjective(0)
        self.model.optimize()

        value_generator_quoted_price = to_value(self.upper_well_quoted_price_tuple_dict)
        value_chp_power_quoted_price = to_value(self.upper_well_quoted_price_tuple_dict)
        value_chp_heat_quoted_price = to_value(self.upper_well_quoted_price_tuple_dict)
        obj_k = np.array([obj.getValue() * -1 for obj in self.obj_k])  # change to profile
        return value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price, obj_k



def build_model():
    weymouth = 0.14
    flow_in_old = 1
    flow_out_old = 1
    pressure_end_old = 1
    penalty = 1
    k1 = weymouth
    k2 = flow_in_old + flow_out_old
    k3 = (flow_in_old + flow_out_old) ** 2 / 4
    k4 = weymouth * (pressure_end_old ** 2)
    k5 = 2 * weymouth * pressure_end_old
    q = np.array([0, -1 * k2 / 2, -1 * k2 / 2, -1 * k5, -1])
    r = np.array([-1 * k3 - k4])
    d = sqrt(k1)


    model = gurobi.Model()
    flow_in = model.addVar(lb=-1*gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='flow_in')
    flow_out = model.addVar(lb=-1*gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='flow_out')
    pressure_start = model.addVar(lb=-1*gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='pressure_start')
    pressure_end = model.addVar(lb=-1*gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='pressure_end')
    relax = model.addVar(lb=-1*gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='relax')
    aux_left = model.addVar(lb=-1*gurobi.GRB.INFINITY, ub=1*gurobi.GRB.INFINITY, name='aux_left')
    aux_right1 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=1 * gurobi.GRB.INFINITY, name='aux_right1')
    aux_right2 = model.addVar(lb=-1 * gurobi.GRB.INFINITY, ub=1 * gurobi.GRB.INFINITY, name='aux_right2')


    expr1 = aux_left - (flow_in + flow_out) / 2
    _, lag_expr1 = Complementary_equal(expr1, model, 'aux_left')
    _, _, lag_expr2 = Complementary_soc([1, d], [aux_left, pressure_end], [d], [pressure_start], model, 'left_soc')


    x = np.array([pressure_start, flow_in, flow_out, pressure_end, relax ])
    expr2 = aux_right1 - sum(q * x) - r - 1
    expr3 = aux_right2 - sum(q * x) - r + 1
    _, lag_expr3 = Complementary_equal(expr2, model, 'right_aux1' )
    _, lag_expr4 = Complementary_equal(expr3, model, 'right_aux2' )
    _, _, lag_expr5 = Complementary_soc([2 * d, 1], [pressure_start, aux_right1], [1], [aux_right2], model, 'soc_right')


    lag = lag_expr1 + lag_expr2 + lag_expr3 + lag_expr4 + lag_expr5
    my_expr = MyExpr(lag + penalty * relax)
    model.update()
    for var in [flow_in, flow_out, pressure_start, pressure_end, aux_left, aux_right1, aux_right2, relax]:
        expr = my_expr.getCoeff(var)
        my_expr.addConstr(expr, model, var.VarName)
    model.optimize()

