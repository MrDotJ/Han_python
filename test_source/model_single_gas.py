from resource.utility import *
from resource.config3_with_gas import T, K
from math import sqrt


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system, gas_system):
        # ------------ Power System----------------
        self.ele_node_num = power_system['node_num']
        self.ele_line_num = power_system['line_num']
        self.ele_line_capacity = power_system['line_capacity']
        self.line_reactance = power_system['reactance']
        self.ele_line_start = power_system['line_start']
        self.ele_line_end = power_system['line_end']

        self.generator_upper_connection_index = power_system['upper_generator_connection_index']
        self.generator_upper_num = power_system['upper_generator_num']
        self.generator_upper_max = power_system['upper_generator_max']
        self.generator_upper_min = power_system['upper_generator_min']
        self.generator_upper_ramp_up = power_system['upper_generator_ramp_up']
        self.generator_upper_ramp_down = power_system['upper_generator_ramp_down']
        self.generator_upper_cost = power_system['upper_generator_cost']
        self.upper_generator_quoted_price_max = power_system['upper_generator_quoted_price_max']

        self.generator_lower_connection_index = power_system['lower_generator_connection_index']
        self.generator_lower_num = power_system['lower_generator_num']
        self.generator_lower_max = power_system['lower_generator_max']
        self.generator_lower_min = power_system['lower_generator_min']
        self.generator_lower_ramp_up = power_system['lower_generator_ramp_up']
        self.generator_lower_ramp_down = power_system['lower_generator_ramp_down']
        self.generator_lower_cost = power_system['lower_generator_cost']

        self.ele_load_num = power_system['load_num']
        self.ele_load_index = power_system['load_index']
        self.ele_load = power_system['load']

        self.wind_connection_index = power_system['wind_connection_index']
        self.wind_output = power_system['wind_output']
        self.wind_farm_num = power_system['wind_farm_num']

        # ------------ Heat System----------------
        self.heat_node_num = heat_system['node_num']
        self.heat_pipe_num = heat_system['pipe_num']
        self.heat_pipe_length = heat_system['heat_pipe_length']
        self.heat_pipe_start_node_supply = heat_system['heat_pipe_start_node_supply']
        self.heat_pipe_start_node_return = heat_system['heat_pipe_start_node_return']
        self.heat_pipe_end_node_supply = heat_system['heat_pipe_end_node_supply']
        self.heat_pipe_end_node_return = heat_system['heat_pipe_end_node_return']
        self.heat_pipe_water_flow = heat_system['line_water_flow']

        self.heat_heater_num = heat_system['heater_num']
        self.heat_exchanger_num = heat_system['exchanger_num']

        self.heater_connection_index = heat_system['heater_connection_index']  # same with supply and return
        self.exchanger_connection_index = heat_system['exchanger_connection_index']

        self.heater_tempe_supply_max = heat_system['heater_tempe_supply_max']
        self.heater_tempe_supply_min = heat_system['heater_tempe_supply_min']
        self.heater_tempe_return_max = heat_system['heater_tempe_return_max']
        self.heater_tempe_return_min = heat_system['heater_tempe_return_min']

        self.exchanger_tempe_supply_max = heat_system['exchanger_tempe_supply_max']
        self.exchanger_tempe_supply_min = heat_system['exchanger_tempe_supply_min']
        self.exchanger_tempe_return_max = heat_system['exchanger_tempe_return_max']
        self.exchanger_tempe_return_min = heat_system['exchanger_tempe_return_min']

        self.chp_upper_connection_power_index = heat_system['chp_upper_connection_power_index']
        self.chp_lower_connection_power_index = heat_system['chp_lower_connection_power_index']
        self.chp_upper_connection_gas_index = gas_system['chp_upper_connection_gas_index']
        self.chp_lower_connection_gas_index = gas_system['chp_lower_connection_gas_index']
        self.chp_upper_connection_heater_index = heat_system['upper_chp_connection_heater_index']
        self.chp_lower_connection_heater_index = heat_system['lower_chp_connection_heater_index']

        self.heat_load = heat_system['load']

        # -------------- chp system -------------
        self.chp_upper_num = chp_system['chp_upper_num']
        self.chp_lower_num = chp_system['chp_lower_num']
        self.chp_point_num = chp_system['chp_point_num']
        self.upper_chp_power_quoted_price_max = chp_system['upper_chp_power_quoted_price_max']
        self.upper_chp_heat_quoted_price_max = chp_system['upper_chp_heat_quoted_price_max']
        self.upper_chp_POWER = chp_system['upper_chp_POWER']
        self.upper_chp_HEAT = chp_system['upper_chp_HEAT']
        self.lower_chp_POWER = chp_system['lower_chp_POWER']
        self.lower_chp_HEAT = chp_system['lower_chp_HEAT']

        self.chp_upper_coeff_p_1 = chp_system['chp_upper_coeff_p_1']
        self.chp_upper_coeff_p_2 = chp_system['chp_upper_coeff_p_2']
        self.chp_upper_coeff_h_1 = chp_system['chp_upper_coeff_h_1']
        self.chp_upper_coeff_h_2 = chp_system['chp_upper_coeff_h_2']
        self.chp_upper_coeff_cross = chp_system['chp_upper_coeff_cross']
        self.chp_upper_coeff_const = chp_system['chp_upper_coeff_const']
        self.chp_lower_coeff_p_1 = chp_system['chp_lower_coeff_p_1']
        self.chp_lower_coeff_p_2 = chp_system['chp_lower_coeff_p_2']
        self.chp_lower_coeff_h_1 = chp_system['chp_lower_coeff_h_1']
        self.chp_lower_coeff_h_2 = chp_system['chp_lower_coeff_h_2']
        self.chp_lower_coeff_cross = chp_system['chp_lower_coeff_cross']
        self.chp_lower_coeff_const = chp_system['chp_lower_coeff_const']

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

        self.upper_generator_quoted_price = None
        self.upper_chp_power_quoted_price = None
        self.upper_chp_heat_quoted_price = None
        self.upper_well_quoted_price = None

        self.upper_generator_quoted_price_tuple_dict = None
        self.upper_chp_power_quoted_price_tuple_dict = None
        self.upper_chp_heat_quoted_price_tuple_dict = None
        self.upper_well_quoted_price_tuple_dict = None

        self.upper_generator_power_output = None
        self.lower_generator_power_output = None

        self.upper_chp_power_output = None
        self.lower_chp_power_output = None
        self.upper_chp_heat_output = None
        self.lower_chp_heat_output = None

        self.line_power_flow = None
        self.bus_angle = None
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
        self.heat_node_tempe_supply = None
        self.heat_node_tempe_return = None
        self.heat_pipe_start_tempe_supply = None
        self.heat_pipe_end_tempe_supply = None
        self.heat_pipe_start_tempe_return = None
        self.heat_pipe_end_tempe_return = None
        self.upper_chp_point = None
        self.lower_chp_point = None
        self.dual_expression = 0
        self.dual_expression_basic = 0
        self.dual_expression_additional = 0
        self.lower_objective = None
        self.upper_objective = None
        self.dual_node_power_balance = None
        self.dual_line_power_flow_great = None
        self.dual_line_power_flow_less = None
        self.dual_lower_generator_power_output_min = None
        self.dual_lower_generator_power_output_max = None
        self.dual_upper_generator_power_output_min = None
        self.dual_upper_generator_power_output_max = None
        self.dual_lower_generator_power_output_ramp_up = None
        self.dual_lower_generator_power_output_ramp_down = None
        self.dual_lower_chp_point_sum_one = None
        self.dual_lower_chp_power_output = None
        self.dual_lower_chp_heat_output = None
        self.dual_upper_chp_power_output = None
        self.dual_upper_chp_heat_output = None
        self.dual_upper_chp_point_sum_one = None
        self.dual_lower_chp_point_less_one = None
        self.dual_lower_chp_point_great_zero = None
        self.dual_upper_chp_point_less_one = None
        self.dual_upper_chp_point_great_zero = None
        self.dual_exchanger_balance = None
        self.dual_heater_supply_min = None
        self.dual_heater_supply_max = None
        self.dual_heater_return_min = None
        self.dual_heater_return_max = None
        self.dual_exchanger_supply_min = None
        self.dual_exchanger_supply_max = None
        self.dual_exchanger_return_min = None
        self.dual_exchanger_return_max = None
        self.dual_heater_balance = None
        self.dual_bus_angle_min = None
        self.dual_bus_angle_max = None
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
        self.dual_weymouth_relax_left_right = None

        self.all_lower_level_vars = []
        self.obj_k = []
        self.do_nothing = 0
        self.equivalent_cost = 0
        self.equivalent_revenue = 0
        self.old_vars_constraints = []

    def build_power_system(self):
        self.upper_generator_quoted_price_tuple_dict = self.model.addVars(self.generator_upper_num, T, lb=0,
                                                                          name='upper_generator_quoted_price')
        self.upper_chp_power_quoted_price_tuple_dict = self.model.addVars(self.chp_upper_num, T, lb=0,
                                                                          name='upper_chp_power_quoted_price')
        self.upper_generator_quoted_price = tonp(self.upper_generator_quoted_price_tuple_dict)
        self.upper_chp_power_quoted_price = tonp(self.upper_chp_power_quoted_price_tuple_dict)

        self.upper_generator_power_output = tonp(
            self.model.addVars(self.generator_upper_num, T, K, name='upper_generator_power'))
        self.lower_generator_power_output = tonp(
            self.model.addVars(self.generator_lower_num, T, K, name='lower_generator_power'))
        self.line_power_flow = tonp(
            self.model.addVars(self.ele_line_num, T, K, lb=-1 * INFINITY, ub=INFINITY, name='line_power_flow'))
        self.bus_angle = tonp(
            self.model.addVars(self.ele_node_num, T, K, lb=-1 * INFINITY, ub=INFINITY, name='bus_angle'))

        self.dual_node_power_balance = np.empty((self.ele_node_num, T, K,), dtype=object)
        self.dual_line_power_flow_great = np.empty((self.ele_line_num, T, K,), dtype=object)
        self.dual_line_power_flow_less = np.empty((self.ele_line_num, T, K,), dtype=object)
        self.dual_lower_generator_power_output_min = np.empty((self.generator_lower_num, T, K,), dtype=object)
        self.dual_lower_generator_power_output_max = np.empty((self.generator_lower_num, T, K,), dtype=object)
        self.dual_upper_generator_power_output_min = np.empty((self.generator_upper_num, T, K,), dtype=object)
        self.dual_upper_generator_power_output_max = np.empty((self.generator_upper_num, T, K,), dtype=object)
        self.dual_lower_generator_power_output_ramp_up = np.empty((self.generator_lower_num, T, K,), dtype=object)
        self.dual_lower_generator_power_output_ramp_down = np.empty((self.generator_lower_num, T, K,), dtype=object)
        self.dual_bus_angle_min = np.empty((self.ele_node_num, T, K,), dtype=object)
        self.dual_bus_angle_max = np.empty((self.ele_node_num, T, K,), dtype=object)

        self.all_lower_level_vars.extend(self.upper_generator_power_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_generator_power_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.line_power_flow.flatten().tolist())
        self.all_lower_level_vars.extend(self.bus_angle.flatten().tolist())
    def build_gas_system(self):
        self.upper_well_quoted_price_tuple_dict = self.model.addVars(self.well_upper_num, T,
                                                                     name='upper_gas_quoted_price')
        self.upper_well_quoted_price = tonp(self.upper_well_quoted_price_tuple_dict)

        self.upper_gas_well_output = tonp(self.model.addVars(self.well_upper_num, T, K, name='upper_well_output'))
        self.lower_gas_well_output = tonp(self.model.addVars(self.well_lower_num, T, K, name='lower_well_output'))
        self.gas_node_pressure = tonp(self.model.addVars(self.gas_node_num, T, K, name='gas_node_pressure'))
        self.gas_flow_in = tonp(self.model.addVars(self.gas_line_num, T, K, name='gas_flow_in'))
        self.gas_flow_out = tonp(self.model.addVars(self.gas_line_num, T, K, name='gas_flow_out'))
        self.aux_weymouth_left = tonp(
            self.model.addVars(self.gas_line_num, T, K, name='weymouth_left_auxiliary', lb=-1 * INFINITY, ub=INFINITY))
        self.aux_weymouth_right_1 = tonp(
            self.model.addVars(self.gas_line_num, T, K, name='weymouth_right_auxiliary1', lb=-1 * INFINITY,
                               ub=INFINITY))
        self.aux_weymouth_right_2 = tonp(
            self.model.addVars(self.gas_line_num, T, K, name='weymouth_right_auxiliary2', lb=-1 * INFINITY,
                               ub=INFINITY))
        self.pccp_relax = tonp(self.model.addVars(self.gas_line_num, T, K, name='pccp_relax'))
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
        self.dual_weymouth_relax_left_right = np.empty((self.gas_line_num, T, K,), dtype=object)

        self.all_lower_level_vars.extend(self.upper_gas_well_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_gas_well_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_node_pressure.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_in.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_out.flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_linepack.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_left.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_right_1.flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_right_2.flatten().tolist())
        self.all_lower_level_vars.extend(self.pccp_relax          .flatten().tolist())
        self.do_nothing = 1
    def build_heat_system(self):
        self.upper_chp_heat_quoted_price_tuple_dict = self.model.addVars(self.chp_upper_num, T, lb=0,
                                                                         name='upper_chp_heat_quoted_price')
        self.upper_chp_heat_quoted_price = tonp(self.upper_chp_heat_quoted_price_tuple_dict)

        self.upper_chp_point = tonp(
            self.model.addVars(self.chp_upper_num, self.chp_point_num, T, K, name='upper_chp_point'))
        self.lower_chp_point = tonp(
            self.model.addVars(self.chp_lower_num, self.chp_point_num, T, K, name='lower_chp_point'))
        self.upper_chp_heat_output = tonp(self.model.addVars(self.chp_upper_num, T, K, name='upper_chp_heat_output'))
        self.upper_chp_power_output = tonp(self.model.addVars(self.chp_upper_num, T, K, name='upper_chp_power'))
        self.lower_chp_heat_output = tonp(self.model.addVars(self.chp_lower_num, T, K, name='lower_chp_heat_output'))
        self.lower_chp_power_output = tonp(self.model.addVars(self.chp_lower_num, T, K, name='lower_chp_power'))
        self.heat_node_tempe_supply = tonp(
            self.model.addVars(self.heat_node_num, T, K, name='heat_node_temperature_supply'))
        self.heat_node_tempe_return = tonp(
            self.model.addVars(self.heat_node_num, T, K, name='heat_node_temperature_return'))
        self.heat_pipe_start_tempe_supply = tonp(
            self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_start_temperature_supply_network'))
        self.heat_pipe_end_tempe_supply = tonp(
            self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_end_temperature_supply_network'))
        self.heat_pipe_start_tempe_return = tonp(
            self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_start_temperature_return_network'))
        self.heat_pipe_end_tempe_return = tonp(
            self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_end_temperature_return_network'))

        self.dual_lower_chp_point_sum_one = np.empty((self.chp_lower_num, T, K,), dtype=object)
        self.dual_lower_chp_power_output = np.empty((self.chp_lower_num, T, K,), dtype=object)
        self.dual_lower_chp_heat_output = np.empty((self.chp_lower_num, T, K,), dtype=object)
        self.dual_upper_chp_power_output = np.empty((self.chp_upper_num, T, K,), dtype=object)
        self.dual_upper_chp_heat_output = np.empty((self.chp_upper_num, T, K,), dtype=object)
        self.dual_upper_chp_point_sum_one = np.empty((self.chp_upper_num, T, K,), dtype=object)
        self.dual_lower_chp_point_less_one = np.empty((self.chp_lower_num, self.chp_point_num, T, K,), dtype=object)
        self.dual_lower_chp_point_great_zero = np.empty((self.chp_lower_num, self.chp_point_num, T, K,), dtype=object)
        self.dual_upper_chp_point_less_one = np.empty((self.chp_upper_num, self.chp_point_num, T, K,), dtype=object)
        self.dual_upper_chp_point_great_zero = np.empty((self.chp_upper_num, self.chp_point_num, T, K,), dtype=object)
        self.dual_exchanger_balance = np.empty((self.heat_exchanger_num, T, K,), dtype=object)
        self.dual_heater_supply_min = np.empty((self.heat_heater_num, T, K,), dtype=object)
        self.dual_heater_supply_max = np.empty((self.heat_heater_num, T, K,), dtype=object)
        self.dual_heater_return_min = np.empty((self.heat_heater_num, T, K,), dtype=object)
        self.dual_heater_return_max = np.empty((self.heat_heater_num, T, K,), dtype=object)
        self.dual_exchanger_supply_min = np.empty((self.heat_exchanger_num, T, K,), dtype=object)
        self.dual_exchanger_supply_max = np.empty((self.heat_exchanger_num, T, K,), dtype=object)
        self.dual_exchanger_return_min = np.empty((self.heat_exchanger_num, T, K,), dtype=object)
        self.dual_exchanger_return_max = np.empty((self.heat_exchanger_num, T, K,), dtype=object)
        self.dual_heater_balance = np.empty((self.heat_heater_num, T, K,), dtype=object)

        self.all_lower_level_vars.extend(self.upper_chp_point.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_chp_point.flatten().tolist())
        self.all_lower_level_vars.extend(self.upper_chp_heat_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.upper_chp_power_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_chp_heat_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_chp_power_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_node_tempe_supply.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_node_tempe_return.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_start_tempe_supply.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_end_tempe_supply.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_start_tempe_return.flatten().tolist())
        self.all_lower_level_vars.extend(self.heat_pipe_end_tempe_return.flatten().tolist())
    def build_power_system_original_and_dual_constraints(self):
        return
        self.model.update()
        dual_expr = []
        for node in range(self.ele_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(self.upper_generator_power_output[
                                np.where(self.generator_upper_connection_index == node), t, k].flatten()) + \
                        sum(self.lower_generator_power_output[
                                np.where(self.generator_lower_connection_index == node), t, k].flatten()) + \
                        sum(self.upper_chp_power_output[
                                np.where(self.chp_upper_connection_power_index == node), t, k].flatten()) + \
                        sum(self.wind_output[np.where(self.wind_connection_index == node), k, t].flatten()) + \
                        sum(self.lower_chp_power_output[
                                np.where(self.chp_lower_connection_power_index == node), t, k].flatten()) - \
                        sum(self.line_power_flow[np.where(self.ele_line_start == node), t, k].flatten()) + \
                        sum(self.line_power_flow[np.where(self.ele_line_end == node), t, k].flatten()) - \
                        sum(self.ele_load[np.where(self.ele_load_index == node), t].flatten())
                    self.dual_node_power_balance[node, t, k], expr1 = Complementary_equal(1 * cons_expr1, self.model,
                                                                                          'dual_node_power_balance_' + str(
                                                                                              t) + '_' + str(
                                                                                              node) + '_' + 'scenario' + str(
                                                                                              k))
                    dual_expr.append(expr1)

        for line in range(self.ele_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = (self.bus_angle[self.ele_line_start[line], t, k] -
                                  self.bus_angle[self.ele_line_end[line], t, k]) / self.line_reactance[line] - \
                                 self.line_power_flow[line, t, k]
                    _, expr1 = Complementary_equal(cons_expr1, self.model,
                                                   'dual_angle_line_' + str(t) + 'line' + str(line) + 'scenario' + str(
                                                       k))
                    dual_expr.append(expr1)
        for t in range(T):
            for k in range(K):
                cons_expr1 = self.bus_angle[2, t, k]
                _, expr1 = Complementary_equal(cons_expr1, self.model,
                                               'dual_reference_angle_' + str(t) + 'scenario' + str(k))
                dual_expr.append(expr1)

        for node in range(self.ele_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.bus_angle[node, t, k] + 3
                    cons_expr2 = 3 - self.bus_angle[node, t, k]
                    self.dual_bus_angle_min[node, t, k], expr1 = Complementary_great(cons_expr1, self.model,
                                                                                     'dual_angle_min' + str(node) + str(
                                                                                         t) + str(k))
                    self.dual_bus_angle_max[node, t, k], expr2 = Complementary_great(cons_expr2, self.model,
                                                                                     'dual_angle_max' + str(node) + str(
                                                                                         t) + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in range(self.ele_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.line_power_flow[line, t, k] + self.ele_line_capacity[line]
                    cons_expr2 = -1 * self.line_power_flow[line, t, k] + self.ele_line_capacity[line]
                    self.dual_line_power_flow_great[line, t, k], expr1 = Complementary_great(cons_expr1, self.model,
                                                                                             'dual_line_power_flow_great' + str(
                                                                                                 t) + '_' + str(
                                                                                                 line) + 'scenario' + str(
                                                                                                 k))
                    self.dual_line_power_flow_less[line, t, k], expr2 = Complementary_great(cons_expr2, self.model,
                                                                                            'dual_line_power_flow_less' + str(
                                                                                                t) + '_' + str(
                                                                                                line) + 'scenario' + str(
                                                                                                k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.upper_generator_power_output[gen, t, k] - self.generator_upper_min[gen]
                    cons_expr2 = -1 * self.upper_generator_power_output[gen, t, k] + self.generator_upper_max[gen]
                    self.dual_upper_generator_power_output_min[gen, t, k], expr1 = Complementary_great(cons_expr1,
                                                                                                       self.model,
                                                                                                       'dual_upper_generator_power_output_min' + str(
                                                                                                           t) + '_' + str(
                                                                                                           gen) + 'scenario' + str(
                                                                                                           k))
                    self.dual_upper_generator_power_output_max[gen, t, k], expr2 = Complementary_great(cons_expr2,
                                                                                                       self.model,
                                                                                                       'dual_upper_generator_power_output_max' + str(
                                                                                                           t) + '_' + str(
                                                                                                           gen) + 'scenario' + str(
                                                                                                           k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.lower_generator_power_output[gen, t, k] - self.generator_lower_min[gen]
                    cons_expr2 = -1 * self.lower_generator_power_output[gen, t, k] + self.generator_lower_max[gen]
                    self.dual_lower_generator_power_output_min[gen, t, k], expr1 = Complementary_great(cons_expr1,
                                                                                                       self.model,
                                                                                                       'dual_lower_generator_power_output_min' + str(
                                                                                                           t) + '_' + str(
                                                                                                           gen) + 'scenario' + str(
                                                                                                           k))
                    self.dual_lower_generator_power_output_max[gen, t, k], expr2 = Complementary_great(cons_expr2,
                                                                                                       self.model,
                                                                                                       'dual_lower_generator_power_output_max' + str(
                                                                                                           t) + '_' + str(
                                                                                                           gen) + 'scenario' + str(
                                                                                                           k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_upper_num):
            for t in range(T - 1):
                for k in range(K):
                    cons_expr1 = -1 * self.upper_generator_power_output[gen, t + 1, k] + \
                                 self.upper_generator_power_output[gen, t, k] + self.generator_upper_ramp_up[gen]
                    cons_expr2 = self.upper_generator_power_output[gen, t + 1, k] - self.upper_generator_power_output[
                        gen, t, k] + self.generator_upper_ramp_down[gen]
                    _, expr1 = Complementary_great(cons_expr1, self.model,
                                                   'dual_upper_generator_power_output_ramp_up' + str(t) + '_' + str(
                                                       gen) + 'scenario' + str(k))
                    _, expr2 = Complementary_great(cons_expr2, self.model,
                                                   'dual_lower_generator_power_output_ramp_down' + str(t) + '_' + str(
                                                       gen) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_lower_num):
            for t in range(T - 1):
                for k in range(K):
                    cons_expr1 = -1 * self.lower_generator_power_output[gen, t + 1, k] + \
                                 self.lower_generator_power_output[gen, t, k] + self.generator_lower_ramp_up[gen]
                    cons_expr2 = self.lower_generator_power_output[gen, t + 1, k] - self.lower_generator_power_output[
                        gen, t, k] + self.generator_lower_ramp_down[gen]
                    self.dual_lower_generator_power_output_ramp_up[gen, t, k], expr1 = Complementary_great(cons_expr1,
                                                                                                           self.model,
                                                                                                           'dual_lower_generator_power_output_ramp_up' + str(
                                                                                                               t) + '_' + str(
                                                                                                               gen) + 'scenario' + str(
                                                                                                               k))
                    self.dual_lower_generator_power_output_ramp_down[gen, t, k], expr2 = Complementary_great(cons_expr2,
                                                                                                             self.model,
                                                                                                             'dual_lower_generator_power_output_ramp_down' + str(
                                                                                                                 t) + '_' + str(
                                                                                                                 gen) + 'scenario' + str(
                                                                                                                 k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_upper_num):
            for t in [T - 1]:
                for k in range(K):
                    cons_expr1 = -1 * self.upper_generator_power_output[gen, 0, k] + self.upper_generator_power_output[
                        gen, t, k] + self.generator_upper_ramp_up[gen]
                    cons_expr2 = self.upper_generator_power_output[gen, 0, k] - self.upper_generator_power_output[
                        gen, t, k] + self.generator_upper_ramp_down[gen]
                    _, expr1 = Complementary_great(cons_expr1, self.model,
                                                   'dual_upper_generator_power_output_ramp_up' + str(t) + '_' + str(
                                                       gen) + 'scenario' + str(k))
                    _, expr2 = Complementary_great(cons_expr2, self.model,
                                                   'dual_lower_generator_power_output_ramp_down' + str(t) + '_' + str(
                                                       gen) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_lower_num):
            for t in [T - 1]:
                for k in range(K):
                    cons_expr1 = -1 * self.lower_generator_power_output[gen, 0, k] + self.lower_generator_power_output[
                        gen, t, k] + self.generator_lower_ramp_up[gen]
                    cons_expr2 = self.lower_generator_power_output[gen, 0, k] - self.lower_generator_power_output[
                        gen, t, k] + self.generator_lower_ramp_down[gen]
                    self.dual_lower_generator_power_output_ramp_up[gen, t, k], expr1 = Complementary_great(cons_expr1,
                                                                                                           self.model,
                                                                                                           'dual_lower_generator_power_output_ramp_up' + str(
                                                                                                               t) + '_' + str(
                                                                                                               gen) + 'scenario' + str(
                                                                                                               k))
                    self.dual_lower_generator_power_output_ramp_down[gen, t, k], expr2 = Complementary_great(cons_expr2,
                                                                                                             self.model,
                                                                                                             'dual_lower_generator_power_output_ramp_down' + str(
                                                                                                                 t) + '_' + str(
                                                                                                                 gen) + 'scenario' + str(
                                                                                                                 k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)
    def build_heat_system_original_and_dual_constraints(self):
        return
        dual_expr = []

        for chp in range(self.chp_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = ((self.upper_chp_point[chp, :, t, k].reshape((1, -1))).dot(
                        self.upper_chp_POWER[chp, :].reshape((-1, 1))))[0][0] - self.upper_chp_power_output[chp, t, k]
                    cons_expr2 = ((self.upper_chp_point[chp, :, t, k].reshape((1, -1))).dot(
                        self.upper_chp_HEAT[chp, :].reshape((-1, 1))))[0][0] - self.upper_chp_heat_output[chp, t, k]
                    cons_expr3 = sum(self.upper_chp_point[chp, :, t, k]) - 1
                    self.dual_upper_chp_power_output[chp, t, k], expr1 = Complementary_equal(-1 * cons_expr1,
                                                                                             self.model,
                                                                                             'dual_upper_chp_power_output_' + str(
                                                                                                 t) + '_' + str(
                                                                                                 chp) + 'scenario' + str(
                                                                                                 k))
                    self.dual_upper_chp_heat_output[chp, t, k], expr2 = Complementary_equal(-1 * cons_expr2, self.model,
                                                                                            'dual_upper_chp_heat_output_' + str(
                                                                                                t) + '_' + str(
                                                                                                chp) + 'scenario' + str(
                                                                                                k))
                    self.dual_upper_chp_point_sum_one[chp, t, k], expr3 = Complementary_equal(cons_expr3, self.model,
                                                                                              'dual_upper_chp_point_sum_one' + str(
                                                                                                  t) + '_' + str(
                                                                                                  chp) + 'scenario' + str(
                                                                                                  k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)
        for chp in range(self.chp_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = ((self.lower_chp_point[chp, :, t, k].reshape((1, -1))).dot(
                        self.lower_chp_POWER[chp, :].reshape((-1, 1))))[0][0] - self.lower_chp_power_output[chp, t, k]
                    cons_expr2 = ((self.lower_chp_point[chp, :, t, k].reshape((1, -1))).dot(
                        self.lower_chp_HEAT[chp, :].reshape((-1, 1))))[0][0] - self.lower_chp_heat_output[chp, t, k]
                    cons_expr3 = sum(self.lower_chp_point[chp, :, t, k]) - 1
                    self.dual_lower_chp_power_output[chp, t, k], expr1 = Complementary_equal(-1 * cons_expr1,
                                                                                             self.model,
                                                                                             'dual_lower_chp_power_output_' + str(
                                                                                                 t) + '_' + str(
                                                                                                 chp) + 'scenario' + str(
                                                                                                 k))
                    self.dual_lower_chp_heat_output[chp, t, k], expr2 = Complementary_equal(-1 * cons_expr2, self.model,
                                                                                            'dual_lower_chp_heat_output_' + str(
                                                                                                t) + '_' + str(
                                                                                                chp) + 'scenario' + str(
                                                                                                k))
                    self.dual_lower_chp_point_sum_one[chp, t, k], expr3 = Complementary_equal(cons_expr3, self.model,
                                                                                              'dual_lower_chp_point_sum_one' + str(
                                                                                                  t) + '_' + str(
                                                                                                  chp) + 'scenario' + str(
                                                                                                  k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)

        for chp in range(self.chp_upper_num):
            for point in range(self.chp_point_num):
                for t in range(T):
                    for k in range(K):
                        cons_expr1 = self.upper_chp_point[chp, point, t, k]
                        cons_expr2 = -1 * self.upper_chp_point[chp, point, t, k] + 1
                        self.dual_upper_chp_point_great_zero[chp, point, t, k], expr1 = Complementary_great(cons_expr1,
                                                                                                            self.model,
                                                                                                            'dual_upper_chp_point_great_zero' + str(
                                                                                                                t) + '_' + str(
                                                                                                                chp) + 'scenario' + str(
                                                                                                                k))
                        self.dual_upper_chp_point_less_one[chp, point, t, k], expr2 = Complementary_great(cons_expr2,
                                                                                                          self.model,
                                                                                                          'dual_upper_chp_point_less_one' + str(
                                                                                                              t) + '_' + str(
                                                                                                              chp) + 'scenario' + str(
                                                                                                              k))
                        dual_expr.append(expr1)
                        dual_expr.append(expr2)

        for chp in range(self.chp_lower_num):
            for point in range(self.chp_point_num):
                for t in range(T):
                    for k in range(K):
                        cons_expr1 = self.lower_chp_point[chp, point, t, k]
                        cons_expr2 = -1 * self.lower_chp_point[chp, point, t, k] + 1
                        self.dual_lower_chp_point_great_zero[chp, point, t, k], expr1 = Complementary_great(cons_expr1,
                                                                                                            self.model,
                                                                                                            'dual_lower_chp_point_great_zero' + str(
                                                                                                                t) + '_' + str(
                                                                                                                chp) + 'scenario' + str(
                                                                                                                k))
                        self.dual_lower_chp_point_less_one[chp, point, t, k], expr2 = Complementary_great(cons_expr2,
                                                                                                          self.model,
                                                                                                          'dual_lower_chp_point_less_one' + str(
                                                                                                              t) + '_' + str(
                                                                                                              chp) + 'scenario' + str(
                                                                                                              k))
                        dual_expr.append(expr1)
                        dual_expr.append(expr2)

        for heater in range(self.heat_heater_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(sum(self.upper_chp_heat_output[
                                    np.where(self.chp_upper_connection_heater_index == heater), t, k])) + \
                        sum(sum(self.lower_chp_heat_output[
                                    np.where(self.chp_lower_connection_heater_index == heater), t, k])) - \
                        0.1 * sum(self.heat_pipe_water_flow[np.where(
                            self.heat_pipe_start_node_supply == self.heater_connection_index[heater])]) * \
                        (self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] -
                         self.heat_node_tempe_return[self.heater_connection_index[heater], t, k])
                    self.dual_heater_balance[heater, t, k], expr1 = Complementary_equal(1 * cons_expr1, self.model,
                                                                                        'dual_heater_balance' + str(
                                                                                            t) + '_' + str(
                                                                                            heater) + 'scenario' + str(
                                                                                            k))
                    dual_expr.append(expr1)

        for exchanger in range(self.heat_exchanger_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_load[exchanger, t] - \
                                 0.1 * sum(self.heat_pipe_water_flow[np.where(
                        self.heat_pipe_end_node_supply == self.exchanger_connection_index[exchanger])]) * \
                                 (self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] -
                                  self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k])
                    self.dual_exchanger_balance[exchanger, t, k], expr1 = Complementary_equal(-1 * cons_expr1,
                                                                                              self.model,
                                                                                              'dual_exchanger_balance' + str(
                                                                                                  t) + '_' + str(
                                                                                                  exchanger) + str(k))
                    dual_expr.append(expr1)

        for line in range(self.heat_pipe_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_pipe_start_tempe_supply[line, t, k] - self.heat_node_tempe_supply[
                        self.heat_pipe_start_node_supply[line], t, k]
                    cons_expr2 = self.heat_pipe_start_tempe_return[line, t, k] - self.heat_node_tempe_return[
                        self.heat_pipe_start_node_return[line], t, k]
                    _, expr1 = Complementary_equal(-1 * cons_expr1, self.model,
                                                   'dual_line_temp_start_supply_' + str(t) + '_' + str(
                                                       line) + 'scenario' + str(k))
                    _, expr2 = Complementary_equal(-1 * cons_expr2, self.model,
                                                   'dual_line_temp_start_return' + str(t) + '_' + str(
                                                       line) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for node in range(self.heat_node_num):  # mix constrains
            for t in range(T):
                for k in range(K):
                    cons_expr1 = ((
                        self.heat_pipe_end_tempe_supply[np.where(self.heat_pipe_end_node_supply == node), t, k].reshape(
                            (1, -1))).dot(
                        (self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_supply == node)].reshape(
                            (-1, 1)))))[0][0] - \
                                 self.heat_node_tempe_supply[node, t, k] * \
                                 (sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_supply == node)]))
                    cons_expr2 = ((
                        self.heat_pipe_end_tempe_return[np.where(self.heat_pipe_end_node_return == node), t, k].reshape(
                            (1, -1))).dot(
                        (self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_return == node)].reshape(
                            (-1, 1)))))[0][0] - \
                                 self.heat_node_tempe_return[node, t, k] * \
                                 (sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_return == node)]))
                    _, expr1 = Complementary_equal(cons_expr1, self.model,
                                                   'dual_mix_constraints_supply' + str(t) + '_' + str(
                                                       node) + 'scenario' + str(k))
                    _, expr2 = Complementary_equal(cons_expr2, self.model,
                                                   'dual_mix_constraints_return' + str(t) + '_' + str(
                                                       node) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in range(self.heat_pipe_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_pipe_end_tempe_supply[line, t, k] - (
                                (1 - 0.0001 * (self.heat_pipe_length[line] * 1) / 1000) *
                                self.heat_pipe_start_tempe_supply[line, t, k])
                    cons_expr2 = self.heat_pipe_end_tempe_return[line, t, k] - (
                                (1 - 0.0001 * (self.heat_pipe_length[line] * 1) / 1000) *
                                self.heat_pipe_start_tempe_return[line, t, k])
                    _, expr1 = Complementary_equal(cons_expr1, self.model, 'dual_heat_loss_supply' + str(t) + '_' + str(
                        line) + 'scenario' + str(k))
                    _, expr2 = Complementary_equal(cons_expr2, self.model, 'dual_heat_loss_return' + str(t) + '_' + str(
                        line) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for heater in range(self.heat_heater_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] - \
                                 self.heater_tempe_supply_min[heater]
                    cons_expr2 = -1 * self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] + \
                                 self.heater_tempe_supply_max[heater]
                    cons_expr3 = self.heat_node_tempe_return[self.heater_connection_index[heater], t, k] - \
                                 self.heater_tempe_return_min[heater]
                    cons_expr4 = -1 * self.heat_node_tempe_return[self.heater_connection_index[heater], t, k] + \
                                 self.heater_tempe_return_max[heater]
                    self.dual_heater_supply_min[heater, t, k], expr1 = Complementary_great(cons_expr1, self.model,
                                                                                           'dual_heater_supply_min' + str(
                                                                                               t) + '_' + str(
                                                                                               heater) + 'scenario' + str(
                                                                                               k))
                    self.dual_heater_supply_max[heater, t, k], expr2 = Complementary_great(cons_expr2, self.model,
                                                                                           'dual_heater_supply_max' + str(
                                                                                               t) + '_' + str(
                                                                                               heater) + 'scenario' + str(
                                                                                               k))
                    self.dual_heater_return_min[heater, t, k], expr3 = Complementary_great(cons_expr3, self.model,
                                                                                           'dual_heater_return_min' + str(
                                                                                               t) + '_' + str(
                                                                                               heater) + 'scenario' + str(
                                                                                               k))
                    self.dual_heater_return_max[heater, t, k], expr4 = Complementary_great(cons_expr4, self.model,
                                                                                           'dual_heater_return_max' + str(
                                                                                               t) + '_' + str(
                                                                                               heater) + 'scenario' + str(
                                                                                               k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)
                    dual_expr.append(expr4)

        for exchanger in range(self.heat_exchanger_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] - \
                                 self.exchanger_tempe_supply_min[exchanger]
                    cons_expr2 = -1 * self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] + \
                                 self.exchanger_tempe_supply_max[exchanger]
                    cons_expr3 = self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k] - \
                                 self.exchanger_tempe_return_min[exchanger]
                    cons_expr4 = -1 * self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k] + \
                                 self.exchanger_tempe_return_max[exchanger]
                    self.dual_exchanger_supply_min[exchanger, t, k], expr1 = Complementary_great(cons_expr1, self.model,
                                                                                                 'dual_exchanger_supply_min' + str(
                                                                                                     t) + '_' + str(
                                                                                                     exchanger) + 'scenario' + str(
                                                                                                     k))
                    self.dual_exchanger_supply_max[exchanger, t, k], expr2 = Complementary_great(cons_expr2, self.model,
                                                                                                 'dual_exchanger_supply_max' + str(
                                                                                                     t) + '_' + str(
                                                                                                     exchanger) + 'scenario' + str(
                                                                                                     k))
                    self.dual_exchanger_return_min[exchanger, t, k], expr3 = Complementary_great(cons_expr3, self.model,
                                                                                                 'dual_exchanger_return_min' + str(
                                                                                                     t) + '_' + str(
                                                                                                     exchanger) + 'scenario' + str(
                                                                                                     k))
                    self.dual_exchanger_return_max[exchanger, t, k], expr4 = Complementary_great(cons_expr4, self.model,
                                                                                                 'dual_exchanger_return_max' + str(
                                                                                                     t) + '_' + str(
                                                                                                     exchanger) + 'scenario' + str(
                                                                                                     k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)
                    dual_expr.append(expr3)
                    dual_expr.append(expr4)
        self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)
    def build_gas_system_original_and_dual_constrains(self):
        dual_expr = []

        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(self.upper_gas_well_output[
                                np.where(self.well_upper_connection_index == node), t, k].flatten()) + \
                        sum(self.lower_gas_well_output[
                                np.where(self.well_lower_connection_index == node), t, k].flatten()) + \
                        sum(self.gas_flow_out[np.where(self.gas_pipe_end_node == node), t, k].flatten()) - \
                        sum(self.gas_flow_in[np.where(self.gas_pipe_start_node == node), t, k].flatten()) - \
                        sum(self.gas_load[np.where(self.gas_load_connection_index == node), t].flatten())# - \
                        # sum((self.upper_chp_power_output[np.where(self.chp_upper_connection_gas_index == node), t, k] *
                        #      self.chp_upper_coeff_p_1[
                        #          np.where(self.chp_upper_connection_gas_index == node)]).flatten()) + \
                        # sum((self.upper_chp_heat_output[np.where(self.chp_upper_connection_gas_index == node), t, k] *
                        #      self.chp_upper_coeff_h_1[
                        #          np.where(self.chp_upper_connection_gas_index == node)]).flatten()) - \
                        # sum((self.lower_chp_power_output[np.where(self.chp_lower_connection_gas_index == node), t, k] *
                        #      self.chp_lower_coeff_p_1[
                        #          np.where(self.chp_lower_connection_gas_index == node)]).flatten()) + \
                        # sum((self.lower_chp_heat_output[np.where(self.chp_lower_connection_gas_index == node), t, k] *
                        #      self.chp_lower_coeff_h_1[np.where(self.chp_lower_connection_gas_index == node)]).flatten())
                    self.dual_node_gas_balance[node, t, k], expr1 = \
                        Complementary_equal(cons_expr1, self.model, 'dual_node_gas_balance_time_' +
                                            str(t) + '_node_' + str(node) + 'scenario_' + str(k))
                    dual_expr.append(expr1)

        for line in self.gas_inactive_line:
            for t in range(0, T - 1):
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] +
                            self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, t + 1, k] - self.gas_linepack[line, t, k] - \
                                 self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_linepack_with_pressure[line, t, k], expr1 = \
                        Complementary_equal(cons_expr1, self.model, 'dual_gas_linepack_equation_line_' +
                                            str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_linepack_with_time[line, t, k], expr2 = \
                        Complementary_equal(cons_expr2, self.model, 'dual_gas_linepack_with_time_line_' +
                                            str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in self.gas_inactive_line:
            for t in [T - 1]:
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] +
                            self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, 0, k] - self.gas_linepack[line, t, k] - \
                                 self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_linepack_with_pressure[line, t, k], expr1 = \
                        Complementary_equal(cons_expr1, self.model,'dual_gas_linepack_equation_line_' +
                                            str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_linepack_with_pressure[line, t, k], expr2 = \
                        Complementary_equal(cons_expr2, self.model, 'dual_gas_linepack_with_time_line_' +
                                            str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in self.gas_active_line:
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_out[line, t, k] - 0.97 * self.gas_flow_in[line, t, k]
                    self.dual_compressor_consume[line, t, k], expr1 = \
                        Complementary_equal(cons_expr1, self.model,'dual_gas_flow_active_line_' +
                                            str(line) + '_time_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for compressor, line in enumerate(self.gas_active_line):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_compressor_coeff[compressor] * self.gas_node_pressure[
                        self.gas_pipe_start_node[line], t, k] - \
                                 self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]
                    self.dual_compressor_pressure_up[compressor, t, k], expr1 = \
                        Complementary_great(cons_expr1, self.model, 'dual_compressor_pressure_' +
                                            str(compressor) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for well in range(self.well_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.upper_gas_well_output[well, t, k] - self.well_upper_output_min[well]
                    cons_expr2 = -1 * self.upper_gas_well_output[well, t, k] + self.well_upper_output_max[well]
                    self.dual_well_upper_output_min[well, t, k], expr1 = \
                        Complementary_great(cons_expr1, self.model,'dual_upper_well_output_min_' +
                                            str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_well_upper_output_max[well, t, k], expr2 = \
                        Complementary_great(cons_expr2, self.model, 'dual_upper_well_output_max_' +
                                            str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for well in range(self.well_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.lower_gas_well_output[well, t, k] - self.well_lower_output_min[well]
                    cons_expr2 = -1 * self.lower_gas_well_output[well, t, k] + self.well_lower_output_max[well]
                    self.dual_well_lower_output_min[well, t, k], expr1 = \
                        Complementary_great(cons_expr1, self.model, 'dual_lower_well_output_min_' +
                                            str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_well_lower_output_max[well, t, k], expr2 = \
                        Complementary_great(cons_expr2, self.model, 'dual_lower_well_output_max_' +
                                            str(well) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_node_pressure[node, t, k] - self.gas_node_pressure_min[node]
                    cons_expr2 = self.gas_node_pressure_max[node] - self.gas_node_pressure[node, t, k]
                    self.dual_gas_node_pressure_min[node, t, k], expr1 = \
                        Complementary_great(cons_expr1, self.model, 'dual_node_pressure_min_' +
                                            str(node) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_gas_node_pressure_max[node, t, k], expr2 = \
                        Complementary_great(cons_expr2, self.model, 'dual_node_pressure_max_' +
                                            str(node) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_gas_flow_in_and_out_great_zero[line, t, k], expr1 = \
                        Complementary_great(cons_expr1,self.model,'dual_gas_flow_great_zero_' +
                                            str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_expr.append(expr1)

        for line in self.gas_inactive_line:
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.aux_weymouth_left[line, t, k] - (
                                self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]) / 2
                    self.dual_weymouth_aux_left[line, t, k], expr1 = \
                        Complementary_equal(cons_expr1, self.model,'weymouth_relax_left_auxiliary_' +
                                            str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    self.dual_weymouth_relax_left_left[line, t, k], \
                    self.dual_weymouth_relax_left_right[line, t, k], \
                    expr2 = \
                        Complementary_soc(
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
                    k3 = (flow_in_old[line, t, k] + flow_out_old[line, t, k]) ** 2 / 4
                    k4 = self.gas_weymouth[line] * pressure_end_old[self.gas_pipe_end_node[line], t, k] * \
                         pressure_end_old[self.gas_pipe_end_node[line], t, k]
                    k5 = 2 * self.gas_weymouth[line] * pressure_end_old[self.gas_pipe_end_node[line], t, k]
                    q = np.array([0, -1 * k2 / 2, -1 * k2 / 2, -k5, -1])
                    r = np.array([-1 * k3 - k4])
                    d = sqrt(k1) / 2
                    x = np.array([self.gas_node_pressure[self.gas_pipe_start_node[line], t, k],
                                  self.gas_flow_in[line, t, k],
                                  self.gas_flow_out[line, t, k],
                                  self.gas_node_pressure[self.gas_pipe_end_node[line], t, k],
                                  self.pccp_relax[line, t, k]
                                  ])
                    cons_expr1 = self.aux_weymouth_right_1[line, t, k] - sum(q * x) - r - 1
                    cons_expr2 = self.aux_weymouth_right_2[line, t, k] - sum(q * x) - r + 1
                    dual_vars1, constr1, expr1 = \
                        Complementary_equal_plus(cons_expr1, self.model, 'weymouth_relax_right_auxiliary1_' +
                                                 str(line) + '_t_' + str(t) + '_scenario_' + str(k))
                    dual_vars2, constr2, expr2 = \
                        Complementary_equal_plus(cons_expr2, self.model, 'weymouth_relax_right_auxiliary2_' +
                                                 str(line) + '_t_' + str(t) + '_scenario_' + str(k))
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
        self.dual_expression_additional = sum(dual_expr)
        self.model.update()

    def build_lower_objective(self):
        lower_objs = []
        '''''''''''
        for gen in range(self.generator_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.upper_generator_quoted_price[gen, time] * self.upper_generator_power_output[gen, time, k])
        for gen in range(self.generator_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, time, k])
        for chp in range(self.chp_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.upper_chp_power_output[chp, time, k] * self.upper_chp_power_quoted_price[chp, time])
                    lower_objs.append(
                        self.upper_chp_heat_output[chp, time, k] * self.upper_chp_heat_quoted_price[chp, time])
        for chp in range(self.chp_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.chp_lower_coeff_const[chp] +
                        self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, time, k] +
                        self.chp_lower_coeff_p_2[chp] * self.lower_chp_power_output[chp, time, k] *
                        self.lower_chp_power_output[chp, time, k] +
                        self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, time, k] +
                        self.chp_lower_coeff_h_2[chp] * self.lower_chp_heat_output[chp, time, k] *
                        self.lower_chp_heat_output[chp, time, k] +
                        self.chp_lower_coeff_cross[chp] * self.lower_chp_power_output[chp, time, k] *
                        self.lower_chp_heat_output[chp, time, k])
        '''
        for well in range(self.well_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.upper_well_quoted_price[well, time] * self.upper_gas_well_output[well, time, k])

        for well in range(self.well_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.well_lower_output_price[well] * self.lower_gas_well_output[well, time, k])

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
        for gen in range(self.generator_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_generator_quoted_price_tuple_dict[gen, t],
                    rhs=self.upper_generator_quoted_price_max[gen][t],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_generator_quoted_price_max_time' + str(t) + 'gen_' + str(gen))

        for chp in range(self.chp_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_chp_power_quoted_price_tuple_dict[chp, t],
                    rhs=self.upper_chp_power_quoted_price_max[chp][t],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_chp_power_quoted_price_max' + str(t) + 'chp_' + str(chp)
                )

        for chp in range(self.chp_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_chp_heat_quoted_price_tuple_dict[chp, t],
                    rhs=self.upper_chp_heat_quoted_price_max[chp][t],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_chp_heat_quoted_price_max' + str(t) + 'chp_' + str(chp)
                )

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
            """""""""
            for gen in range(self.generator_upper_num):  # generator  成本
                for t in range(T):
                    objs_cost.append(self.generator_upper_cost[gen] * self.upper_generator_power_output[gen, t, k])

            for gen in range(self.generator_lower_num):
                for t in range(T):
                    objs_revenue.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
                    objs_revenue.append(
                        -1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
                    objs_revenue.append(
                        self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])
                    objs_revenue.append(
                        1 * self.dual_lower_generator_power_output_ramp_up[gen, t, k] * self.generator_lower_ramp_up[
                            gen])
                    objs_revenue.append(1 * self.dual_lower_generator_power_output_ramp_down[gen, t, k] *
                                        self.generator_lower_ramp_down[gen])

            for line in range(self.ele_line_num):
                for t in range(T):
                    objs_revenue.append(self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
                    objs_revenue.append(self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])

            # power load part
            for load in range(self.ele_load_num):
                for t in range(T):
                    objs_revenue.append(
                        -1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])

            # wind output part
            for wind in range(self.wind_farm_num):
                for t in range(T):
                    objs_revenue.append(
                        self.dual_node_power_balance[self.wind_connection_index[wind], t, k] * self.wind_output[
                            wind, k, t])

            for node in range(self.ele_node_num):
                for t in range(T):
                    objs_revenue.append(
                        -3 * self.dual_bus_angle_min[node, t, k] - 3 * self.dual_bus_angle_max[node, t, k])

            for chp in range(self.chp_upper_num):
                for t in range(T):
                    objs_cost.append(self.chp_upper_coeff_const[chp])
                    objs_cost.append(self.chp_upper_coeff_p_1[chp] * self.upper_chp_power_output[chp, t, k])
                    # objs_cost.append(self.chp_upper_coeff_p_2[chp] * self.upper_chp_power_output[chp, t, k] * self.upper_chp_power_output[chp, t, k])
                    objs_cost.append(self.chp_upper_coeff_h_1[chp] * self.upper_chp_heat_output[chp, t, k])
                    # objs_cost.append(self.chp_upper_coeff_h_2[chp] * self.upper_chp_heat_output[chp, t, k] * self.upper_chp_heat_output[chp, t, k])
                    # objs_cost.append(self.chp_upper_coeff_cross[chp] * self.upper_chp_heat_output[chp, t, k] * self.upper_chp_power_output[chp, t, k])

            for chp in range(self.chp_lower_num):
                for t in range(T):
                    objs_revenue.append(self.chp_lower_coeff_const[chp])
                    objs_revenue.append(self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, t, k])
                    # objs_revenue.append(self.chp_lower_coeff_p_2[chp] * self.lower_chp_power_output[chp, t, k] * self.lower_chp_power_output[chp, t, k])
                    objs_revenue.append(self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, t, k])
                    # objs_revenue.append(self.chp_lower_coeff_h_2[chp] * self.lower_chp_heat_output[chp, t, k] * self.lower_chp_heat_output[chp, t, k])
                    # objs_revenue.append(self.chp_lower_coeff_cross[chp] * self.lower_chp_heat_output[chp, t, k] * self.lower_chp_power_output[chp, t, k])

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(
                        -1 * self.dual_exchanger_balance[exchanger, t, k] * self.heat_load[exchanger, t])

            for chp in range(self.chp_lower_num):
                for t in range(T):
                    for point in range(self.chp_point_num):
                        objs_revenue.append(1 * self.dual_lower_chp_point_less_one[chp, point, t, k])
                    objs_revenue.append(-1 * self.dual_lower_chp_point_sum_one[chp, t, k])

            for heater in range(self.heat_heater_num):
                for t in range(T):
                    objs_revenue.append(
                        1 * self.dual_heater_supply_min[heater, t, k] * self.heater_tempe_supply_min[heater])
                    objs_revenue.append(
                        -1 * self.dual_heater_supply_max[heater, t, k] * self.heater_tempe_supply_max[heater])
                    objs_revenue.append(
                        1 * self.dual_heater_return_min[heater, t, k] * self.heater_tempe_return_min[heater])
                    objs_revenue.append(
                        -1 * self.dual_heater_return_max[heater, t, k] * self.heater_tempe_return_max[heater])

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(
                        1 * self.dual_exchanger_supply_min[exchanger, t, k] * self.exchanger_tempe_supply_min[
                            exchanger])
                    objs_revenue.append(
                        -1 * self.dual_exchanger_supply_max[exchanger, t, k] * self.exchanger_tempe_supply_max[
                            exchanger])
                    objs_revenue.append(
                        1 * self.dual_exchanger_return_min[exchanger, t, k] * self.exchanger_tempe_return_min[
                            exchanger])
                    objs_revenue.append(
                        -1 * self.dual_exchanger_return_max[exchanger, t, k] * self.exchanger_tempe_return_max[
                            exchanger])
            
            """""""""

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
        '''
        expected_cost = []
        for chp in range(self.chp_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.upper_chp_heat_output[chp, t, k] * self.dual_heater_balance[0, t, k])
                    expected_cost.append(self.upper_chp_power_output[chp, t, k] * self.dual_node_power_balance[
                        self.chp_upper_connection_power_index[chp], t, k])
        for gen in range(self.generator_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.upper_generator_power_output[gen, t, k] * self.dual_node_power_balance[
                        self.generator_upper_connection_index[gen], t, k])

        self.expected_revenue = sum(expected_cost)
        '''

        value_generator_quoted_price = to_value(self.upper_generator_quoted_price_tuple_dict)
        value_chp_power_quoted_price = to_value(self.upper_chp_power_quoted_price_tuple_dict)
        value_chp_heat_quoted_price = to_value(self.upper_chp_heat_quoted_price_tuple_dict)
        obj_k = np.array([obj.getValue() * -1 for obj in self.obj_k])  # change to profile
        return value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price, obj_k

    def sss(self):
        objs_revenue = []
        for k in range(K):
            # power load output
            for load in range(self.ele_load_num):
                for t in range(T):
                    objs_revenue.append(
                        1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])
            # wind output part
            for wind in range(self.wind_farm_num):
                for t in range(T):
                    objs_revenue.append(
                        -1 * self.dual_node_power_balance[self.wind_connection_index[wind], t, k] * self.wind_output[
                            wind, k, t])
            for line in range(self.ele_line_num):
                for t in range(T):
                    objs_revenue.append(-1 * self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
                    objs_revenue.append(-1 * self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])
            for gen in range(self.generator_upper_num):
                for t in range(T):
                    objs_revenue.append(
                        1 * self.dual_upper_generator_power_output_min[gen, t, k] * self.generator_upper_min[gen])
                    objs_revenue.append(
                        -1 * self.dual_upper_generator_power_output_max[gen, t, k] * self.generator_upper_max[gen])
            for gen in range(self.generator_lower_num):
                for t in range(T):
                    objs_revenue.append(
                        1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
                    objs_revenue.append(
                        -1 * self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])
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
                    objs_revenue.append(
                        -1 * self.dual_heater_supply_min[heater, t, k] * self.heater_tempe_supply_min[heater])
                    objs_revenue.append(
                        1 * self.dual_heater_supply_max[heater, t, k] * self.heater_tempe_supply_max[heater])
                    objs_revenue.append(
                        -1 * self.dual_heater_return_min[heater, t, k] * self.heater_tempe_return_min[heater])
                    objs_revenue.append(
                        1 * self.dual_heater_return_max[heater, t, k] * self.heater_tempe_return_max[heater])

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    objs_revenue.append(
                        -1 * self.dual_exchanger_supply_min[exchanger, t, k] * self.exchanger_tempe_supply_min[
                            exchanger])
                    objs_revenue.append(
                        1 * self.dual_exchanger_supply_max[exchanger, t, k] * self.exchanger_tempe_supply_max[
                            exchanger])
                    objs_revenue.append(
                        -1 * self.dual_exchanger_return_min[exchanger, t, k] * self.exchanger_tempe_return_min[
                            exchanger])
                    objs_revenue.append(
                        1 * self.dual_exchanger_return_max[exchanger, t, k] * self.exchanger_tempe_return_max[
                            exchanger])
        self.jl = sum(objs_revenue)
        expected_cost = []
        for chp in range(self.chp_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(
                        self.upper_chp_heat_output[chp, t, k] * self.upper_chp_heat_quoted_price[chp, t])
                    expected_cost.append(
                        self.upper_chp_power_output[chp, t, k] * self.upper_chp_power_quoted_price[chp, t])
        for gen in range(self.generator_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(
                        self.upper_generator_power_output[gen, t, k] * self.upper_generator_quoted_price[gen, t])
        for chp in range(self.chp_lower_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(1 * self.chp_lower_coeff_const[chp])
                    expected_cost.append(1 * self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_p_2[chp] * self.lower_chp_power_output[chp, t, k] *
                                         self.lower_chp_power_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_h_2[chp] * self.lower_chp_heat_output[chp, t, k] *
                                         self.lower_chp_heat_output[chp, t, k])
                    expected_cost.append(1 * self.chp_lower_coeff_cross[chp] * self.lower_chp_heat_output[chp, t, k] *
                                         self.lower_chp_power_output[chp, t, k])
        for gen in range(self.generator_lower_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
        self.jr = sum(expected_cost)
