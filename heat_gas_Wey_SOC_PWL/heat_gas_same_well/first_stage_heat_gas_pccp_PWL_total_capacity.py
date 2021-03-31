from resource.utility_soc_PWL import *
from resource.config4_with_gas import T, K
from math import sqrt


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system, gas_system):
        self.chp_lower_connection_well_index = gas_system['lower_chp_connection_well_index']
        self.chp_upper_connection_well_index = gas_system['upper_chp_connection_well_index']

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

        self.upper_chp_gas_quoted_price_tuple_dict          = None
        self.upper_chp_gas_quoted_price                     = None

        self.upper_generator_power_output                   = None
        self.lower_generator_power_output                   = None

        self.upper_chp_power_output                         = None
        self.lower_chp_power_output                         = None
        self.upper_chp_heat_output                          = None
        self.lower_chp_heat_output                          = None

        self.line_power_flow                                = None
        self.bus_angle                                      = None
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
        self.dual_node_power_balance                        = None
        self.dual_line_power_flow_great                     = None
        self.dual_line_power_flow_less                      = None
        self.dual_lower_generator_power_output_min          = None
        self.dual_lower_generator_power_output_max          = None
        self.dual_upper_generator_power_output_min          = None
        self.dual_upper_generator_power_output_max          = None
        self.dual_lower_generator_power_output_ramp_up      = None
        self.dual_lower_generator_power_output_ramp_down    = None
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
        self.dual_bus_angle_min                             = None
        self.dual_bus_angle_max                             = None
        self.dual_node_gas_balance                          = None
        self.dual_linepack_with_pressure                    = None
        self.dual_linepack_with_time                        = None
        self.dual_compressor_consume                        = None
        self.dual_compressor_pressure_up                    = None
        self.dual_well_upper_output_min                     = None
        self.dual_well_upper_output_max                     = None
        self.dual_well_lower_output_min                     = None
        self.dual_well_lower_output_max                     = None
        self.dual_gas_node_pressure_min                     = None
        self.dual_gas_node_pressure_max                     = None
        self.dual_gas_flow_in_and_out_great_zero            = None
        self.dual_weymouth_aux_left                         = None
        self.dual_weymouth_relax_left_left                  = None
        self.dual_weymouth_relax_left_right                 = None
        self.dual_gas_flow_in_min                           = None
        self.dual_gas_flow_in_max                           = None
        self.dual_gas_flow_out_min                          = None
        self.dual_gas_flow_out_max                          = None
        self.dual_pccp_relax_great_zero                     = None
        self.dual_well_upper_capacity                       = None

        self.all_lower_level_vars                           = []
        self.obj_k                                          = []
        self.do_nothing                                     = 0
        self.equivalent_cost                                = 0
        self.equivalent_revenue                             = 0
        self.old_vars_constraints                           = []
        self.objection_aux_update                           = []
        self.old_vars                                       = []
        self.old_constraints                                = []
        self.old_dual_obj                                   = []
        self.DE = [[] for i in range(K)]
        self.Dobj = [[] for i in range(K)]

    def build_power_system(self):
        return

    def build_gas_system(self):
        self.upper_well_quoted_price_tuple_dict   = \
            self.model.addVars(self.well_upper_num, T, name='upper_gas_quoted_price')
        self.upper_well_quoted_price              = tonp( self.upper_well_quoted_price_tuple_dict)

        self.upper_gas_well_output                = \
            tonp( self.model.addVars(self.well_upper_num,  T, K, name='upper_well_output',     lb=-1 * INF, ub=INF ) )
        self.lower_gas_well_output                = \
            tonp( self.model.addVars(self.well_lower_num,  T, K, name='lower_well_output',     lb=-1 * INF, ub=INF ) )
        self.gas_node_pressure                    = \
            tonp( self.model.addVars(self.gas_node_num,    T, K, name='gas_node_pressure',     lb=-1 * INF, ub=INF ) )
        self.gas_flow_in                          = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='gas_flow_in',           lb=-1 * INF, ub=INF ) )
        self.gas_flow_out                         = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='gas_flow_out',          lb=-1 * INF, ub=INF ) )
        self.aux_weymouth_left                    = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='weymouth_left_aux',     lb=-1 * INF, ub=INF ) )
        self.aux_weymouth_right_1                 = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='weymouth_right_aux1',   lb=-1 * INF, ub=INF ) )
        self.aux_weymouth_right_2                 = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='weymouth_right_aux2',   lb=-1 * INF, ub=INF ) )
        self.pccp_relax                           = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='pccp_relax',            lb=-1 * INF, ub=INF ) )
        self.gas_linepack                         = \
            tonp( self.model.addVars(self.gas_line_num,    T, K, name='gas_linepack',          lb=-1 * INF, ub=INF ) )

        self.dual_node_gas_balance                = np.empty((self.gas_node_num,           T, K, ), dtype=object)
        self.dual_linepack_with_pressure          = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_linepack_with_time              = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_compressor_consume              = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_compressor_pressure_up          = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_well_upper_output_min           = np.empty((self.well_upper_num,         T, K, ), dtype=object)
        self.dual_well_upper_output_max           = np.empty((self.well_upper_num,         T, K, ), dtype=object)
        self.dual_well_lower_output_min           = np.empty((self.well_lower_num,         T, K, ), dtype=object)
        self.dual_well_lower_output_max           = np.empty((self.well_lower_num,         T, K, ), dtype=object)
        self.dual_gas_node_pressure_min           = np.empty((self.gas_node_num,           T, K, ), dtype=object)
        self.dual_gas_node_pressure_max           = np.empty((self.gas_node_num,           T, K, ), dtype=object)
        self.dual_gas_flow_in_and_out_great_zero  = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_weymouth_aux_left               = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_weymouth_relax_left_left        = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_weymouth_relax_left_right       = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_gas_flow_in_min                 = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_gas_flow_in_max                 = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_gas_flow_out_min                = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_gas_flow_out_max                = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_pccp_relax_great_zero           = np.empty((self.gas_line_num,           T, K, ), dtype=object)
        self.dual_well_upper_capacity             = np.empty((self.well_upper_num,         T, K, ), dtype=object)


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
        self.upper_chp_heat_quoted_price_tuple_dict = \
            self.model.addVars(self.chp_upper_num, T, lb=0, name='upper_chp_heat_quoted_price')
        self.upper_chp_heat_quoted_price            = tonp( self.upper_chp_heat_quoted_price_tuple_dict )
        self.upper_chp_gas_quoted_price_tuple_dict  = \
            self.model.addVars(self.chp_upper_num, T, lb=0, name='upper_chp_gas_quoted_price')
        self.upper_chp_gas_quoted_price             = tonp( self.upper_chp_gas_quoted_price_tuple_dict )

        self.upper_chp_point                    = \
            tonp( self.model.addVars(self.chp_upper_num, self.chp_point_num, T, K, name='upper_chp_point',  lb=-1 * INF, ub=INF ) )
        self.lower_chp_point                    = \
            tonp( self.model.addVars(self.chp_lower_num, self.chp_point_num, T, K, name='lower_chp_point',  lb=-1 * INF, ub=INF ) )
        self.upper_chp_heat_output              = \
            tonp( self.model.addVars(self.chp_upper_num, T, K, name='upper_chp_heat_output',                lb=-1 * INF, ub=INF ) )
        self.lower_chp_heat_output              = \
            tonp( self.model.addVars(self.chp_lower_num, T, K, name='lower_chp_heat_output',                lb=-1 * INF, ub=INF ) )
        self.heat_node_tempe_supply             = \
            tonp( self.model.addVars(self.heat_node_num, T, K, name='heat_node_tempe_supply',               lb=-1 * INF, ub=INF ) )
        self.heat_node_tempe_return             = \
            tonp( self.model.addVars(self.heat_node_num, T, K, name='heat_node_tempe_return',               lb=-1 * INF, ub=INF ) )
        self.heat_pipe_start_tempe_supply       = \
            tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_start_tempe_supply_network', lb=-1 * INF, ub=INF ) )
        self.heat_pipe_end_tempe_supply         = \
            tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_end_tempe_supply_network',   lb=-1 * INF, ub=INF ) )
        self.heat_pipe_start_tempe_return       = \
            tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_start_tempe_return_network', lb=-1 * INF, ub=INF ) )
        self.heat_pipe_end_tempe_return         = \
            tonp( self.model.addVars(self.heat_pipe_num, T, K, name='heat_pipe_end_tempe_return_network',   lb=-1 * INF, ub=INF ) )

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

        for k in range(K):
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    cons_expr2 = ((self.upper_chp_point[chp, :, t, k].reshape((1, -1))).dot(
                        self.upper_chp_HEAT[chp, :].reshape((-1, 1))))[0][0] - self.upper_chp_heat_output[chp, t, k]
                    cons_expr3 = sum(self.upper_chp_point[chp, :, t, k]) - 1
                    self.dual_upper_chp_heat_output[chp, t, k] = Complementary_equal(
                        1 * cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'upper_chp_heat_output[' + str(chp) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_upper_chp_point_sum_one[chp, t, k] = Complementary_equal(
                        cons_expr3, self.model, self.DE[k], self.Dobj[k],
                        'upper_chp_point_sum_one[' + str(chp) + ',' + str(t) + ',' + str(k) + ']')

            for chp in range(self.chp_lower_num):
                for t in range(T):
                    cons_expr2 = ((self.lower_chp_point[chp, :, t, k].reshape((1, -1))).dot(
                        self.lower_chp_HEAT[chp, :]. reshape((-1, 1))))[0][0] - self.lower_chp_heat_output[chp, t, k]
                    cons_expr3 = sum(self.lower_chp_point[chp, :, t, k]) - 1
                    self.dual_lower_chp_heat_output[chp, t, k] = Complementary_equal(
                        1 * cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'lower_chp_heat_output[' + str(chp) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_lower_chp_point_sum_one[chp, t, k] = Complementary_equal(
                        cons_expr3, self.model, self.DE[k], self.Dobj[k],
                        'lower_chp_point_sum_one[' + str(chp) + ',' + str(t) + ',' + str(k) + ']')

            for chp in range(self.chp_upper_num):
                for p in range(self.chp_point_num):
                    for t in range(T):
                        cons_expr1 = self.upper_chp_point[chp, p, t, k]
                        cons_expr2 = -1 * self.upper_chp_point[chp, p, t, k] + 1
                        self.dual_upper_chp_point_great_zero[chp, p, t, k] = Complementary_great(
                            cons_expr1, self.model, self.DE[k], self.Dobj[k],
                            'upper_chp_point_great_zero[' + str(chp) + ',' + str(p) + ',' + str(t) + ',' + str(k) + ']')
                        self.dual_upper_chp_point_less_one[chp, p, t, k] = Complementary_great(
                            cons_expr2, self.model, self.DE[k], self.Dobj[k],
                            'upper_chp_point_less_one[' + str(chp) + ',' + str(p) + ',' + str(t) + ',' + str(k) + ']')

            for chp in range(self.chp_lower_num):
                for p in range(self.chp_point_num):
                    for t in range(T):
                        cons_expr1 = self.lower_chp_point[chp, p, t, k]
                        cons_expr2 = -1 * self.lower_chp_point[chp, p, t, k] + 1
                        self.dual_lower_chp_point_great_zero[chp, p, t, k] = Complementary_great(
                            cons_expr1, self.model, self.DE[k], self.Dobj[k],
                            'lower_chp_point_great_zero[' + str(chp) + ',' + str(p) + ',' + str(t) + ',' + str(k) + ']')
                        self.dual_lower_chp_point_less_one[chp, p, t, k] = Complementary_great(
                            cons_expr2, self.model, self.DE[k], self.Dobj[k],
                            'lower_chp_point_less_one[' + str(chp) + ',' + str(p) + ',' + str(t) + ',' + str(k) + ']')

            for heater in range(self.heat_heater_num):
                for t in range(T):
                    cons_expr1 = \
                        sum(sum(self.upper_chp_heat_output[np.where(
                            self.chp_upper_connection_heater_index == heater), t, k] )) + \
                        sum(sum(self.lower_chp_heat_output[np.where(
                            self.chp_lower_connection_heater_index == heater), t, k] )) - \
                        0.1 * sum(self.heat_pipe_water_flow[np.where(
                            self.heat_pipe_start_node_supply == self.heater_connection_index[heater])]) * \
                        (self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] -
                         self.heat_node_tempe_return[self.heater_connection_index[heater], t, k])
                    self.dual_heater_balance[heater, t, k] = Complementary_equal(
                        1 * cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'heater_balance[' + str(heater) + str(t) + ',' + str(k) + ']')

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    cons_expr1 = self.heat_load[exchanger, t] - \
                                 0.1 * sum(self.heat_pipe_water_flow[np.where(
                        self.heat_pipe_end_node_supply == self.exchanger_connection_index[exchanger])]) * \
                                 (self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] -
                                  self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k])
                    self.dual_exchanger_balance[exchanger, t, k] = Complementary_equal(
                        1*cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'exchanger_balance[' + str(exchanger) + str(t) + ',' + str(k) + ']')

            for line in range(self.heat_pipe_num):
                for t in range(T):
                    cons_expr1 = self.heat_pipe_start_tempe_supply[line, t, k] - \
                                 self.heat_node_tempe_supply[self.heat_pipe_start_node_supply[line], t, k]
                    cons_expr2 = self.heat_pipe_start_tempe_return[line, t, k] - \
                                 self.heat_node_tempe_return[self.heat_pipe_start_node_return[line], t, k]
                    _ = Complementary_equal(
                        1 * cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'line_temp_start_supply[' + str(line) + str(t) + ',' + str(k) + ']')
                    _ = Complementary_equal(
                        1 * cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'line_temp_start_return[' + str(line) + str(t) + ',' + str(k) + ']')


            for node in range(self.heat_node_num):      # mix constrains
                for t in range(T):
                    cons_expr1 = ( (self.heat_pipe_end_tempe_supply[
                                        np.where(self.heat_pipe_end_node_supply == node), t, k].reshape((1, -1))).dot(
                        (self.heat_pipe_water_flow[
                             np.where(self.heat_pipe_end_node_supply == node)].reshape((-1, 1)))))[0][0] - \
                                 self.heat_node_tempe_supply[node, t, k] * \
                                 (sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_supply == node)]))
                    cons_expr2 = ( (self.heat_pipe_end_tempe_return[np.where(
                        self.heat_pipe_end_node_return == node), t, k].reshape((1, -1)) ).dot(
                        (self.heat_pipe_water_flow[np.where(
                            self.heat_pipe_end_node_return == node)].reshape((-1, 1)))) )[0][0] - \
                                 self.heat_node_tempe_return[node, t, k] * \
                                 (sum(self.heat_pipe_water_flow[np.where(self.heat_pipe_end_node_return == node)]))
                    _ = Complementary_equal(cons_expr1, self.model, self.DE[k], self.Dobj[k],
                                            'mix_constraints_supply[' + str(node) + str(t) + ',' + str(k) + ']')
                    _ = Complementary_equal(cons_expr2, self.model, self.DE[k], self.Dobj[k],
                                            'mix_constraints_return[' + str(node) + str(t) + ',' + str(k) + ']')

            for line in range(self.heat_pipe_num):
                for t in range(T):
                    cons_expr1 = self.heat_pipe_end_tempe_supply[line, t, k] - (
                            (1 - 0.000 * (self.heat_pipe_length[line] * 1) / 1000) *
                            self.heat_pipe_start_tempe_supply[line, t, k])
                    cons_expr2 = self.heat_pipe_end_tempe_return[line, t, k] - (
                            (1 - 0.000 * (self.heat_pipe_length[line] * 1) / 1000) *
                            self.heat_pipe_start_tempe_return[line, t, k])
                    _ = Complementary_equal(cons_expr1, self.model, self.DE[k], self.Dobj[k],
                                            'heat_loss_supply[' + str(line) + str(t) + ',' + str(k) + ']')
                    _ = Complementary_equal(cons_expr2, self.model, self.DE[k], self.Dobj[k],
                                            'heat_loss_return[' + str(line) + str(t) + ',' + str(k) + ']')

            for heater in range(self.heat_heater_num):
                for t in range(T):
                    cons_expr1 = self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] - \
                                 self.heater_tempe_supply_min[heater]
                    cons_expr2 = -1 * self.heat_node_tempe_supply[self.heater_connection_index[heater], t, k] + \
                                 self.heater_tempe_supply_max[heater]
                    cons_expr3 = self.heat_node_tempe_return[self.heater_connection_index[heater], t, k] - \
                                 self.heater_tempe_return_min[heater]
                    cons_expr4 = -1 * self.heat_node_tempe_return[self.heater_connection_index[heater], t, k] + \
                                 self.heater_tempe_return_max[heater]
                    self.dual_heater_supply_min[heater, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'heater_supply_min[' + str(heater) + str(t) + ',' + str(k) + ']')
                    self.dual_heater_supply_max[heater, t, k] = Complementary_great(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'heater_supply_max[' + str(heater) + str(t) + ',' + str(k) + ']')
                    self.dual_heater_return_min[heater, t, k] = Complementary_great(
                        cons_expr3, self.model, self.DE[k], self.Dobj[k],
                        'heater_return_min[' + str(heater) + str(t) + ',' + str(k) + ']')
                    self.dual_heater_return_max[heater, t, k] = Complementary_great(
                        cons_expr4, self.model, self.DE[k], self.Dobj[k],
                        'heater_return_max[' + str(heater) + str(t) + ',' + str(k) + ']')

            for exchanger in range(self.heat_exchanger_num):
                for t in range(T):
                    cons_expr1 = self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] - \
                                 self.exchanger_tempe_supply_min[exchanger]
                    cons_expr2 = -1 * self.heat_node_tempe_supply[self.exchanger_connection_index[exchanger], t, k] + \
                                 self.exchanger_tempe_supply_max[exchanger]
                    cons_expr3 = self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k] - \
                                 self.exchanger_tempe_return_min[exchanger]
                    cons_expr4 = -1 * self.heat_node_tempe_return[self.exchanger_connection_index[exchanger], t, k] + \
                                 self.exchanger_tempe_return_max[exchanger]
                    self.dual_exchanger_supply_min[exchanger, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'exchanger_supply_min[' + str(exchanger) + str(t) + ',' + str(k) + ']')
                    self.dual_exchanger_supply_max[exchanger, t, k] = Complementary_great(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'exchanger_supply_max[' + str(exchanger) + str(t) + ',' + str(k) + ']')
                    self.dual_exchanger_return_min[exchanger, t, k] = Complementary_great(
                        cons_expr3, self.model, self.DE[k], self.Dobj[k],
                        'exchanger_return_min[' + str(exchanger) + str(t) + ',' + str(k) + ']')
                    self.dual_exchanger_return_max[exchanger, t, k] = Complementary_great(
                        cons_expr4, self.model, self.DE[k], self.Dobj[k],
                        'exchanger_return_max[' + str(exchanger) + str(t) + ',' + str(k) + ']')

        # self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    # 构建 气网 部分
    def build_gas_system_original_and_dual_constrains(self):
        self.DAAA = sum(self.DE[0])
        dual_expr = []
        for k in range(K):
            for node in range(self.gas_node_num):
                for t in range(T):
                    cons_expr1 = \
                        sum(self.upper_gas_well_output[  np.where(self.well_upper_connection_index    == node), t, k].flatten()) +  \
                        sum(self.lower_gas_well_output[  np.where(self.well_lower_connection_index    == node), t, k].flatten()) +  \
                        sum(self.gas_flow_out[           np.where(self.gas_pipe_end_node              == node), t, k].flatten()) -  \
                        sum(self.gas_flow_in[            np.where(self.gas_pipe_start_node            == node), t, k].flatten()) -   \
                        sum(self.gas_load[               np.where(self.gas_load_connection_index      == node), t   ].flatten()) #-  \
                        # sum((self.upper_chp_heat_output[ np.where(self.chp_upper_connection_gas_index == node), t, k] *
                        #     self.chp_upper_coeff_h_1[    np.where(self.chp_upper_connection_gas_index == node)      ]).flatten()) - \
                        # sum((self.lower_chp_heat_output[ np.where(self.chp_lower_connection_gas_index == node), t, k] *
                        #     self.chp_lower_coeff_h_1[    np.where(self.chp_lower_connection_gas_index == node)      ]).flatten())
                    self.dual_node_gas_balance[node, t, k] = Complementary_equal(
                        1*cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'node_gas_balance[' + str(node) + ',' + str(t) + ',' + str(k) + ']')
                    # self.model.addConstr(self.dual_node_gas_balance[node, t, k] >= 0)
        self.D4 = sum(self.DE[0])
        for k in range(K):
            for well in range(self.well_upper_num):
                for t in range(T):
                    cons_expr1 = self.well_upper_output_max[well] - (self.upper_gas_well_output[well, t, k] +
                        sum((self.upper_chp_heat_output[  np.where(self.chp_upper_connection_well_index == well), t, k] *
                             self.chp_upper_coeff_h_1[    np.where(self.chp_upper_connection_well_index == well)]).flatten()) )#+
                        # sum((self.upper_chp_power_output[ np.where(self.chp_upper_connection_well_index == well), t, k] *
                        #      self.chp_upper_coeff_p_1[    np.where(self.chp_upper_connection_well_index == well)]).flatten()))
                    self.dual_well_upper_capacity[well, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'dual_upper_well_capacity_time_' + str(t) + '_well_' + str(well) + 'S_' + str(k))

            for well in range(self.well_lower_num):
                for t in range(T):
                    cons_expr1 = \
                        self.well_lower_output_max[well] - (self.lower_gas_well_output[well, t, k]  +
                        sum((self.lower_chp_heat_output[np.where(self.chp_lower_connection_well_index == well), t, k] *
                             self.chp_lower_coeff_h_1[ np.where(self.chp_lower_connection_well_index == well)]).flatten()) )# +
                        # sum((self.lower_chp_power_output[np.where(self.chp_lower_connection_well_index == well), t, k] *
                        #      self.chp_lower_coeff_p_1[np.where(self.chp_lower_connection_well_index == well)]).flatten()))
                    _ = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'dual_lower_well_capacity_time_' + str(t) + '_well_' + str(well) + '_S_' + str(k))
        self.D3 = sum(self.DE[0])
        for k in range(K):
            for line in self.gas_inactive_line:
                for t in range(0, T-1):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] +
                            self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, t+1, k] - self.gas_linepack[line, t, k] - \
                                 self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_linepack_with_pressure[line, t, k] = Complementary_equal(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'gas_linepack_equation[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_linepack_with_time[line, t, k] = Complementary_equal(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'gas_linepack_with_time[' + str(line) + ',' + str(t) + ',' + str(k) + ']')

            for line in self.gas_inactive_line:
                for t in [T-1]:
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] +
                            self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, 0, k] - self.gas_linepack[line, t, k] - \
                                 self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    self.dual_linepack_with_pressure[line, t, k] = Complementary_equal(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'gas_linepack_equation[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_linepack_with_time[line, t, k] = Complementary_equal(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'gas_linepack_with_time[' + str(line) + ',' + str(t) + ',' + str(k) + ']')

            # for line in self.gas_active_line:
            #     for t in range(T):
            #         cons_expr1 = self.gas_flow_out[line, t, k] - 0.97 * self.gas_flow_in[line, t, k]
            #         self.dual_compressor_consume[line, t, k], expr1 = \
            #             Complementary_equal(cons_expr1, self.model,
            #                                 'dual_gas_flow_active_' + str(line) + '_time_' + str(t) + '_S_' + str(k))
            #         dual_expr.append(expr1)
            #
            # for compressor, line in enumerate(self.gas_active_line):
            #     for t in range(T):
            #         cons_expr1 = self.gas_compressor_coeff[compressor] * \
            #                      self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] - \
            #                      self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]
            #         self.dual_compressor_pressure_up[compressor, t, k], expr1 = \
            #             Complementary_great(cons_expr1, self.model,
            #                                 'dual_com_pressure_' + str(compressor) + '_t_' + str(t) + '_S_' + str(k))
            #         dual_expr.append(expr1)
        self.D2 = sum(self.DE[0])
        for k in range(K):
            for well in range(self.well_upper_num):
                for t in range(T):
                    cons_expr1 = self.upper_gas_well_output[well, t, k] - self.well_upper_output_min[well]
                    cons_expr2 = -1 * self.upper_gas_well_output[well, t, k] + self.well_upper_output_max[well]
                    self.dual_well_upper_output_min[well, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'upper_well_output_min[' + str(well) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_well_upper_output_max[well, t, k] = Complementary_great(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'upper_well_output_max[' + str(well) + ',' + str(t) + ',' + str(k) + ']')

            for well in range(self.well_lower_num):
                for t in range(T):
                    cons_expr1 = self.lower_gas_well_output[well, t, k] - self.well_lower_output_min[well]
                    cons_expr2 = -1 * self.lower_gas_well_output[well, t, k] + self.well_lower_output_max[well]
                    self.dual_well_lower_output_min[well, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'lower_well_output_min[' + str(well) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_well_lower_output_max[well, t, k] = Complementary_great(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'lower_well_output_max[' + str(well) + ',' + str(t) + ',' + str(k) + ']')
        self.D1 = sum(self.DE[0])

        for k in range(K):
            for node in range(self.gas_node_num):
                for t in range(T):
                    cons_expr1 = self.gas_node_pressure[node, t, k] - self.gas_node_pressure_min[node]
                    cons_expr2 = self.gas_node_pressure_max[node] - self.gas_node_pressure[node, t, k]
                    self.dual_gas_node_pressure_min[node, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'node_pressure_min[' + str(node) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_gas_node_pressure_max[node, t, k] = Complementary_great(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'node_pressure_max[' + str(node) + ',' + str(t) + ',' + str(k) + ']')

            # for line in range(self.gas_line_num):
            #     for t in range(T):
            #         cons_expr1 = self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
            #         self.dual_gas_flow_in_and_out_great_zero[line, t, k], expr1 = \
            #             Complementary_great(cons_expr1, self.model,
            #                                 'dual_gas_flow_great_zero_' + str(line) + '_t_' + str(t) + '_S_' + str(k))
            #         dual_expr.append(expr1)
        self.D7 = sum(self.DE[0])
        for k in range(K):
            for line in range(self.gas_line_num):
                for t in range(T):
                    cons_expr1 = self.gas_flow_in[line, t, k] - self.gas_flow_in_min[line]
                    cons_expr2 = -1 * self.gas_flow_in[line, t, k] + self.gas_flow_in_max[line]
                    cons_expr3 = self.gas_flow_out[line, t, k] - self.gas_flow_out_min[line]
                    cons_expr4 = -1 * self.gas_flow_out[line, t, k] + self.gas_flow_out_max[line]
                    self.dual_gas_flow_in_min[line, t, k]  = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'gas_flow_in_min['  + str(line) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_gas_flow_in_max[line, t, k]  = Complementary_great(
                        cons_expr2, self.model, self.DE[k], self.Dobj[k],
                        'gas_flow_in_max['  + str(line) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_gas_flow_out_min[line, t, k] = Complementary_great(
                        cons_expr3, self.model, self.DE[k], self.Dobj[k],
                        'gas_flow_out_min[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
                    self.dual_gas_flow_out_max[line, t, k] = Complementary_great(
                        cons_expr4, self.model, self.DE[k], self.Dobj[k],
                        'gas_flow_out_max[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
            #
        self.D8 = sum(self.DE[0])
        for k in range(K):
            for line in range(self.gas_line_num):
                for t in range(T):
                    cons_expr1 = self.pccp_relax[line, t, k]
                    self.dual_pccp_relax_great_zero[line, t, k] = Complementary_great(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'pccp_relax_great_zero[' + str(line) + ',' + str(t) + ',' + str(k) + ']')


        self.mearsurement = []
        self.DBBB = sum(self.DE[0])
        for k in range(K):
            for line in self.gas_inactive_line:
                for t in range(T):
                    cons_expr1 = self.aux_weymouth_left[line, t, k] - \
                                 ((self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]) / 2)
                    self.dual_weymouth_aux_left[line, t, k] = Complementary_equal(
                        cons_expr1, self.model, self.DE[k], self.Dobj[k],
                        'weymouth_left_aux[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
        self.DCCC = sum(self.DE[0])
        for k in range(K):
            for line in self.gas_inactive_line:
                for t in range(T):
                    MM = 1e1
                    self.dual_weymouth_relax_left_left[line, t, k], self.dual_weymouth_relax_left_right[line, t, k], \
                    measurement = Complementary_soc(
                        [1, sqrt(self.gas_weymouth[line])],
                        [self.aux_weymouth_left[line, t, k], self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]],
                        [sqrt(self.gas_weymouth[line])],
                        [self.gas_node_pressure[self.gas_pipe_start_node[line], t, k]],
                        self.model, self.DE[k], self.Dobj[k],
                        'weymouth_left_soc[' + str(line) + ',' + str(t) + ',' + str(k) + ']',
                        [-200, -200, -200],
                        [200, 200, 200],
                        [-MM, -MM, -MM],
                        [MM, MM, MM]
                        )
                    self.mearsurement.append(measurement)
            # for line in self.gas_inactive_line:
            #     for t in range(T):
            #         cons_expr1 = self.gas_weymouth[line] * (
            #                 self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] -
            #                 self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]
            #         ) - (self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k])
            #         _ = Complementary_equal(cons_expr1, self.model, self.DE[k], self.Dobj[k],
            #                                 'dual_weymouth_simplify' + str(line) + str(t) + str(k))
        self.DDDD = sum(self.DE[0])
        # self.dual_expression_basic = self.dual_expression_basic + sum(dual_expr)

    # 每次迭代， 更新 PCCP 部分
    def update_gas_system_pccp_original_and_dual_constraints(self, pressure_end_old, flow_in_old, flow_out_old):
        # for k in range(K):
        #     self.Dobj[k].extend([self.old_dual_obj[i] * (-1) for i in range(len(self.old_dual_obj))])
        self.old_dual_obj = []

        self.model.remove(self.old_vars)
        self.model.remove(self.old_constraints)
        self.old_vars = []
        self.old_constraints = []

        for k in range(K):
            for line in self.gas_inactive_line:
                for t in range(T):
                    k1 = self.gas_weymouth[line]
                    k2 = flow_in_old[line, t, k] + flow_out_old[line, t, k]
                    k3 = (flow_in_old[line, t, k] + flow_out_old[line, t, k]) ** 2 / 4
                    k4 = self.gas_weymouth[line] * ((pressure_end_old[self.gas_pipe_end_node[line], t, k]) ** 2)
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

                    # 两个辅助 变量
                    cons_expr1 = self.aux_weymouth_right_1[line, t, k] - sum(q*x) - r - 1
                    cons_expr2 = self.aux_weymouth_right_2[line, t, k] - sum(q*x) - r + 1
                    dual_vars1, constr1, dual_obj1 = \
                        Complementary_equal_plus(cons_expr1, self.model, self.DE[k], self.Dobj[k],
                                                 'weymouth_right_aux1[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
                    dual_vars2, constr2, dual_obj2 = \
                        Complementary_equal_plus(cons_expr2, self.model, self.DE[k], self.Dobj[k],
                                                 'weymouth_right_aux2[' + str(line) + ',' + str(t) + ',' + str(k) + ']')
        self.D9 = sum(self.DE[0])

        for k in range(K):
            for line in self.gas_inactive_line:
                for t in range(T):
                    MM = 1e1
                    # 构建SOC 约束
                    # 左对偶变量, 右对偶变量,  原SOC约束,      对偶SOC约束,      互补为零约束,     lagrange项
                    dual_left, dual_right, constr_original, constr_dual, var_line, constrain_line, measurement = \
                        Complementary_soc_plus(
                        [2 * d, 1],
                        [self.gas_node_pressure[self.gas_pipe_start_node[line], t, k],
                         self.aux_weymouth_right_1[line, t, k]],
                        [1],
                        [self.aux_weymouth_right_2[line, t, k]],
                        self.model, self.DE[k], self.Dobj[k],
                        'weymouth_right_soc[' + str(line) + ',' + str(t) + ',' + str(k) + ']',
                        [-MM, -MM, -MM],
                        [MM, MM, MM],
                        [-MM, -MM, -MM],
                        [MM, MM, MM])
                    # 追加旧的变量及约束
                    self.old_vars.extend([dual_vars1, dual_vars2, dual_left, dual_right, var_line])
                    self.old_constraints.extend([constr1, constr2, constr_original, constr_dual, constrain_line])
                    self.old_dual_obj.extend([dual_obj1, dual_obj2])
                    self.mearsurement.append(measurement)
            # 用于 每次 更新 KKT 等价 部分

        self.model.update()
    # 构建下层市场的目标函数，用于kkt求导的目标函数部分
    def build_lower_objective(self):
        # 市场 ： 整个社会成本最小
        lower_objs = []
        # UPPER CHP 从上层买热 quoted price 买
        for chp in range(self.chp_upper_num):
            for time in range(T):
                for k in range(K):
                    # lower_objs.append(self.upper_chp_power_output[chp, time, k] * self.upper_chp_power_quoted_price[chp, time])
                    lower_objs.append(self.upper_chp_heat_output[chp, time, k] * self.upper_chp_heat_quoted_price[0, time])
                    # lower_objs.append(self.upper_chp_heat_output[chp, time, k] * self.dual)
        # UPPER CHP 的 买气 成本 ????? ！！！！！
        # for chp in range(self.chp_upper_num):
        #     for time in range(T):
        #         for k in range(K):
        #             lower_objs.append(-1 * (self.upper_chp_heat_output[chp, time, k] * self.chp_upper_coeff_h_1[chp]) *
        #                               self.dual_node_gas_balance[self.chp_upper_connection_gas_index[chp], time, k])
        # 下层chp的成本
        for chp in range(self.chp_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.well_lower_cost[self.chp_lower_connection_well_index[chp]] *
                                      (self.lower_chp_heat_output[chp, time, k] * self.chp_lower_coeff_h_1[chp]) * 1)
                    #self.upper_chp_gas_quoted_price[chp, time])
        # ！！！！？？？？？
        # Lower CHP : 耗气量 * 节点边际气价
        # for chp in range(self.chp_lower_num):
        #     for time in range(T):
        #         for k in range(K):
        #             lower_objs.append(
        #                 self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, time, k] )

        for well in range(self.well_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.upper_well_quoted_price[0, time] * self.upper_gas_well_output[well, time, k])

        for well in range(self.well_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.well_lower_cost[well] * self.lower_gas_well_output[well, time, k])

        self.lower_objective = sum(lower_objs)

    # KKT 等价中的 求导部分
    def build_kkt_derivative_constraints(self, penalty):
        # 包含 下层目标函数 + lagrange 基本部分 + lagrange 增量部分 + P-CCP 罚项
        for k in range(K):
            self.DE[k] = sum(self.DE[k])
        self.dual_expression_basic = sum(self.DE)
        my_expr = MyExpr(self.lower_objective +
                         self.dual_expression_basic +
                         0*self.dual_expression_additional +
                         0*penalty * sum(self.pccp_relax.flatten()))
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
        for chp in range(self.chp_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_chp_gas_quoted_price_tuple_dict[chp, t],
                    rhs=10,
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_chp_gas_quoted_price_max' + str(t) + "chp_" + str(chp)
                )
        for well in range(self.well_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_well_quoted_price_tuple_dict[well, t],
                    rhs=self.well_upper_quoted_price_max[well],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_gas_well_quoted_price_max' + str(t) + '_well_' + str(well)
                )

    # 上层的目标函数， 这里 是 非线性的 直接 => 产量 * 边际价格 - 成本，    这里的一个问题是， chp的天然气 需要 按节点边际气价 付费吗？
    def build_upper_objective(self):  #
        obj_k = []
        for k in range(K):
            expected_cost = []

            # chp 收益    节点边际热价 * 热输出 - chp 的成本       (const + p1 * power  + p3 * heat) * 节点边际气价      购气成本
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    expected_cost.append(self.upper_chp_heat_output[chp, t, k] *
                                         self.dual_heater_balance[self.chp_upper_connection_heater_index[chp], t, k])
                    expected_cost.append(-1 * self.upper_chp_heat_output[chp, t, k] * self.chp_upper_coeff_h_1[chp] *
                                         self.well_upper_cost[self.chp_upper_connection_well_index[chp]])     # 写法1
                    # expected_cost.append((-1 * self.upper_chp_heat_output[chp, t, k] * self.chp_upper_coeff_h_1[chp]) *
                    # self.dual_node_gas_balance[self.chp_upper_connection_gas_index[chp], t, k])    # 写法2
            # well  气井的收益
            for well in range(self.well_upper_num):
                for t in range(T):
                    expected_cost.append(self.upper_gas_well_output[well, t, k] *
                                         self.dual_node_gas_balance[self.well_upper_connection_index[well], t, k])
                    expected_cost.append(-1 * self.upper_gas_well_output[well, t, k] * self.well_upper_cost[well])

            obj_k.append(-1 * sum(expected_cost))
        self.obj_k = obj_k

    def build_upper_objective_(self):
        LC = [[] for i in range(K)]
        for k in range(K):
            # for gen in range(self.generator_lower_num):
            #     for t in range(T):
            #         LC[k].append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
            for chp in range(self.chp_lower_num):
                for t in range(T):
                    # LC[k].append(self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, t, k])
                    LC[k].append(self.well_lower_cost[self.chp_lower_connection_well_index[chp]] *
                                 self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, t, k])
            for well in range(self.well_lower_num):
                for t in range(T):
                    LC[k].append(self.well_lower_cost[well] * self.lower_gas_well_output[well, t, k])
            LC[k] = sum(LC[k])
        ## equivalnet
        OE = [[] for i in range(K)]
        for k in range(K):
            # for gen in range(self.generator_upper_num):
            #     for t in range(T):
            #         OE[k].append(-1 * self.dual_upper_generator_power_output_min[gen, t, k] * self.generator_upper_min[gen])
            #         OE[k].append(self.dual_upper_generator_power_output_max[gen, t, k] * self.generator_upper_max[gen])
            for well in range(self.well_upper_num):
                for t in range(T):
                    OE[k].append(-1 * self.dual_well_upper_output_min[well, t, k] * self.well_upper_output_min[well])
                    OE[k].append(1 * self.dual_well_upper_output_max[well, t, k] * self.well_upper_output_max[well])
                    OE[k].append(self.dual_well_upper_capacity[well, t, k] * self.well_upper_output_max[well])
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    temp = []
                    for point in range(self.chp_point_num):
                        temp.append(self.dual_upper_chp_point_less_one[chp, point, t, k])
                    OE[k].append(sum(temp))
                    OE[k].append(-1 * self.dual_upper_chp_point_sum_one[chp, t, k])
            OE[k] = sum(OE[k])

        Dobj = [0 for i in range(K)]
        for k in range(K):
            Dobj[k] = sum(self.Dobj[k])

        ## upper cost
        UC = [[] for i in range(K)]
        for k in range(K):
            for well in range(self.well_upper_num):
                for t in range(T):
                    UC[k].append(self.well_upper_cost[well] * self.upper_gas_well_output[well, t, k])

            for chp in range(self.chp_upper_num):
                for t in range(T):
                    UC[k].append(self.well_upper_cost[self.chp_upper_connection_well_index[chp]] *
                                 self.upper_chp_heat_output[chp, t, k] * self.chp_upper_coeff_h_1[chp])

        for k in range(K):
            UC[k] = sum(UC[k])

        for k in range(K):
            self.obj_k.append((Dobj[k] - LC[k] + OE[k] - UC[k]) * (-1))

    def optimize(self, distribution):
        # self.model.setParam("IntegralityFocus", 1)
        self.model.setParam("NonConvex", 2)
        self.model.setParam("MIPFocus", 3)
        self.model.setParam('TimeLimit', 60)
        # self.model.setParam("OutputFlag", 0)

        self.model.setObjective(np.array(self.obj_k).dot(np.array(distribution)))
        # self.model.setObjective(0)
        # self.model.setObjective((np.array(self.obj_k) + np.array(self.objection_aux_update)).dot(np.array(distribution)))
        self.model.optimize()

        # expected_cost = []
        # for chp in range(self.chp_upper_num):
        #     for t in range(T):
        #         for k in range(K):
        #             expected_cost.append(self.upper_chp_heat_output[chp, t, k] * self.dual_heater_balance[0, t, k])
        #             expected_cost.append(self.upper_chp_power_output[chp, t, k] *
        #                                  self.dual_node_power_balance[self.chp_upper_connection_power_index[chp], t, k])
        # for gen in range(self.generator_upper_num):
        #     for t in range(T):
        #         for k in range(K):
        #             expected_cost.append(self.upper_generator_power_output[gen, t, k] *
        #                                  self.dual_node_power_balance[self.generator_upper_connection_index[gen], t, k])
        #
        # self.expected_revenue = sum(expected_cost)

        weymouth_left = []
        weymouth_right = []
        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    weymouth_left.append(self.gas_weymouth[line] *
                                         ((self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] *
                                           self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] -
                                           self.gas_node_pressure[self.gas_pipe_end_node[line], t, k] *
                                           self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]).getValue()))
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
                    objs_revenue.append(-1 * self.dual_node_power_balance[self.wind_connection_index[wind], t, k] *
                                        self.wind_output[wind, k, t])
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
