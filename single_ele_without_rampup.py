from resource.utility import *
from resource.config2 import T, K


class OneLayer:
    def __init__(self, power_system, heat_system, chp_system):
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
        self.generator_upper_cost               = power_system['upper_generator_cost']
        self.upper_generator_quoted_price_max   = power_system['upper_generator_quoted_price_max']

        self.generator_lower_connection_index   = power_system['lower_generator_connection_index']
        self.generator_lower_num                = power_system['lower_generator_num']
        self.generator_lower_max                = power_system['lower_generator_max']
        self.generator_lower_min                = power_system['lower_generator_min']
        self.generator_lower_cost               = power_system['lower_generator_cost']

        self.ele_load_num                       = power_system['load_num']
        self.ele_load_index                     = power_system['load_index']
        self.ele_load                           = power_system['load']

        self.wind_connection_index              = power_system['wind_connection_index']
        self.wind_output                        = power_system['wind_output']


        # model
        self.model = gurobi.Model()
        self.upper_generator_quoted_price                   = None
        self.upper_generator_quoted_price_tuple_dict        = None

        self.upper_generator_power_output                   = None
        self.lower_generator_power_output                   = None


        self.line_power_flow                                = None
        self.bus_angle                                      = None
        self.dual_expression                                = 0
        self.lower_objective                                = None
        self.upper_objective                                = None
        self.dual_node_power_balance                        = None
        self.dual_line_power_flow_great                     = None
        self.dual_line_power_flow_less                      = None
        self.dual_lower_generator_power_output_min          = None
        self.dual_lower_generator_power_output_max          = None

        self.all_lower_level_vars                           = []
        self.obj_k                                          = []
        self.do_nothing                                     = 0
        self.expected_generator_revenue                     = 0
        self.equivalent_generator_cost                         = 0
        self.dual_upper_generator_power_output_min          = None
        self.dual_upper_generator_power_output_max          = None
        self.dual_angle_line                                = None
        self.dual_reference_angle                           = None


    def build_power_system(self):
        self.upper_generator_quoted_price_tuple_dict      = self.model.addVars(self.generator_upper_num, T, lb=0,                       name='upper_generator_quoted_price')
        self.upper_generator_quoted_price                 = tonp( self.upper_generator_quoted_price_tuple_dict                                                             )
        self.upper_generator_power_output                 = tonp( self.model.addVars(self.generator_upper_num, T, K,                    name='upper_generator_power'       )                                                 )
        self.lower_generator_power_output                 = tonp( self.model.addVars(self.generator_lower_num, T, K,                    name='lower_generator_power'       )                                                 )
        self.line_power_flow                              = tonp( self.model.addVars(self.ele_line_num,        T, K, lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='line_power_flow'             )                                                       )
        self.bus_angle                                    = tonp( self.model.addVars(self.ele_node_num,        T, K, lb=-1 * gurobi.GRB.INFINITY, ub=gurobi.GRB.INFINITY, name='bus_angle'                   )                                                             )

        self.dual_node_power_balance                      = np.empty((self.ele_node_num,        T,   K, ), dtype=object)
        self.dual_line_power_flow_great                   = np.empty((self.ele_line_num,        T,   K, ), dtype=object)
        self.dual_line_power_flow_less                    = np.empty((self.ele_line_num,        T,   K, ), dtype=object)
        self.dual_lower_generator_power_output_min        = np.empty((self.generator_lower_num, T,   K, ), dtype=object)
        self.dual_lower_generator_power_output_max        = np.empty((self.generator_lower_num, T,   K, ), dtype=object)
        self.dual_upper_generator_power_output_min        = np.empty((self.generator_upper_num, T,   K, ), dtype=object)
        self.dual_upper_generator_power_output_max        = np.empty((self.generator_upper_num, T,   K, ), dtype=object)
        self.dual_angle_line                              = np.empty((self.ele_line_num,        T,   K, ), dtype=object)
        self.dual_reference_angle                         = np.empty((T, K, ),                             dtype=object)

        self.all_lower_level_vars.extend(self.upper_generator_power_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.lower_generator_power_output.flatten().tolist())
        self.all_lower_level_vars.extend(self.line_power_flow.flatten().tolist())
        self.all_lower_level_vars.extend(self.bus_angle.flatten().tolist())

    def build_gas_system(self):
        self.do_nothing = 1

    def build_heat_system(self):
        self.do_nothing = 1

    def build_power_system_original_and_dual_constraints(self):
        self.model.update()
        dual_expr = []
        for node in range(self.ele_node_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = \
                        sum(self.upper_generator_power_output[np.where(self.generator_upper_connection_index == node), t, k].flatten()) + \
                        sum(self.lower_generator_power_output[np.where(self.generator_lower_connection_index == node), t, k].flatten()) + \
                        sum(self.wind_output[                 np.where(self.wind_connection_index == node), k, t].flatten()) -  \
                        sum(self.line_power_flow[             np.where(self.ele_line_start == node), t, k].flatten()) +  \
                        sum(self.line_power_flow[             np.where(self.ele_line_end == node), t, k].flatten()) -  \
                        sum(self.ele_load[                    np.where(self.ele_load_index == node), t].flatten())
                    self.dual_node_power_balance[node, t, k], expr1 = Complementary_equal(1 * cons_expr1, self.model, 'dual_node_power_balance_' + str(t) + '_' + str(node) + '_' + 'scenario' + str(k))
                    dual_expr.append(expr1)

        for line in range(self.ele_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = (self.bus_angle[self.ele_line_start[line], t, k] -
                                  self.bus_angle[self.ele_line_end[line], t, k]) / self.line_reactance[line] / 10 - \
                                 self.line_power_flow[line, t, k]
                    self.dual_angle_line[line, t, k], expr1 = Complementary_equal(cons_expr1, self.model, 'dual_angle_line_' + str(t) + 'line' + str(line) + 'scenario' + str(k))
                    dual_expr.append(expr1)

        for t in range(T):
            for k in range(K):
                cons_expr1 = self.bus_angle[2, t, k]
                self.dual_reference_angle[t, k], expr1 = Complementary_equal(cons_expr1, self.model, 'dual_reference_angle_' + str(t) + 'scenario' + str(k))
                dual_expr.append(expr1)


        for line in range(self.ele_line_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.line_power_flow[line, t, k] + self.ele_line_capacity[line]
                    cons_expr2 = -1 * self.line_power_flow[line, t, k] + self.ele_line_capacity[line]
                    self.dual_line_power_flow_great[line, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_line_power_flow_great' + str(t) + '_' + str(line) + 'scenario' + str(k))
                    self.dual_line_power_flow_less[line, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_line_power_flow_less' + str(t) + '_' + str(line) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_upper_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.upper_generator_power_output[gen, t, k] - self.generator_upper_min[gen]
                    cons_expr2 = -1 * self.upper_generator_power_output[gen, t, k] + self.generator_upper_max[gen]
                    self.dual_upper_generator_power_output_min[gen, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_upper_generator_power_output_min' + str(t) + '_' + str(gen) + 'scenario' + str(k))
                    self.dual_upper_generator_power_output_max[gen, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_upper_generator_power_output_max' + str(t) + '_' + str(gen) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)

        for gen in range(self.generator_lower_num):
            for t in range(T):
                for k in range(K):
                    cons_expr1 = self.lower_generator_power_output[gen, t, k] - self.generator_lower_min[gen]
                    cons_expr2 = -1 * self.lower_generator_power_output[gen, t, k] + self.generator_lower_max[gen]
                    self.dual_lower_generator_power_output_min[gen, t, k], expr1 = Complementary_great(cons_expr1, self.model, 'dual_lower_generator_power_output_min' + str(t) + '_' + str(gen) + 'scenario' + str(k))
                    self.dual_lower_generator_power_output_max[gen, t, k], expr2 = Complementary_great(cons_expr2, self.model, 'dual_lower_generator_power_output_max' + str(t) + '_' + str(gen) + 'scenario' + str(k))
                    dual_expr.append(expr1)
                    dual_expr.append(expr2)


        self.dual_expression = self.dual_expression + sum(dual_expr)

    def build_heat_system_original_and_dual_constraints(self):
        self.do_nothing = 1

    def build_gas_system_original_and_dual_constrains(self):
        self.do_nothing = 1

    def build_lower_objective(self):
        lower_objs = []
        for gen in range(self.generator_upper_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.upper_generator_quoted_price[gen, time] * self.upper_generator_power_output[gen, time, k])
        for gen in range(self.generator_lower_num):
            for time in range(T):
                for k in range(K):
                    lower_objs.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, time, k])
        self.lower_objective = sum(lower_objs)

    def build_kkt_derivative_constraints(self):
        my_expr = MyExpr(self.dual_expression + self.lower_objective)
        for var in self.all_lower_level_vars:
            expr = my_expr.getCoeff(var)
            my_expr.addConstr(expr, self.model)

    def build_upper_constraints(self):
        for gen in range(self.generator_upper_num):
            for t in range(T):
                self.model.addConstr(
                   lhs=self.upper_generator_quoted_price_tuple_dict[gen, t],
                   rhs=1 * self.upper_generator_quoted_price_max[gen][t],
                   sense=gurobi.GRB.LESS_EQUAL,
                   name='upper_generator_quoted_price_max_time' + str(t) + 'gen_' + str(gen))
                self.model.addConstr(
                    lhs=self.upper_generator_quoted_price_tuple_dict[gen, t],
                    rhs=1 * self.generator_upper_cost[gen],
                    sense=gurobi.GRB.GREATER_EQUAL,
                    name='upper_generator_quoted_price_min_time' + str(t) + 'gen_' + str(gen))


    def build_upper_objective(self):
        obj_k = []
        obj_k_p = []
        for k in range(K):
            objs = []
            objs_p = []
            for gen in range(self.generator_upper_num):    # generator  成本
                for t in range(T):
                    objs.append(self.generator_upper_cost[gen] * self.upper_generator_power_output[gen, t, k])

            for gen in range(self.generator_lower_num):
                for t in range(T):
                    objs.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
                    objs.append(-1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
                    objs.append(self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])
                    objs_p.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])
                    objs_p.append(-1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
                    objs_p.append(self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])

            for line in range(self.ele_line_num):
                for t in range(T):
                    objs.append(self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
                    objs.append(self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])
                    objs_p.append(self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
                    objs_p.append(self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])

            for load in range(self.ele_load_num):
                for t in range(T):
                    objs.append(-1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])
                    objs_p.append(-1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])






            obj_k.append(sum(objs))
            obj_k_p.append(sum(objs_p))

        self.obj_k = obj_k
        self.equivalent_generator_cost = obj_k_p

    def optimize(self, distribution):
        self.model.setObjective(np.array(self.obj_k).dot(np.array(distribution)))
        self.model.optimize()
        expected_cost = []
        for gen in range(self.generator_upper_num):
            for t in range(T):
                for k in range(K):
                    expected_cost.append(self.upper_generator_power_output[gen, t, k] * self.dual_node_power_balance[self.generator_upper_connection_index[gen], t, k])
        self.expected_generator_revenue = sum(expected_cost)
        value_generator_quoted_price = to_value(self.upper_generator_quoted_price_tuple_dict)
        value_chp_power_quoted_price = to_value(self.upper_generator_quoted_price_tuple_dict)
        value_chp_heat_quoted_price = to_value(self.upper_generator_quoted_price_tuple_dict)
        obj_k = np.array([obj.getValue() for obj in self.obj_k])
        return value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price, obj_k



objs = []
for k in range(K):
    for load in range(self.ele_load_num):
        for t in range(T):
            objs.append(1 * self.dual_node_power_balance[self.ele_load_index[load], t, k] * self.ele_load[load, t])
    for line in range(self.ele_line_num):
        for t in range(T):
            objs.append(-1 * self.dual_line_power_flow_great[line, t, k] * self.ele_line_capacity[line])
            objs.append(-1 * self.dual_line_power_flow_less[line, t, k] * self.ele_line_capacity[line])
    for gen in range(self.generator_upper_num):
        for t in range(T):
            objs.append(self.dual_upper_generator_power_output_min[gen, t, k] * self.generator_upper_min[gen])
            objs.append(-1 * self.dual_upper_generator_power_output_max[gen, t, k] * self.generator_upper_max[gen])
    for gen in range(self.generator_lower_num):
        for t in range(T):
            objs.append(1 * self.dual_lower_generator_power_output_min[gen, t, k] * self.generator_lower_min[gen])
            objs.append(-1 * self.dual_lower_generator_power_output_max[gen, t, k] * self.generator_lower_max[gen])

objs2 = []
for k in range(K):
    for gen in range(self.generator_upper_num):
        for t in range(T):
            objs2.append(self.upper_generator_quoted_price[gen, t] * self.upper_generator_power_output[gen, t, k])
    for gen in range(self.generator_lower_num):
        for t in range(T):
            objs2.append(self.generator_lower_cost[gen] * self.lower_generator_power_output[gen, t, k])