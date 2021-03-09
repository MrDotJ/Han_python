from resource.utility import *
from resource.config3_with_gas import T, K
from math import sqrt


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system, gas_system):
        # ------------ Power System----------------
        self.ele_node_num                       = power_system['node_num']
        self.ele_line_num                       = power_system['line_num']
        self.ele_line_capacity                  = power_system['line_capacity']
        self.line_reactance                     = power_system['reactance']
        self.ele_line_start                     = power_system['line_start']
        self.ele_line_end                       = power_system['line_end']

        self.generator_upper_connection_index   = power_system['upper_generator_connection_index']
        self.generator_upper_num                = power_system['upper_generator_num']
        self.generator_upper_max                = power_system['upper_generator_max']
        self.generator_upper_min                = power_system['upper_generator_min']
        self.generator_upper_ramp_up            = power_system['upper_generator_ramp_up']
        self.generator_upper_ramp_down          = power_system['upper_generator_ramp_down']
        self.generator_upper_cost               = power_system['upper_generator_cost']
        self.upper_generator_quoted_price_max   = power_system['upper_generator_quoted_price_max']

        self.generator_lower_connection_index   = power_system['lower_generator_connection_index']
        self.generator_lower_num                = power_system['lower_generator_num']
        self.generator_lower_max                = power_system['lower_generator_max']
        self.generator_lower_min                = power_system['lower_generator_min']
        self.generator_lower_ramp_up            = power_system['lower_generator_ramp_up']
        self.generator_lower_ramp_down          = power_system['lower_generator_ramp_down']
        self.generator_lower_cost               = power_system['lower_generator_cost']

        self.ele_load_num                       = power_system['load_num']
        self.ele_load_index                     = power_system['load_index']
        self.ele_load                           = power_system['load']

        self.wind_connection_index              = power_system['wind_connection_index']
        self.wind_output                        = power_system['wind_output']
        self.wind_farm_num                      = power_system['wind_farm_num']

        # ------------ Heat System----------------
        self.heat_node_num                      = heat_system['node_num']
        self.heat_pipe_num                      = heat_system['pipe_num']
        self.heat_pipe_length                   = heat_system['heat_pipe_length']
        self.heat_pipe_start_node_supply        = heat_system['heat_pipe_start_node_supply']
        self.heat_pipe_start_node_return        = heat_system['heat_pipe_start_node_return']
        self.heat_pipe_end_node_supply          = heat_system['heat_pipe_end_node_supply']
        self.heat_pipe_end_node_return          = heat_system['heat_pipe_end_node_return']
        self.heat_pipe_water_flow               = heat_system['line_water_flow']

        self.heat_heater_num                    = heat_system['heater_num']
        self.heat_exchanger_num                 = heat_system['exchanger_num']



        self.heater_connection_index            = heat_system['heater_connection_index']          # same with supply and return
        self.exchanger_connection_index         = heat_system['exchanger_connection_index']

        self.heater_tempe_supply_max            = heat_system['heater_tempe_supply_max']
        self.heater_tempe_supply_min            = heat_system['heater_tempe_supply_min']
        self.heater_tempe_return_max            = heat_system['heater_tempe_return_max']
        self.heater_tempe_return_min            = heat_system['heater_tempe_return_min']

        self.exchanger_tempe_supply_max         = heat_system['exchanger_tempe_supply_max']
        self.exchanger_tempe_supply_min         = heat_system['exchanger_tempe_supply_min']
        self.exchanger_tempe_return_max         = heat_system['exchanger_tempe_return_max']
        self.exchanger_tempe_return_min         = heat_system['exchanger_tempe_return_min']

        self.chp_upper_connection_power_index   = heat_system['chp_upper_connection_power_index']
        self.chp_lower_connection_power_index   = heat_system['chp_lower_connection_power_index']
        self.chp_upper_connection_gas_index     = gas_system['chp_upper_connection_gas_index']
        self.chp_lower_connection_gas_index     = gas_system['chp_lower_connection_gas_index']
        self.chp_upper_connection_heater_index  = heat_system['upper_chp_connection_heater_index']
        self.chp_lower_connection_heater_index  = heat_system['lower_chp_connection_heater_index']

        self.heat_load                          = heat_system['load']

        # -------------- chp system -------------
        self.chp_upper_num                      = chp_system['chp_upper_num']
        self.chp_lower_num                      = chp_system['chp_lower_num']
        self.chp_point_num                      = chp_system['chp_point_num']
        self.upper_chp_power_quoted_price_max   = chp_system['upper_chp_power_quoted_price_max']
        self.upper_chp_heat_quoted_price_max    = chp_system['upper_chp_heat_quoted_price_max']
        self.upper_chp_POWER                    = chp_system['upper_chp_POWER']
        self.upper_chp_HEAT                     = chp_system['upper_chp_HEAT']
        self.lower_chp_POWER                    = chp_system['lower_chp_POWER']
        self.lower_chp_HEAT                     = chp_system['lower_chp_HEAT']

        self.chp_upper_coeff_p_1                = chp_system['chp_upper_coeff_p_1']
        self.chp_upper_coeff_p_2                = chp_system['chp_upper_coeff_p_2']
        self.chp_upper_coeff_h_1                = chp_system['chp_upper_coeff_h_1']
        self.chp_upper_coeff_h_2                = chp_system['chp_upper_coeff_h_2']
        self.chp_upper_coeff_cross              = chp_system['chp_upper_coeff_cross']
        self.chp_upper_coeff_const              = chp_system['chp_upper_coeff_const']
        self.chp_lower_coeff_p_1                = chp_system['chp_lower_coeff_p_1']
        self.chp_lower_coeff_p_2                = chp_system['chp_lower_coeff_p_2']
        self.chp_lower_coeff_h_1                = chp_system['chp_lower_coeff_h_1']
        self.chp_lower_coeff_h_2                = chp_system['chp_lower_coeff_h_2']
        self.chp_lower_coeff_cross              = chp_system['chp_lower_coeff_cross']
        self.chp_lower_coeff_const              = chp_system['chp_lower_coeff_const']

        # ------------ Gas System----------------
        self.well_upper_num                     = gas_system['well_upper_num']
        self.well_lower_num                     = gas_system['well_lower_num']
        self.well_upper_quoted_price_max        = gas_system['well_upper_quoted_price_max']
        self.well_upper_connection_index        = gas_system['well_upper_connection_index']
        self.well_lower_connection_index        = gas_system['well_lower_connection_index']

        self.well_upper_cost                    = gas_system['well_upper_output_price']
        self.well_lower_cost                    = gas_system['well_lower_output_price']
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

        self.gas_flow_in_min                    = gas_system['gas_flow_in_min']
        self.gas_flow_in_max                    = gas_system['gas_flow_in_max']
        self.gas_flow_out_min                   = gas_system['gas_flow_out_min']
        self.gas_flow_out_max                   = gas_system['gas_flow_out_max']

        # model
        self.model = gurobi.Model()

        self.upper_generator_quoted_price                   = None
        self.upper_chp_power_quoted_price                   = None
        self.upper_chp_heat_quoted_price                    = None
        self.upper_well_quoted_price                        = None

        self.upper_generator_quoted_price_tuple_dict        = None
        self.upper_chp_power_quoted_price_tuple_dict        = None
        self.upper_chp_heat_quoted_price_tuple_dict         = None
        self.upper_well_quoted_price_tuple_dict             = None

        self.upper_generator_power_output                   = None
        self.lower_generator_power_output                   = None

        self.upper_chp_power_output                         = None
        self.lower_chp_power_output                         = None
        self.upper_chp_heat_output                          = None
        self.lower_chp_heat_output                          = None


        self.heat_node_tempe_supply                         = None
        self.heat_node_tempe_return                         = None
        self.heat_pipe_start_tempe_supply                   = None
        self.heat_pipe_end_tempe_supply                     = None
        self.heat_pipe_start_tempe_return                   = None
        self.heat_pipe_end_tempe_return                     = None
        self.upper_chp_point                                = None
        self.lower_chp_point                                = None
        self.dual_expression                                = 0
        self.dual_expression_basic                          = 0
        self.dual_expression_additional                     = 0
        self.lower_objective                                = None
        self.upper_objective                                = None

        self.dual_lower_chp_point_sum_one                   = None
        self.dual_lower_chp_power_output                    = None
        self.dual_lower_chp_heat_output                     = None
        self.dual_upper_chp_power_output                    = None
        self.dual_upper_chp_heat_output                     = None
        self.dual_upper_chp_point_sum_one                   = None
        self.dual_lower_chp_point_less_one                  = None
        self.dual_lower_chp_point_great_zero                = None
        self.dual_upper_chp_point_less_one                  = None
        self.dual_upper_chp_point_great_zero                = None
        self.dual_exchanger_balance                         = None
        self.dual_heater_supply_min                         = None
        self.dual_heater_supply_max                         = None
        self.dual_heater_return_min                         = None
        self.dual_heater_return_max                         = None
        self.dual_exchanger_supply_min                      = None
        self.dual_exchanger_supply_max                      = None
        self.dual_exchanger_return_min                      = None
        self.dual_exchanger_return_max                      = None
        self.dual_heater_balance                            = None


        self.all_lower_level_vars                           = []
        self.obj_k                                          = []
        self.do_nothing                                     = 0
        self.equivalent_cost                                = 0
        self.equivalent_revenue                             = 0
        self.old_vars_constraints                           = []
        self.objection_aux_update                           = []

    def build_power_system(self):
        return

    def build_gas_system(self):
        return

    def build_heat_system(self):
        self.upper_chp_heat_quoted_price_tuple_dict = self.model.addVars(self.chp_upper_num, T, lb=0, name='upper_chp_heat_quoted_price')
        self.upper_chp_heat_quoted_price            = tonp( self.upper_chp_heat_quoted_price_tuple_dict )

        self.upper_chp_point                    = tonp( self.model.addVars(self.chp_upper_num, self.chp_point_num, T, K, name='upper_chp_point',          lb=-1 * INFINITY, ub=INFINITY ) )
        self.lower_chp_point                    = tonp( self.model.addVars(self.chp_lower_num, self.chp_point_num, T, K, name='lower_chp_point',          lb=-1 * INFINITY, ub=INFINITY ) )
        self.upper_chp_heat_output              = tonp( self.model.addVars(self.chp_upper_num, T, K, name='upper_chp_heat_output',                        lb=-1 * INFINITY, ub=INFINITY ) )
        self.lower_chp_heat_output              = tonp( self.model.addVars(self.chp_lower_num, T, K, name='lower_chp_heat_output',                        lb=-1 * INFINITY, ub=INFINITY ) )
        self.heat_node_tempe_supply             = tonp( self.model.addVars(self.heat_node_num, T, K, name='heat_node_temperature_supply',                 lb=-1 * INFINITY, ub=INFINITY ) )
        self.heat_node_tempe_return             = tonp( self.model.addVars(self.heat_node_num, T, K, name='heat_node_temperature_return',                 lb=-1 * INFINITY, ub=INFINITY ) )
        self.heat_pipe_start_tempe_supply       = tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_start_temperature_supply_network',   lb=-1 * INFINITY, ub=INFINITY ) )
        self.heat_pipe_end_tempe_supply         = tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_end_temperature_supply_network',     lb=-1 * INFINITY, ub=INFINITY ) )
        self.heat_pipe_start_tempe_return       = tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_start_temperature_return_network',   lb=-1 * INFINITY, ub=INFINITY ) )
        self.heat_pipe_end_tempe_return         = tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_end_temperature_return_network',     lb=-1 * INFINITY, ub=INFINITY ) )

        self.dual_lower_chp_point_sum_one       = np.empty((self.chp_lower_num,                     T, K, ), dtype=object)
        self.dual_lower_chp_heat_output         = np.empty((self.chp_lower_num,                     T, K, ), dtype=object)
        self.dual_upper_chp_heat_output         = np.empty((self.chp_upper_num,                     T, K, ), dtype=object)
        self.dual_upper_chp_point_sum_one       = np.empty((self.chp_upper_num,                     T, K, ), dtype=object)
        self.dual_lower_chp_point_less_one      = np.empty((self.chp_lower_num, self.chp_point_num, T, K, ), dtype=object)
        self.dual_lower_chp_point_great_zero    = np.empty((self.chp_lower_num, self.chp_point_num, T, K, ), dtype=object)
        self.dual_upper_chp_point_less_one      = np.empty((self.chp_upper_num, self.chp_point_num, T, K, ), dtype=object)
        self.dual_upper_chp_point_great_zero    = np.empty((self.chp_upper_num, self.chp_point_num, T, K, ), dtype=object)
        self.dual_exchanger_balance             = np.empty((self.heat_exchanger_num,                T, K, ), dtype=object)
        self.dual_heater_supply_min             = np.empty((self.heat_heater_num,                   T, K, ), dtype=object)
        self.dual_heater_supply_max             = np.empty((self.heat_heater_num,                   T, K, ), dtype=object)
        self.dual_heater_return_min             = np.empty((self.heat_heater_num,                   T, K, ), dtype=object)
        self.dual_heater_return_max             = np.empty((self.heat_heater_num,                   T, K, ), dtype=object)
        self.dual_exchanger_supply_min          = np.empty((self.heat_exchanger_num,                T, K, ), dtype=object)
        self.dual_exchanger_supply_max          = np.empty((self.heat_exchanger_num,                T, K, ), dtype=object)
        self.dual_exchanger_return_min          = np.empty((self.heat_exchanger_num,                T, K, ), dtype=object)
        self.dual_exchanger_return_max          = np.empty((self.heat_exchanger_num,                T, K, ), dtype=object)
        self.dual_heater_balance                = np.empty((self.heat_heater_num,                   T, K, ), dtype=object)


        self.all_lower_level_vars.extend(self.upper_chp_point.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_chp_point.flatten().tolist())
        self.all_lower_level_vars.extend(self.upper_chp_heat_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_chp_heat_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_node_tempe_supply.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_node_tempe_return.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_start_tempe_supply.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_end_tempe_supply.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_start_tempe_return.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_end_tempe_return.flatten().tolist())

    def build_power_system_original_and_dual_constraints(self):
        return

    # 构建 热网 部分
    def build_heat_system_original_and_dual_constraints(self):
        dual_expr = []

        for chp in range(self.chp_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr2 = ( (self.upper_chp_point[chp, :, t, k].reshape((1, -1))).dot(self.upper_chp_HEAT[chp, :].reshape((-1, 1)))  )[0][0] - self.upper_chp_heat_output[chp, t, k]
                    cons_expr3 = sum(self.upper_chp_point[chp, :, t, k]) - 1
                    self.dual_upper_chp_heat_output[chp, t, k]  , expr2 = Complementary_equal(-1 * cons_expr2, self.model, 'dual_upper_chp_heat_output_' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                    self.dual_upper_chp_point_sum_one[chp, t, k], expr3 = Complementary_equal(cons_expr3, self.model, 'dual_upper_chp_point_sum_one' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)
        for chp in range(self.chp_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr2 = (  (self.lower_chp_point[chp, :, t, k].reshape((1, -1))).dot(self.lower_chp_HEAT[chp, :]. reshape((-1, 1)))   )[0][0] - self.lower_chp_heat_output[chp, t, k]
                    cons_expr3 = sum(self.lower_chp_point[chp, :, t, k]) - 1
                    self.dual_lower_chp_heat_output[chp, t, k]  , expr2 = Complementary_equal(-1 * cons_expr2, self.model, 'dual_lower_chp_heat_output_' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                    self.dual_lower_chp_point_sum_one[chp, t, k], expr3 = Complementary_equal(cons_expr3, self.model, 'dual_lower_chp_point_sum_one' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)

        for chp in range(self.chp_upper_num):
            for point in range(self.chp_point_num):
                for t in range(T):
                    for k in range(K):
                        cons_expr1 = self.upper_chp_point[chp, point, t, k]
                        cons_expr2 = -1 * self.upper_chp_point[chp, point, t, k] + 1
                        self.dual_upper_chp_point_great_zero[chp, point, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_upper_chp_point_great_zero' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                        self.dual_upper_chp_point_less_one[chp, point, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_upper_chp_point_less_one' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                        dual_expr.append(expr1)
                        dual_expr.append(expr2)

        for chp in range(self.chp_lower_num):
            for point in range(self.chp_point_num):
                for t in range(T):
                    for k in range(K):
                        cons_expr1 = self.lower_chp_point[chp, point, t, k]
                        cons_expr2 = -1 * self.lower_chp_point[chp, point, t, k] + 1
                        self.dual_lower_chp_point_great_zero[chp, point, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_lower_chp_point_great_zero' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                        self.dual_lower_chp_point_less_one[chp, point, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_lower_chp_point_less_one' + str(t) + '_' + str(chp) + 'scenario' + str(k))
                        dual_expr.append(expr1)
                        dual_expr.append(expr2)

        for heater in range(self.heat_heater_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(sum(self.upper_chp_heat_output[np.where(self.chp_upper_connection_heater_index == heater), t, k] )) + \
                        sum(sum(self.lower_chp_heat_output[np.where(self.chp_lower_connection_heater_index == heater), t, k] )) - \
                        0.1 * sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_start_node_supply == self.heater_connection_index[heater])]) * \
                        (self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] -
                         self.heat_node_tempe_return[self.heater_connection_index[heater], t, k])
                    self.dual_heater_balance[heater, t, k], expr1 = Complementary_equal(1 * cons_expr1, self.model, 'dual_heater_balance' + str(t) + '_' + str(heater) + 'scenario' + str(k))
                    dual_expr.append(expr1)

        for exchanger in range(self.heat_exchanger_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_load[exchanger, t] - \
                                 0.1 * sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_supply == self.exchanger_connection_index[exchanger])]) * \
                                 (self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] -
                                  self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k])
                    self.dual_exchanger_balance[exchanger, t, k], expr1 = Complementary_equal(-1*cons_expr1, self.model, 'dual_exchanger_balance' + str(t) + '_' + str(exchanger) + str(k))
                    dual_expr.append(expr1)

        for line in range(self.heat_pipe_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_pipe_start_tempe_supply[line, t, k] - self.heat_node_tempe_supply[self.heat_pipe_start_node_supply[line], t, k]
                    cons_expr2 = self.heat_pipe_start_tempe_return[line, t, k] - self.heat_node_tempe_return[self.heat_pipe_start_node_return[line], t, k]
                    _, expr1 = Complementary_equal(-1 * cons_expr1, self.model, 'dual_line_temp_start_supply_' + str(t) + '_' + str(line) + 'scenario' + str(k))
                    _, expr2 = Complementary_equal(-1 * cons_expr2, self.model, 'dual_line_temp_start_return' + str(t) + '_' + str(line) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for node in range(self.heat_node_num):      # mix constrains
            for t in range(T):
                for k in range(K):
                    cons_expr1 = ( (self.heat_pipe_end_tempe_supply[np.where(self.heat_pipe_end_node_supply == node), t, k].reshape((1, -1))  ).dot(
                                      (self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_supply == node)].reshape((-1, 1)))           )  )[0][0] - \
                                 self.heat_node_tempe_supply[node, t, k] * \
                                 (sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_supply == node)]))
                    cons_expr2 = ( (self.heat_pipe_end_tempe_return[np.where(self.heat_pipe_end_node_return == node), t, k].reshape((1, -1)) ).dot(
                                   (self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_return == node)].reshape((-1, 1)))              ) )[0][0] - \
                                 self.heat_node_tempe_return[node, t, k] * \
                                 (sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_return == node)]))
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_mix_constraints_supply' + str(t) + '_' + str(node) + 'scenario' + str(k))
                    _, expr2 = Complementary_equal(cons_expr2, self.model, 'dual_mix_constraints_return' + str(t) + '_' + str(node) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in range(self.heat_pipe_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_pipe_end_tempe_supply[line, t, k] - ((1 - 0.000 * (self.heat_pipe_length[line] * 1) / 1000) * self.heat_pipe_start_tempe_supply[line, t, k])
                    cons_expr2 = self.heat_pipe_end_tempe_return[line, t, k] - ((1 - 0.000 * (self.heat_pipe_length[line] * 1) / 1000) * self.heat_pipe_start_tempe_return[line, t, k])
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_heat_loss_supply' + str(t) + '_' + str(line) + 'scenario' + str(k))
                    _, expr2 = Complementary_equal(cons_expr2, self.model, 'dual_heat_loss_return' + str(t) + '_' + str(line) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for heater in range(self.heat_heater_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] - self.heater_tempe_supply_min[heater]
                    cons_expr2 = -1 * self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] + self.heater_tempe_supply_max[heater]
                    cons_expr3 = self.heat_node_tempe_return[self.heater_connection_index[heater], t, k] - self.heater_tempe_return_min[heater]
                    cons_expr4 = -1 * self.heat_node_tempe_return[self.heater_connection_index[heater], t, k] + self.heater_tempe_return_max[heater]
                    self.dual_heater_supply_min[heater, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_heater_supply_min' + str(t) + '_' + str(heater) + 'scenario' + str(k))
                    self.dual_heater_supply_max[heater, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_heater_supply_max' + str(t) + '_' + str(heater) + 'scenario' + str(k))
                    self.dual_heater_return_min[heater, t, k], expr3 = Complementary_great(cons_expr3, self.model, 'dual_heater_return_min' + str(t) + '_' + str(heater) + 'scenario' + str(k))
                    self.dual_heater_return_max[heater, t, k], expr4 = Complementary_great(cons_expr4, self.model, 'dual_heater_return_max' + str(t) + '_' + str(heater) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)
                    dual_expr.append(expr4)

        for exchanger in range(self.heat_exchanger_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] - self.exchanger_tempe_supply_min[exchanger]
                    cons_expr2 = -1 * self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] + self.exchanger_tempe_supply_max[exchanger]
                    cons_expr3 = self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k] - self.exchanger_tempe_return_min[exchanger]
                    cons_expr4 = -1 * self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k] + self.exchanger_tempe_return_max[exchanger]
                    self.dual_exchanger_supply_min[exchanger, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_exchanger_supply_min' + str(t) + '_' + str(exchanger) + 'scenario' + str(k))
                    self.dual_exchanger_supply_max[exchanger, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_exchanger_supply_max' + str(t) + '_' + str(exchanger) + 'scenario' + str(k))
                    self.dual_exchanger_return_min[exchanger, t, k], expr3 = Complementary_great(cons_expr3, self.model, 'dual_exchanger_return_min' + str(t) + '_' + str(exchanger) + 'scenario' + str(k))
                    self.dual_exchanger_return_max[exchanger, t, k], expr4 = Complementary_great(cons_expr4, self.model, 'dual_exchanger_return_max' + str(t) + '_' + str(exchanger) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)
                    dual_expr.append(expr4)
        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    # 构建 气网 部分
    def build_gas_system_original_and_dual_constrains(self):
        return

    # 每次迭代， 更新 PCCP 部分
    def update_gas_system_pccp_original_and_dual_constraints(self, pressure_end_old, flow_in_old, flow_out_old):
        return

    # 构建下层市场的目标函数，用于kkt求导的目标函数部分
    def build_lower_objective(self):
        lower_objs = []
        for chp in range(self.chp_upper_num):
            for time in range(T):
                for k in range(K):
                    # lower_objs.append(self.upper_chp_power_output[chp, time, k] * self.upper_chp_power_quoted_price[chp, time])
                    lower_objs.append(self.upper_chp_heat_output[chp, time, k] * self.upper_chp_heat_quoted_price[chp, time])
        for chp in range(self.chp_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, time, k] )

        self.lower_objective = sum(lower_objs)

    # KKT 等价中的 求导部分
    def build_kkt_derivative_constraints(self, penalty):
        # 包含 下层目标函数 + lagrange 基本部分 + lagrange 增量部分 + P-CCP 罚项
        my_expr = MyExpr(self.lower_objective +
                         self.dual_expression_basic)
        # 对下层的 所有 原变量 求导， 注意要包含 pccp 项
        self.model.update()
        for var in self.all_lower_level_vars:
            expr = my_expr.getCoeff(var)
            my_expr.addConstr(expr, self.model, var.VarName)

    # 上层目标函数 报价 的约束
    def build_upper_constraints(self):
        for chp in range(self.chp_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_chp_heat_quoted_price_tuple_dict[chp, t],
                    rhs=self.upper_chp_heat_quoted_price_max[chp][t],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_chp_heat_quoted_price_max' + str(t) + 'chp_' + str(chp)
                )

    # 上层的目标函数， 这里 是 非线性的 直接 => 产量 * 边际价格 - 成本，    这里的一个问题是， chp的天然气 需要 按节点边际气价 付费吗？
    def build_upper_objective(self):
        obj_k = []
        for k in range(K):
            expected_cost = []
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    expected_cost.append(self.upper_chp_heat_output[chp, t, k] * self.dual_heater_balance[self.chp_upper_connection_heater_index[chp], t, k])
                    expected_cost.append(-1 * self.upper_chp_heat_output[chp, t, k] * self.chp_upper_coeff_h_1[chp])
            obj_k.append(-1 * sum(expected_cost))
        self.obj_k = obj_k

    # 上层的目标函数，这里是 kkt 等价  ，  有问题
    def build_upper_objective_(self):
        obj_k = []
        obj_k_p = []
        obj_k_h = []
        for k in range(K):
            objs_cost = []
            objs_revenue = []
            # 成本
            for gen in range(self.generator_upper_num):
                for t in range(T):
                    objs_cost.append(self.generator_upper_cost[gen] * self.upper_generator_power_output[gen, t, k])
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    objs_cost.append(self.chp_upper_coeff_const[chp])
                    objs_cost.append(self.chp_upper_coeff_p_1[chp] * self.upper_chp_power_output[chp, t, k])
                    objs_cost.append(self.chp_upper_coeff_p_2[chp] * self.upper_chp_power_output[chp, t, k] * self.upper_chp_power_output[chp, t, k])
                    objs_cost.append(self.chp_upper_coeff_h_1[chp] * self.upper_chp_heat_output[chp, t, k])
                    objs_cost.append(self.chp_upper_coeff_h_2[chp] * self.upper_chp_heat_output[chp, t, k] * self.upper_chp_heat_output[chp, t, k])
                    objs_cost.append(self.chp_upper_coeff_cross[chp] * self.upper_chp_heat_output[chp, t, k] * self.upper_chp_power_output[chp, t, k])
            for well in range(self.well_upper_num):
                for t in range(T):
                    objs_cost.append(self.well_upper_cost[well] * self.upper_gas_well_output[well, t, k])

            # 等价 收益
            # 下层成本 部分
            for gen in range(self.generator_lower_num):
                for t in range(T):
                    objs_revenue.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
            for chp in range(self.chp_lower_num):
                for t in range(T):
                    objs_revenue.append(self.chp_lower_coeff_const[chp])
                    objs_revenue.append(self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, t, k])
                    objs_revenue.append(self.chp_lower_coeff_p_2[chp] * self.lower_chp_power_output[chp, t, k] * self.lower_chp_power_output[chp, t, k])
                    objs_revenue.append(self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, t, k])
                    objs_revenue.append(self.chp_lower_coeff_h_2[chp] * self.lower_chp_heat_output[chp, t, k] * self.lower_chp_heat_output[chp, t, k])
                    objs_revenue.append(self.chp_lower_coeff_cross[chp] * self.lower_chp_heat_output[chp, t, k] * self.lower_chp_power_output[chp, t, k])
            for well in range(self.well_lower_num):
                for t in range(T):
                    objs_cost.append(self.well_lower_cost[well] * self.lower_gas_well_output[well, t, k])

            # 负荷部分
            for load in range(self.ele_load_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])
            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_exchanger_balance[exchanger, t, k] * self.heat_load[exchanger, t])
            for load in range(self.gas_load_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_node_gas_balance[self.gas_load_connection_index[load], t, k] * self.gas_load[load, t])

            # 对偶等价部分
            for gen in range(self.generator_lower_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
                    objs_revenue.append(self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])
                    objs_revenue.append(1 * self.dual_lower_generator_power_output_ramp_up[gen, t, k] * self.generator_lower_ramp_up[gen])
                    objs_revenue.append(1 * self.dual_lower_generator_power_output_ramp_down[gen, t, k] * self.generator_lower_ramp_down[gen])

            for line in range(self.ele_line_num):
                for t in range(T):
                    objs_revenue.append(self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
                    objs_revenue.append(self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])

            # wind output part
            for wind in range(self.wind_farm_num):
                for t in range(T):
                    objs_revenue.append(self.dual_node_power_balance[self.wind_connection_index[wind], t, k] * self.wind_output[wind, k, t])

            for node in range(self.ele_node_num):
                for t in range(T):
                    objs_revenue.append(-3 * self.dual_bus_angle_min[node, t, k] - 3 * self.dual_bus_angle_max[node, t, k])

            for chp in range(self.chp_lower_num):
                for t in range(T):
                    for point in range(self.chp_point_num):
                        objs_revenue.append(1 * self.dual_lower_chp_point_less_one[chp, point, t, k])
                    objs_revenue.append(-1 * self.dual_lower_chp_point_sum_one[chp, t, k])

            # TODO: change to minus - plus - minus - plus
            for heater in range(self.heat_heater_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_heater_supply_min[heater, t, k] * self.heater_tempe_supply_min[heater])
                    objs_revenue.append(1 * self.dual_heater_supply_max[heater, t, k] * self.heater_tempe_supply_max[heater])
                    objs_revenue.append(-1 * self.dual_heater_return_min[heater, t, k] * self.heater_tempe_return_min[heater])
                    objs_revenue.append(1 * self.dual_heater_return_max[heater, t, k] * self.heater_tempe_return_max[heater])

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_exchanger_supply_min[exchanger, t, k] * self.exchanger_tempe_supply_min[exchanger])
                    objs_revenue.append(1 * self.dual_exchanger_supply_max[exchanger, t, k] * self.exchanger_tempe_supply_max[exchanger])
                    objs_revenue.append(-1 * self.dual_exchanger_return_min[exchanger, t, k] * self.exchanger_tempe_return_min[exchanger])
                    objs_revenue.append(1 * self.dual_exchanger_return_max[exchanger, t, k] * self.exchanger_tempe_return_max[exchanger])

            for well in range(self.well_lower_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_well_lower_output_min[well, t, k] * self.well_lower_output_min[well])
                    objs_revenue.append(1 * self.dual_well_lower_output_max[well, t, k] * self.well_lower_output_max[well])

            # TODO: change to minus - plus
            for node in range(self.gas_node_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_gas_node_pressure_min[node, t, k] * self.gas_node_pressure_min[node])
                    objs_revenue.append(1 * self.dual_gas_node_pressure_max[node, t, k] * self.gas_node_pressure_max[node])

            for line in range(self.gas_line_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_gas_flow_in_min[line, t, k] * self.gas_flow_in_min[line])
                    objs_revenue.append(1 * self.dual_gas_flow_in_max[line, t, k] * self.gas_flow_in_max[line])
                    objs_revenue.append(-1 * self.dual_gas_flow_out_min[line, t, k] * self.gas_flow_out_min[line])
                    objs_revenue.append(1 * self.dual_gas_flow_out_max[line, t, k] * self.gas_flow_out_max[line])
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
        # self.model.setObjective((np.array(self.obj_k) + np.array(self.objection_aux_update)).dot(np.array(distribution)))
        self.model.optimize()

        # expected_cost = []
        # for chp in range(self.chp_upper_num):
        #     for t in range(T):
        #         for k in range(K):
        #             expected_cost.append(self.upper_chp_heat_output[chp, t, k] * self.dual_heater_balance[0, t, k])
        #             expected_cost.append(self.upper_chp_power_output[chp, t, k] * self.dual_node_power_balance[self.chp_upper_connection_power_index[chp], t, k])
        # for gen in range(self.generator_upper_num):
        #     for t in range(T):
        #         for k in range(K):
        #             expected_cost.append(self.upper_generator_power_output[gen, t, k] * self.dual_node_power_balance[self.generator_upper_connection_index[gen], t, k])
        #
        # self.expected_revenue = sum(expected_cost)

        weymouth_left = []
        weymouth_right = []
        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    weymouth_left.append(self.gas_weymouth[line] *
                                         ((self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] * self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] -
                                           self.gas_node_pressure[self.gas_pipe_end_node[line], t, k] * self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]).getValue()))
                    weymouth_right.append(((self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]) *
                                           (self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k])).getValue() / 4)


        value_generator_quoted_price = to_value(self.upper_chp_heat_quoted_price_tuple_dict)
        value_chp_power_quoted_price = to_value(self.upper_chp_heat_quoted_price_tuple_dict)
        value_chp_heat_quoted_price = to_value(self.upper_chp_heat_quoted_price_tuple_dict)

        obj_k = np.array([obj.getValue() * -1 for obj in self.obj_k])              # change to profile

        linearization_point = [
            to_value_np(self.gas_node_pressure[self.gas_pipe_start_node]),
            to_value_np(self.gas_node_pressure[self.gas_pipe_end_node]),
            to_value_np(self.gas_flow_in),
            to_value_np(self.gas_flow_out)]

        pccp = to_value_np(self.pccp_relax)

        return [value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price], \
               obj_k, \
               linearization_point, \
               pccp, \
               np.array(weymouth_left), \
               np.array(weymouth_right)


    def sss(self):
        objs_revenue = []
        for k in range(K):
            # power load output
            for load in range(self.ele_load_num):
                for t in range(T):
                    objs_revenue.append(1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])
            # wind output part
            for wind in range(self.wind_farm_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_node_power_balance[self.wind_connection_index[wind], t, k] * self.wind_output[wind, k, t])
            for line in range(self.ele_line_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
                    objs_revenue.append(-1 * self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])
            for gen in range(self.generator_upper_num):
                for t in range(T):
                    objs_revenue.append(1 * self.dual_upper_generator_power_output_min[gen, t, k] * self.generator_upper_min[gen])
                    objs_revenue.append(-1 * self.dual_upper_generator_power_output_max[gen, t, k] * self.generator_upper_max[gen])
            for gen in range(self.generator_lower_num):
                for t in range(T):
                    objs_revenue.append(1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
                    objs_revenue.append(-1 * self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])
            for chp in range(self.chp_lower_num):
                for t in range(T):
                    for point in range(self.chp_point_num):
                        objs_revenue.append(-1 * self.dual_lower_chp_point_less_one[chp, point, t, k])
                    objs_revenue.append(1 * self.dual_lower_chp_point_sum_one[chp, t, k])
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    for point in range(self.chp_point_num):
                        objs_revenue.append(-1 * self.dual_upper_chp_point_less_one[chp, point, t, k])
                    objs_revenue.append(1 * self.dual_upper_chp_point_sum_one[chp, t, k])
            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(1 * self.dual_exchanger_balance[exchanger, t, k] * self.heat_load[exchanger, t])
            for heater in range(self.heat_heater_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_heater_supply_min[heater, t, k] * self.heater_tempe_supply_min[heater])
                    objs_revenue.append(1 * self.dual_heater_supply_max[heater, t, k] * self.heater_tempe_supply_max[heater])
                    objs_revenue.append(-1 * self.dual_heater_return_min[heater, t, k] * self.heater_tempe_return_min[heater])
                    objs_revenue.append(1 * self.dual_heater_return_max[heater, t, k] * self.heater_tempe_return_max[heater])

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_exchanger_supply_min[exchanger, t, k] * self.exchanger_tempe_supply_min[exchanger])
                    objs_revenue.append(1 * self.dual_exchanger_supply_max[exchanger, t, k] * self.exchanger_tempe_supply_max[exchanger])
                    objs_revenue.append(-1 * self.dual_exchanger_return_min[exchanger, t, k] * self.exchanger_tempe_return_min[exchanger])
                    objs_revenue.append(1 * self.dual_exchanger_return_max[exchanger, t, k] * self.exchanger_tempe_return_max[exchanger])
        self.jl = sum(objs_revenue)
        expected_cost = []
        for chp in range(self.chp_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.upper_chp_heat_output[chp, t, k] * self.upper_chp_heat_quoted_price[chp, t])
                    expected_cost.append(self.upper_chp_power_output[chp, t, k] * self.upper_chp_power_quoted_price[chp, t])
        for gen in range(self.generator_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.upper_generator_power_output[gen, t, k] * self.upper_generator_quoted_price[gen, t])
        for chp in range(self.chp_lower_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(1 * self.chp_lower_coeff_const[chp])
                    expected_cost.append(1 * self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_p_2[chp] * self.lower_chp_power_output[chp, t, k] * self.lower_chp_power_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_h_2[chp] * self.lower_chp_heat_output[chp, t, k] * self.lower_chp_heat_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_cross[chp] * self.lower_chp_heat_output[chp, t, k] * self.lower_chp_power_output[chp, t, k])
        for gen in range(self.generator_lower_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
        self.jr = sum(expected_cost)
