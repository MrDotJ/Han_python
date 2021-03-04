from resource.utility import *
from resource.config3_with_gas import T, K
from math import sqrt
from resource.config3_with_gas import get_config
Linear_POINTS = 10


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system, gas_system):
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

        self.upper_well_quoted_price                        = None

        self.upper_well_quoted_price_tuple_dict             = None

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
        self.dual_expression                                = 0
        self.dual_expression_basic                          = 0
        self.dual_expression_additional                     = 0
        self.lower_objective                                = None
        self.upper_objective                                = None
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
        self.gas_node_pressure_aux                          = None
        self.gas_flow_aux                                   = None

        self.all_lower_level_vars                           = []
        self.obj_k                                          = []
        self.do_nothing                                     = 0
        self.equivalent_cost                                = 0
        self.equivalent_revenue                             = 0
        self.old_vars_constraints                           = []
        self.objection_aux_update                           = []
        self.pressure_continue                              = []
        self.pressure_binary                                = []
        self.flow_continue                                  = []
        self.flow_binary                                    = []


    def build_gas_system(self):
        self.upper_well_quoted_price_tuple_dict   = self.model.addVars(self.well_upper_num, T, name='upper_gas_quoted_price')
        self.upper_well_quoted_price              = tonp( self.upper_well_quoted_price_tuple_dict)

        self.upper_gas_well_output                = \
            tonp( self.model.addVars(self.well_upper_num, T, K, name='upper_well_output',          lb=-1 * INFINITY, ub=INFINITY ) )
        self.lower_gas_well_output                = \
            tonp( self.model.addVars(self.well_lower_num, T, K, name='lower_well_output',          lb=-1 * INFINITY, ub=INFINITY ) )
        self.gas_node_pressure                    = \
            tonp( self.model.addVars(self.gas_node_num,   T, K, name='gas_node_pressure',          lb=-1 * INFINITY, ub=INFINITY ) )
        self.gas_flow_in                          = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='gas_flow_in',                lb=-1 * INFINITY, ub=INFINITY ) )
        self.gas_flow_out                         = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='gas_flow_out',               lb=-1 * INFINITY, ub=INFINITY ) )
        self.aux_weymouth_left                    = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='weymouth_left_auxiliary',    lb=-1 * INFINITY, ub=INFINITY ) )
        self.aux_weymouth_right_1                 = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='weymouth_right_auxiliary1',  lb=-1 * INFINITY, ub=INFINITY ) )
        self.aux_weymouth_right_2                 = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='weymouth_right_auxiliary2',  lb=-1 * INFINITY, ub=INFINITY ) )
        self.pccp_relax                           = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='pccp_relax',                 lb=-1 * INFINITY, ub=INFINITY ) )
        self.gas_linepack                         = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='gas_linepack',               lb=-1 * INFINITY, ub=INFINITY ) )
        self.gas_node_pressure_aux                = \
            tonp( self.model.addVars(self.gas_node_num,   T, K, name='gas_node_pressure_aux',      lb=-1 * INFINITY, ub=INFINITY ) )
        self.gas_flow_aux                         = \
            tonp( self.model.addVars(self.gas_line_num,   T, K, name='gas_flow_aux',               lb=-1 * INFINITY, ub=INFINITY ) )


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


        self.all_lower_level_vars.extend(self.upper_gas_well_output .flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_gas_well_output .flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_node_pressure     .flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_in           .flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_flow_out          .flatten().tolist())
        self.all_lower_level_vars.extend(self.gas_linepack          .flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_left     .flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_right_1  .flatten().tolist())
        self.all_lower_level_vars.extend(self.aux_weymouth_right_2  .flatten().tolist())
        self.all_lower_level_vars.extend(self.pccp_relax            .flatten().tolist())
        self.do_nothing = 1

    def build_gas_system_original_and_dual_constrains(self):
        dual_expr = []
        # # ==================================== node balance ===================================
        # 气网的 节点 气平衡
        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(self.upper_gas_well_output[  np.where(self.well_upper_connection_index    == node), t, k].flatten()) +  \
                        sum(self.lower_gas_well_output[  np.where(self.well_lower_connection_index    == node), t, k].flatten()) +  \
                        sum(self.gas_flow_out[           np.where(self.gas_pipe_end_node              == node), t, k].flatten()) -  \
                        sum(self.gas_flow_in[            np.where(self.gas_pipe_start_node            == node), t, k].flatten()) -   \
                        sum(self.gas_load[               np.where(self.gas_load_connection_index      == node), t   ].flatten())
                    name1 = 'dual_node_gas_balance_time_' + str(t) + '_node_' + str(node) + 'scenario_' + str(k)
                    self.model.addConstr(cons_expr1 == 0, name=name1)
        # # ==================================== gas linepack ==================================
        # 气管网 的 linepack 与 气压 / 时间的关系 0 - T-2
        for line in self.gas_inactive_line:
            for t in range(0, T-1):
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] +
                            self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, t+1, k] - self.gas_linepack[line, t, k] - \
                                 self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    name1 = 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    name2 = 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 == 0, name=name1)
                    self.model.addConstr(cons_expr2 == 0, name=name2)
        # 气管网 的 linepack 与 气压/时间 的关系 T-1
        for line in self.gas_inactive_line:
            for t in [T-1]:
                for k in range(K):
                    cons_expr1 = self.gas_linepack[line, t, k] - self.gas_linepack_coeff[line] * (
                            self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] +
                            self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]) / 2
                    cons_expr2 = self.gas_linepack[line, 0, k] - self.gas_linepack[line, t, k] - \
                                 self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k]
                    name1 = 'dual_gas_linepack_equation_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    name2 = 'dual_gas_linepack_with_time_line_' + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 == 0, name=name1)
                    self.model.addConstr(cons_expr2 == 0, name=name2)
        # # ======================================== active line ===================================
        # active 线路 的气损耗
        for line in self.gas_active_line:
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_out[line, t, k] - 0.97 * self.gas_flow_in[line, t, k]
                    name1 = 'dual_gas_flow_active_line_' + str(line) + '_time_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 == 0, name=name1)
        # active 线路 气压变化
        for compressor, line in enumerate(self.gas_active_line):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_compressor_coeff[compressor] * \
                                 self.gas_node_pressure[self.gas_pipe_start_node[line], t, k] - \
                                 self.gas_node_pressure[self.gas_pipe_end_node[line], t, k]
                    name1 = 'dual_compressor_pressure_' + str(compressor) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 >= 0, name=name1)
        # # ======================================= gas well =========================================
        # 上层 气井 的 出力范围
        for well in range(self.well_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.upper_gas_well_output[well, t, k] - self.well_upper_output_min[well]
                    cons_expr2 = -1 * self.upper_gas_well_output[well, t, k] + self.well_upper_output_max[well]
                    name1 = 'dual_upper_well_output_min_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k)
                    name2 = 'dual_upper_well_output_max_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 >= 0, name=name1)
                    self.model.addConstr(cons_expr2 >= 0, name=name2)
        # 下层 气井 的 出力范围
        for well in range(self.well_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.lower_gas_well_output[well, t, k] - self.well_lower_output_min[well]
                    cons_expr2 = -1 * self.lower_gas_well_output[well, t, k] + self.well_lower_output_max[well]
                    name1 = 'dual_lower_well_output_min_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k)
                    name2 = 'dual_lower_well_output_max_' + str(well) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 >= 0, name=name1)
                    self.model.addConstr(cons_expr2 >= 0, name=name2)
        # # ==================================== gas node ===============================================
        # 节点 气压 上下限
        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_node_pressure[node, t, k] - self.gas_node_pressure_min[node]
                    cons_expr2 = self.gas_node_pressure_max[node] - self.gas_node_pressure[node, t, k]
                    name1 = 'dual_node_pressure_min_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k)
                    name2 = 'dual_node_pressure_max_' + str(node) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 >= 0, name=name1)
                    self.model.addConstr(cons_expr2 >= 0, name=name2)
        # # ==================================== gas flow ==================================================
        # 管道流量 上下限
        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.gas_flow_in[line, t, k] - self.gas_flow_in_min[line]
                    cons_expr2 = -1 * self.gas_flow_in[line, t, k] + self.gas_flow_in_max[line]
                    cons_expr3 = self.gas_flow_out[line, t, k] - self.gas_flow_out_min[line]
                    cons_expr4 = -1 * self.gas_flow_out[line, t, k] + self.gas_flow_out_max[line]
                    name1 = 'dual_gas_flow_in_min'  + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    name2 = 'dual_gas_flow_in_max'  + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    name3 = 'dual_gas_flow_out_min' + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    name4 = 'dual_gas_flow_out_max' + str(line) + '_t_' + str(t) + '_scenario_' + str(k)
                    self.model.addConstr(cons_expr1 >= 0, name=name1)
                    self.model.addConstr(cons_expr2 >= 0, name=name2)
                    self.model.addConstr(cons_expr3 >= 0, name=name3)
                    self.model.addConstr(cons_expr4 >= 0, name=name4)
        # # ==================================== pressure^2 aux ===========================================
        for node in range(self.gas_node_num):
            for t in range(T):
                for k in range(K):
                    x_point = np.linspace(0, 10, Linear_POINTS)
                    y_point = x_point**2
                    x_continue = tonp(self.model.addVars(Linear_POINTS))
                    self.pressure_continue.append(x_continue)
                    # continue constraints
                    cons_expr1 = x_continue.dot(x_point) - self.gas_node_pressure[node, t, k]
                    cons_expr2 = sum(x_continue) - 1
                    cons_expr3 = x_continue.dot(y_point) - self.gas_node_pressure_aux[node, t, k]
                    self.model.addConstr(cons_expr1 == 0)
                    self.model.addConstr(cons_expr2 == 0)
                    self.model.addConstr(cons_expr3 == 0)

                    x_binary = tonp(self.model.addVars(Linear_POINTS, vtype=gurobi.GRB.BINARY))
                    self.pressure_binary.append(x_binary)
                    # binary constraints
                    for point in range(Linear_POINTS):
                        self.model.addConstr(x_continue[point] <= x_binary[point])
                    self.model.addConstr(gurobi.quicksum(x_binary) <= 2)
                    for point1 in range(Linear_POINTS):  # [0 1 2 3 4]  1
                        for point2 in range(point1, Linear_POINTS): # [ 1 2 3 4]
                            if (point2 - point1) >= 2:
                                self.model.addConstr(x_binary[point1] + x_binary[point2] <= 1)
        # # ==================================== (flow_in + flow_out)^2 aux ==============================
        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    x_point = np.linspace(0, 10, Linear_POINTS)
                    y_point = x_point**2
                    x_continue = tonp(self.model.addVars(Linear_POINTS))
                    self.flow_continue.append(x_continue)
                    # continue constraints
                    cons_expr1 = x_continue.dot(x_point) - (self.gas_flow_in[line, t, k] + self.gas_flow_out[line, t, k])
                    cons_expr2 = sum(x_continue) - 1
                    cons_expr3 = x_continue.dot(y_point) - self.gas_flow_aux[line, t, k]
                    self.model.addConstr(cons_expr1 == 0)
                    self.model.addConstr(cons_expr2 == 0)
                    self.model.addConstr(cons_expr3 == 0)

                    x_binary = tonp(self.model.addVars(Linear_POINTS, vtype=gurobi.GRB.BINARY))
                    self.flow_binary.append(x_binary)
                    # binary constraints
                    for point in range(Linear_POINTS):
                        self.model.addConstr(x_continue[point] <= x_binary[point])
                    self.model.addConstr(gurobi.quicksum(x_binary) <= 2)
                    for point1 in range(Linear_POINTS):  # [0 1 2 3 4]  1
                        for point2 in range(point1, Linear_POINTS): # [ 1 2 3 4]
                            if (point2 - point1) >= 2:
                                self.model.addConstr(x_binary[point1] + x_binary[point2] <= 1)
        # # ==================================== Weymouth ==================================================
        for line in range(self.gas_line_num):
            for t in range(T):
                for k in range(K):
                    start_node = self.gas_pipe_start_node[line]
                    end_node = self.gas_pipe_end_node[line]
                    self.model.addConstr(
                        self.gas_node_pressure_aux[start_node, t, k] - self.gas_node_pressure_aux[end_node, t, k] ==
                        self.gas_flow_aux[line, t, k],
                        name='Weymouth'+str(line) + str(t) + str(k))


    # 构建 下层 的目标函数
    def build_lower_objective(self):
        lower_objs = []
        # 上层 发电机的报价 成本
        for gen in range(self.generator_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.upper_generator_quoted_price[gen, time] * self.upper_generator_power_output[gen, time, k])
        # 下层 发电机的 发电 成本
        for gen in range(self.generator_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, time, k])
        # 上层 chp 的 报价 成本
        for chp in range(self.chp_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.upper_chp_power_output[chp, time, k] * self.upper_chp_power_quoted_price[chp, time])
                    lower_objs.append(self.upper_chp_heat_output[chp, time, k] * self.upper_chp_heat_quoted_price[chp, time])
        # 下层 chp 的 生产 成本， 这里 先做线性 处理
        for chp in range(self.chp_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(
                        self.chp_lower_coeff_const[chp] +
                        self.chp_lower_coeff_p_1[chp] * self.lower_chp_power_output[chp, time, k] +
                        # self.chp_lower_coeff_p_2[chp] * self.lower_chp_power_output[chp, time, k] * self.lower_chp_power_output[chp, time, k] +
                        self.chp_lower_coeff_h_1[chp] * self.lower_chp_heat_output[chp, time, k])
                        # self.chp_lower_coeff_h_2[chp] * self.lower_chp_heat_output[chp, time, k] * self.lower_chp_heat_output[chp, time, k] +
                        # self.chp_lower_coeff_cross[chp] * self.lower_chp_power_output[chp, time, k] * self.lower_chp_heat_output[chp, time, k])
        # 上层 well 的报价成本
        for well in range(self.well_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.upper_well_quoted_price[well, time] * self.upper_gas_well_output[well, time, k])
        # 下层 well 的 生产成本
        for well in range(self.well_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.well_lower_cost[well] * self.lower_gas_well_output[well, time, k])

        self.lower_objective = sum(lower_objs)

    def build_kkt_derivative_constraints(self, penalty):
        # 构建 lagrange 表达式， 目标函数 + 基本对偶项 + 更新对偶项 + P-CCP罚项
        my_expr = MyExpr(self.lower_objective +
                         self.dual_expression_basic +
                         self.dual_expression_additional +
                         penalty * sum(self.pccp_relax.flatten()))
        # 对 所有 原变量 求导 等于0
        for var in self.all_lower_level_vars:
            expr = my_expr.getCoeff(var)
            my_expr.addConstr(expr, self.model, var.VarName)

    def build_upper_constraints(self):
        # 上层 发电机的 报价 约束
        for gen in range(self.generator_upper_num):
            for t in range(T):
                self.model.addConstr(
                   lhs=self.upper_generator_quoted_price_tuple_dict[gen, t],
                   rhs=self.upper_generator_quoted_price_max[gen][t],
                   sense=gurobi.GRB.LESS_EQUAL,
                   name='upper_generator_quoted_price_max_time' + str(t) + 'gen_' + str(gen))
        # 上层 chp 的电报价 约束
        for chp in range(self.chp_upper_num):
            for t in range(T):
                self.model.addConstr(
                   lhs=self.upper_chp_power_quoted_price_tuple_dict[chp, t],
                   rhs=self.upper_chp_power_quoted_price_max[chp][t],
                   sense=gurobi.GRB.LESS_EQUAL,
                   name='upper_chp_power_quoted_price_max' + str(t) + 'chp_' + str(chp)
                )
        # 上层 chp 的热报价 约束
        for chp in range(self.chp_upper_num):
            for t in range(T):
                self.model.addConstr(
                    lhs=self.upper_chp_heat_quoted_price_tuple_dict[chp, t],
                    rhs=self.upper_chp_heat_quoted_price_max[chp][t],
                    sense=gurobi.GRB.LESS_EQUAL,
                    name='upper_chp_heat_quoted_price_max' + str(t) + 'chp_' + str(chp)
                )
        # 上层 well 的气报价 约束
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
        for k in range(K):
            expected_cost = []
            # 上层 chp 的 电收益 / 热收益 -  chp 成本
            for chp in range(self.chp_upper_num):
                for t in range(T):
                    expected_cost.append(self.upper_chp_heat_output[chp, t, k] *
                                         self.dual_heater_balance[self.chp_upper_connection_heater_index[chp], t, k])
                    expected_cost.append(self.upper_chp_power_output[chp, t, k] *
                                         self.dual_node_power_balance[self.chp_upper_connection_power_index[chp], t, k])
                    expected_cost.append(-1 * self.upper_chp_heat_output[chp, t, k] * self.chp_upper_coeff_h_1[chp] -
                                         self.upper_chp_power_output[chp, t, k] * self.chp_upper_coeff_p_1[chp])
            # 上层 generator 的 电收益 - 电成本
            for gen in range(self.generator_upper_num):
                for t in range(T):
                    expected_cost.append(self.upper_generator_power_output[gen, t, k] *
                                         self.dual_node_power_balance[self.generator_upper_connection_index[gen], t, k])
                    expected_cost.append(-1 * self.upper_generator_power_output[gen, t, k] * self.generator_upper_cost[gen])
            # 上层 well 的 气收益 - 气成本
            for well in range(self.well_upper_num):
                for t in range(T):
                    expected_cost.append(self.upper_gas_well_output[well, t, k] *
                                         self.dual_node_gas_balance[self.well_upper_connection_index[well], t, k])
                    expected_cost.append(-1 * self.upper_gas_well_output[well, t, k] * self.well_upper_cost[well])
            obj_k.append(-1 * sum(expected_cost))
        self.obj_k = obj_k

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

    def optimize(self):
        self.model.setParam("IntegralityFocus", 1)
        # self.model.setParam("NonConvex", 2)
        # self.model.setParam("OutputFlag", 0)

        self.model.setObjective(0)
        self.model.optimize()



def fff():
    # fx + gy + hz
    # upper constraints
    # all lower constraints
    # ===>new lower variables          -| A
    # ===>lower objective great         | D
    # ===>KKT equivalent constraints   -| D
    mo.build_upper_and_lower_variables()
    mo.set_upper_objective()
    mo.build_upper_constraints()
    mo.build_lower_constraints()
    lower_bound = mo.optimize()
    mo.build_subproblem1()
    obj1 = mo.optimize_subproblem1()
    lower_bound = mo.build_subproblem2(obj1)
    mo.update_new_lower_KKT_equivalent_constraints()
    a = 0
    return a


if __name__ == '__main__':
    power_system, heat_system, chp_system, gas_system = get_config()
    model = OneLayer(power_system, heat_system, chp_system, gas_system)
    model.build_gas_system()
    model.build_gas_system_original_and_dual_constrains()
    model.optimize()