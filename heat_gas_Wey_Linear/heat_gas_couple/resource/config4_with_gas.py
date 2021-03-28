import numpy as np
T = 1
K = 1
empirical_distribution = [1/K] * K
confidence_level = 0.2


def get_config():
    #   Bus     P_max   P_min   Ramp_up   Ramp_down   Cost    bid_max
    upper_generator_info = np.array([
        [0,      0.6,    0.0,       1.5,      1.5,       10,      20],
        [3,      0.4,    0.0,       1.5,      1.5,       10,      34],
        [2,      0.4,    0.0,       1.5,      1.5,       10,      20],
        [4,      0.4,    0.0,       1.5,      1.5,       10,      20],
    ])

    lower_generator_info = np.array([
        [0,      0.4,    0.0,       1.5,      1.5,       16],
        [3,      1.4,    0.0,       1.5,      1.5,       16],
        [4,      1.3,    0.0,       1.5,      1.5,       16]
    ])

    wind_output = np.array([
        [
            [1452, 1452, 1099, 1213, 939,  553,  371,  328,  370,  362,  477,  635,
            728,  947,  1236, 1609, 1822, 1739, 1618, 1980, 2111, 1968, 1728, 1500],
            [1502, 1150, 1049, 1263, 989,  503,  421,  278,  420,  312,  527,  585,
            778,  897,  1286, 1559, 1872, 1689, 1668, 1930, 2161, 1918, 1778, 1450],
            [1462, 1210, 1109, 1223, 949,  563,  381,  338,  380,  372,  487,  645,
            738,  957,  1246, 1619, 1832, 1749, 1628, 1990, 2121, 1978, 1738, 1510],
            [1442, 1190, 1089, 1203, 929,  543,  361,  318,  360,  352,  467,  625,
            718,  937,  1226, 1599, 1812, 1729, 1608, 1970, 2101, 1958, 1718, 1490],
            [1442, 1190, 1089, 1203, 929, 543, 361, 318, 360, 352, 467, 625,
             718, 937, 1226, 1599, 1812, 1729, 1608, 1970, 2101, 1958, 1718, 1490]
        ]
    ]) / 1000 * 0.


    # bus
    wind_connection_index = np.array([
        3,
    ])

    # gas generator
    # Bus    P_max    P_min    Ramp up    Ramp down    gas node    efficiency
    gas_generator_power_info = np.array([
        [4,   400,      180,      50,         50,          3,          0.4],
    ])

    power_load_demand_total = np.array([
        2.5, 2.65, 2.05, 2.15, 2.25, 2.55, 2.35,
        2.5,  2.625, 2.825,  3.125,  3.625, 3.4,   3.595, 2.85,  3.075, 3.255, 3.42,  3.54,
        3.63,   3.645, 3.72,  3.825, 3.84,  3.69,  3.675, 3.555, 3.555, 3.405, 3.015, 2.94, ])   *  0.5

    # Bus / total
    power_load_info = np.array([
        [1, 0.5],
        [2, 0.3],
        [3, 0.2],
    ])

    # Beginning node   Terminal node   Impedance   Line Capacity
    power_line_info = np.array([
        [0,                   1,         0.0281,         12.9],
        [0,                   3,         0.0304,         12.9],
        [0,                   4,         0.0064,         13.9],
        [1,                   2,         0.0108,         12.9],
        [2,                   3,         0.0297,         14.1],
        [3,                   4,         0.0297,         12.0],
    ])

    ##       0       1d       2d
    #        o--------o--------o
    #        | \_____________  |
    #      4 |               \ |
    #        o--------------- o 3d
    # #


    ## 只有 上层 一个chp机组啊
    upper_chp_info = np.array([
        # a0   p1        a1 p2       a2  h1         a3  h2       a4 cross        a5 const             heater     bid_power      bid_heat
        [
          20 * 0.6,    0 * 0.06,   1.5 * 0.6,      .0 * 0.6,    0. * 0.6,      0.0 * 0.6,           0,          20,              10
        ],
        [
            20 * 0.6,   0 * 0.06,   1.5 * 0.6,      .0 * 0.6,    0. * 0.6,     0.0 * 0.6,            0,          20,              10
        ],
        [
            20 * 0.6,   0 * 0.06,   1.5 * 0.6,      .0 * 0.6,    0. * 0.6,     0.0 * 0.6,            0,          20,              10
        ],
        [
            20 * 0.6,   0 * 0.06,   1.5 * 0.6,      .0 * 0.6,    0. * 0.6,     0.0 * 0.6,            0,          20,              10
        ],
    ])

    lower_chp_info = np.array([
        [
            2 * 0.6,   0 * 0.06,     1. * 3.6,   .0 * 0.6,    0. * 0.6,      0.0 * 0.6,            0
        ],
        [
            2 * 0.6,   0 * 0.06,     1. * 2.6,   .0 * 0.6,    0. * 0.6,      0.0 * 0.6,            0
         ],
        [
            2 * 0.6,   0 * 0.06,     1. * 1.6,   .0 * 0.6,    0. * 0.6,      0.0 * 0.6,            0
        ],
        [
            2 * 0.6,   0 * 0.06,     1. * 0.6,   .0 * 0.6,    0. * 0.6,      0.0 * 0.6,            0
        ],
    ])

    upper_chp_POWER = np.array([
        [0.81 * 1,     2.97 * 1,    2.55 * 1,       0],
        [0.81 * 1,     2.97 * 1,    2.55 * 1,       0],
        [0.81 * 1,     2.97 * 1,    2.55 * 1,       0],
        [0.81 * 1,     2.97 * 1,    2.55 * 1,       0],
    ])

    upper_chp_HEAT = np.array([
        [0.528 * 1,     0.8 * 1,       0.45 * 1,     0 * 1],
        [0.328 * 1,     0.3 * 1,       0.35 * 1,     0 * 1],
        [0.428 * 0,     0.4 * 0,       0.45 * 0,     0 * 1],
        [0.228 * 0,     0.2 * 0,       0.045 * 0,     0 * 0],
    ])*1

    lower_chp_POWER = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])

    lower_chp_HEAT = np.array([
        [0.3*1,      0.2*1,      0.1*1,       0.0],
        [0.1*1,      0.5*1,      0.3*1,       0.0],
        [0.3*1,      0.2*1,      0.1*1,       0.0],
        [0.3*1,      0.2*1,      0.1*1,       0.0],
    ])
    upper_chp_power_index = np.array([
        2, 2, 2, 2,
    ])

    lower_chp_power_index = np.array([
        2, 2, 2, 2,
    ])

    chp_upper_connection_gas_index = np.array([
        1, 3, 3, 3
    ])
    chp_lower_connection_gas_index = np.array([
        5, 5, 5, 5
    ])

    lower_chp_connection_well_index = np.array([
        0, 0, 0, 0
    ])
    upper_chp_connection_well_index = np.array([
        0, 0, 0, 0
    ])

    heat_network_supply = np.array([
        # Beginning node Terminal node length(m)    flow(kg / h)
        [        0,              1,     3500,      1   ],
        [        1,              2,     1750,      0.8 ],
        [        2,              3,     1750,      0.4 ],
        [        1,              4,     1750,      0.2 ],
        [        2,              5,     750,       0.4 ],
    ])
    heat_network_return = np.array([
        # Beginning node Terminal node length(m)    flow(kg / h)
        [        1,              0,     3500,      1   ],
        [        2,              1,     1750,      0.8 ],
        [        3,              2,     1750,      0.4 ],
        [        4,              1,     1750,      0.2 ],
        [        5,              2,     750,       0.4 ],
    ])
    ##    0    10    1      8     2      4     3
    #     o----------o------------o------------o
    #                |         4  |
    #              2 |            |
    #             4  o         5  o
    ##

    heat_network_node = np.array([
    #   node      Tsmin       Tsmax       Trmin     Trmax
        [0,        0 ,         100,        0,       100],
        [1,        0,          100,        0,       100],
        [2,        0,          100,        0,       100],
        [3,        0,          100,        0,       100],
        [4,        0,          100,        0,       100],
        [5,        0,          100,        0,       100],
    ])



    #     Node     load demand(MW)
    exchanger_info = np.array([
          [3,        1 / 3,   ],
          [4,        1 / 3,   ],
          [5,        1 / 3,   ],
    ])

    #  node    flow
    heater_info = np.array([
        [0],
    ])

    heat_load = np.array([[
        49,          50,          52,     47.8,     48,      49,      48.06451613,
        47.09677419,
        45.16129032, 44.19354839, 43.22580645, 42.25806452, 41.29032258, 41.29032258, 41.29032258, 42.25806452,
        43.22580645, 44.19354839, 44.19354839, 44.19354839, 45.16129032, 46.12903226, 47.09677419, 47.09677419],
    ]) / 50



    # use config 6 - gas - node
    # #  0L             1LL            2            3           4W(L)
    #    o ------------ o ------------ o ---------- o ------------- o
    #                                               |
    #                                               |
    #                                               o
    # #                                             5W(U) CHP CHP
    upper_well_info = np.array([
    #  node    max(Sm3/h)      min(Sm3/h)     cost($/Sm3)    quoted_max($/Sm3)
        [5,       33.36,             0,            2.2,             4.4],
    ])
    lower_well_info = np.array([
        [4,       0.0,             0,            2.8 ],
    ])




    gas_pipe_line_info = np.array([
    #  start     end       weymouth     linepack   index   is_active   flow_min   flow_max
        [5,       3,        0.193/0.193,       0.0,     0,       0,           0,        20 ],
        [4,       3,        0.193/0.193,       0.0,     1,       0,           0,        20 ],
        [3,       2,        0.193/0.193,       0.0,     2,       0,           0,        20 ],
        [2,       1,        0.193/0.193,       0.0,     3,       0,           0,        20 ],
        [1,       0,        0.193/0.193,       0.0,     4,       0,           0,        20 ],
    ])

    gas_node_info = np.array([
    #   Node     MaxPressure(bar)   MinPressure(bar)
        [0,           8.28 * 10,           7.34 * 0 ],
        [1,           8.28 * 10,           7.34 * 0 ],
        [2,           8.28 * 10,           7.34 * 0 ],
        [3,           8.28 * 10,           7.34 * 0 ],
        [4,           8.28 * 10,           7.34 * 0 ],
        [5,           8.28 * 10,           7.34 * 0 ],
    ])

    compressor_info = np.array([
    #  start         end           CompFact
    #    [2,           1,              2 ],
    ])

    gas_load_total = np.array([
         1,   1.1,  1.15, 1.2, 1.25, 1.15, 1.1,  1,   0.95, 0.9, 0.88, 0.85,
         0.9, 0.95, 0.99, 1,   1.1,  1.05, 1.05, 1.1, 1.15, 1.1, 1,    0.95
    ]) * 1

    gas_load_info = np.array([
    #   node     percent
        [0,      0.5],
        [1,      0.2],
        [2,      0.3],
    ])



    power_system = {
        'node_num': int(np.max([np.max(power_line_info[:, 0]), np.max(power_line_info[:, 1])])) + 1,
        'line_num': len(power_line_info),
        'line_capacity': power_line_info[:, 3].tolist(),
        'reactance': power_line_info[:, 2].tolist(),
        'line_start': power_line_info[:, 0].astype(np.int),
        'line_end': power_line_info[:, 1].astype(np.int),

        'upper_generator_connection_index': upper_generator_info[:, 0].astype(np.int),
        'upper_generator_num': len(upper_generator_info),
        'upper_generator_max': upper_generator_info[:, 1].tolist(),
        'upper_generator_min': upper_generator_info[:, 2].tolist(),
        'upper_generator_ramp_up': upper_generator_info[:, 3].tolist(),
        'upper_generator_ramp_down': upper_generator_info[:, 4].tolist(),
        'upper_generator_cost': upper_generator_info[:, 5].tolist(),
        'upper_generator_quoted_price_max': [[bid] * T for bid in upper_generator_info[:, 6]],    # its shape is => (generator, T)

        'lower_generator_connection_index': lower_generator_info[:, 0].astype(np.int),
        'lower_generator_num': len(lower_generator_info),
        'lower_generator_max': lower_generator_info[:, 1].tolist(),
        'lower_generator_min': lower_generator_info[:, 2].tolist(),
        'lower_generator_ramp_up': lower_generator_info[:, 3].tolist(),
        'lower_generator_ramp_down': lower_generator_info[:, 4].tolist(),
        'lower_generator_cost': lower_generator_info[:, 5].tolist(),

        'load_num': len(power_load_info),
        'load_index': power_load_info[:, 0].astype(np.int),
        'load': (power_load_info[:, 1].reshape((-1, 1)).dot(power_load_demand_total.reshape((1, -1)))),

        'wind_connection_index': wind_connection_index.astype(np.int),
        'wind_output': wind_output,
        'wind_farm_num': len(wind_connection_index)
    }
    heat_system = {
        'node_num': len(heat_network_node),
        'pipe_num': len(heat_network_supply),
        'heat_pipe_length': heat_network_supply[:, 2].tolist(),
        'heat_pipe_start_node_supply': heat_network_supply[:, 0].astype(np.int64),
        'heat_pipe_end_node_supply': heat_network_supply[:, 1].astype(np.int64),
        'heat_pipe_start_node_return': heat_network_return[:, 0].astype(np.int64),
        'heat_pipe_end_node_return': heat_network_return[:, 1].astype(np.int64),
        'line_water_flow': heat_network_supply[:, 3],

        'heater_num': len(heater_info),
        'exchanger_num': len(exchanger_info),
        'upper_chp_connection_heater_index': upper_chp_info[:, 6].astype(np.int),
        'lower_chp_connection_heater_index': lower_chp_info[:, 6].astype(np.int),
        'heater_connection_index': heater_info[:, 0].astype(np.int64),
        'exchanger_connection_index': exchanger_info[:, 0].astype(np.int64),
        'heater_tempe_supply_min': heat_network_node[heater_info[:, 0].astype(np.int), 1].tolist(),
        'heater_tempe_supply_max': heat_network_node[heater_info[:, 0].astype(np.int), 2].tolist(),
        'heater_tempe_return_min': heat_network_node[heater_info[:, 0].astype(np.int), 3].tolist(),
        'heater_tempe_return_max': heat_network_node[heater_info[:, 0].astype(np.int), 4].tolist(),
        'exchanger_tempe_supply_min': heat_network_node[exchanger_info[:, 0].astype(np.int), 1].tolist(),
        'exchanger_tempe_supply_max': heat_network_node[exchanger_info[:, 0].astype(np.int), 2].tolist(),
        'exchanger_tempe_return_min': heat_network_node[exchanger_info[:, 0].astype(np.int), 3].tolist(),
        'exchanger_tempe_return_max': heat_network_node[exchanger_info[:, 0].astype(np.int), 4].tolist(),

        'load' : exchanger_info[:, 1].reshape((-1, 1)).dot(heat_load.reshape((1, -1))),

        'chp_upper_connection_power_index': upper_chp_power_index.astype(np.int),
        'chp_lower_connection_power_index': lower_chp_power_index.astype(np.int),
    }

    chp_system = {
        'chp_upper_num': len(upper_chp_info),
        'chp_lower_num': len(lower_chp_info),
        'chp_point_num': len(upper_chp_POWER[0]),
        'upper_chp_power_quoted_price_max': [[bid] * T for bid in upper_chp_info[:, 7]],  # its shape is (chp, T)
        'upper_chp_heat_quoted_price_max': [[bid] * T for bid in upper_chp_info[:,  8]],   # its shape is (chp, T)
        'upper_chp_POWER': upper_chp_POWER,
        'upper_chp_HEAT': upper_chp_HEAT,
        'lower_chp_POWER': lower_chp_POWER,
        'lower_chp_HEAT': lower_chp_HEAT,



        'chp_upper_coeff_p_1':   upper_chp_info[:, 0],
        'chp_upper_coeff_p_2':   upper_chp_info[:, 1],
        'chp_upper_coeff_h_1':   upper_chp_info[:, 2],
        'chp_upper_coeff_h_2':   upper_chp_info[:, 3],
        'chp_upper_coeff_cross': upper_chp_info[:, 4],
        'chp_upper_coeff_const': upper_chp_info[:, 5],
        'chp_lower_coeff_p_1':   lower_chp_info[:, 0],
        'chp_lower_coeff_p_2':   lower_chp_info[:, 1],
        'chp_lower_coeff_h_1':   lower_chp_info[:, 2],
        'chp_lower_coeff_h_2':   lower_chp_info[:, 3],
        'chp_lower_coeff_cross': lower_chp_info[:, 4],
        'chp_lower_coeff_const': lower_chp_info[:, 5],
    }
    gas_system = {
        'well_upper_num': len(upper_well_info),
        'well_lower_num': len(lower_well_info),
        'well_upper_quoted_price_max': upper_well_info[:, 4],
        'well_upper_connection_index': upper_well_info[:, 0].astype(np.int),
        'well_lower_connection_index': lower_well_info[:, 0].astype(np.int),

        'well_upper_output_price': upper_well_info[:, 3],
        'well_lower_output_price': lower_well_info[:, 3],
        'well_upper_output_max': upper_well_info[:, 1],
        'well_upper_output_min': upper_well_info[:, 2],
        'well_lower_output_max': lower_well_info[:, 1],
        'well_lower_output_min': lower_well_info[:, 2],

        'gas_node_num': len(gas_node_info),
        'gas_node_pressure_max': gas_node_info[:, 1],
        'gas_node_pressure_min': gas_node_info[:, 2],

        'gas_line_num': len(gas_pipe_line_info),
        'gas_inactive_line_num': len(gas_pipe_line_info) - len(compressor_info),
        'gas_active_line_num': len(compressor_info),
        'gas_active_line': (gas_pipe_line_info[np.where(gas_pipe_line_info[:, 5] == 1), 4][0]).astype(np.int),
        'gas_inactive_line': (gas_pipe_line_info[np.where(gas_pipe_line_info[:, 5] != 1), 4][0]).astype(np.int),

        'gas_flow_in_min' : gas_pipe_line_info[:, 6],
        'gas_flow_in_max' : gas_pipe_line_info[:, 7],
        'gas_flow_out_min': gas_pipe_line_info[:, 6],
        'gas_flow_out_max': gas_pipe_line_info[:, 7],

        'weymouth': gas_pipe_line_info[:, 2],
        'gas_linepack_coeff': gas_pipe_line_info[:, 3],
        'gas_pipe_start_node': gas_pipe_line_info[:, 0].astype(np.int),
        'gas_pipe_end_node': gas_pipe_line_info[:, 1].astype(np.int),

        'gas_compressor_num': len(compressor_info),
        'gas_compressor_coeff': [],#compressor_info[:, 2],

        'gas_load_num': len(gas_load_info),
        'gas_load': gas_load_info[:, 1].reshape((-1, 1)).dot(gas_load_total.reshape((1, -1))),
        'gas_load_connection_index': gas_load_info[:, 0].astype(np.int),
        'chp_upper_connection_gas_index': chp_upper_connection_gas_index.astype(np.int),
        'chp_lower_connection_gas_index': chp_lower_connection_gas_index.astype(np.int),
        'lower_chp_connection_well_index': lower_chp_connection_well_index,
        'upper_chp_connection_well_index': upper_chp_connection_well_index,
    }
    return power_system, heat_system, chp_system, gas_system
