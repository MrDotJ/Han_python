import numpy as np
T = 5


def get_config():
    #   Bus     P_max   P_min   Ramp_up   Ramp_down   Cost    bid_max
    upper_generator_info = np.array([
        [0,      1100,   0,       1800,     1800,      10,         20],
        [3,      300,    0,       50,       50,        17,         34],
        [2,      400,    180,     50,       50,        10,         20],
        [4,      400,    180,     50,       50,        10,         20]
    ])

    lower_generator_info = np.array([
        [0,      600,    0,       180,      180,       16],
        [3,      400,    0,       150,      150,       18],
        [4,      400,    10,      150,      150,       11]
    ])

    # bus / capacity
    wind_connection_index = np.array([
        3,
    ])

    wind_output = np.array([
        [1452, 1600, 1099, 1213, 939, 553, 371, 328, 370, 362, 477, 635, 728, 947, 1236, 1609, 1822, 1739, 1618, 1980, 2111,
         1968, 1728, 1500],
        [1502, 1150, 1049, 1263, 989, 503, 421, 278, 420, 312, 527, 585, 778, 897, 1286, 1559, 1872, 1689, 1668, 1930, 2161,
         1918, 1778, 1450],
        [1462, 1210, 1109, 1223, 949, 563, 381, 338, 380, 372, 487, 645, 738, 957, 1246, 1619, 1832, 1749, 1628, 1990, 2121,
         1978, 1738, 1510],
        [1442, 1190, 1089, 1203, 929, 543, 361, 318, 360, 352, 467, 625, 718, 937, 1226, 1599, 1812, 1729, 1608, 1970, 2101,
         1958, 1718, 1490]
    ])





    # gas generator
    # Bus    P_max    P_min    Ramp up    Ramp down    gas node    efficiency
    gas_generator_power_info = np.array([
        [4,   400,      180,      50,         50,          3,          0.4],
    ])

    power_load_demand_total = np.array([175, 135, 158, 154, 155, 160, 173, 190, 205, 217, 228, 236, 242, 243, 248, 255, 256, 246, 245, 237, 237, 227, 201, 196])

    # Bus / total
    power_load_info = np.array([
        [1, 550],
        [2, 450],
        [3, 350],
    ])

    # Beginning node   Terminal node   Impedance   Line Capacity
    power_line_info = np.array([
        [0,                   1,         0.0281,         200],
        [0,                   3,         0.0304,         290],
        [0,                   4,         0.0064,         190],
        [1,                   2,         0.0108,         290],
        [2,                   3,         0.0297,         410],
        [3,                   4,         0.0297,         200],
    ])

    ##       0         1       2
    #        o--------o--------o
    #        | \_____________  |
    #      4 |               \ |
    #        o--------------- o 3
    # #

    power_system = {
        'node_num': int(np.max([np.max(power_line_info[:, 0]), np.max(power_line_info[:, 1])])),
        'line_num': len(power_line_info),
        'line_capacity': power_line_info[:, 3].tolist(),
        'reactance': power_line_info[:, 2].tolist(),
        'line_start': power_line_info[:, 0],
        'line_end': power_line_info[:, 1],

        'upper_generator_connection_index': upper_generator_info[:, 0],
        'upper_generator_num': len(upper_generator_info),
        'upper_generator_max': upper_generator_info[:, 1].tolist(),
        'upper_generator_min': upper_generator_info[:, 2].tolist(),
        'upper_generator_ramp_up': upper_generator_info[:, 3].tolist(),
        'upper_generator_ramp_down': upper_generator_info[:, 4].tolist(),
        'upper_generator_cost': upper_generator_info[:, 5].tolist(),
        'upper_generator_quoted_price_max': [[bid] * T for bid in upper_generator_info[:, 6]],    # its shape is => (generator, T)

        'lower_generator_connection_index': lower_generator_info[:, 0],
        'lower_generator_num': len(lower_generator_info),
        'lower_generator_max': lower_generator_info[:, 1].tolist(),
        'lower_generator_min': lower_generator_info[:, 2].tolist(),
        'lower_generator_ramp_up': lower_generator_info[:, 3].tolist(),
        'lower_generator_ramp_down': lower_generator_info[:, 4].tolist(),
        'lower_generator_cost': lower_generator_info[:, 5].tolist(),

        'load_num': len(power_load_info),
        'load_index': power_load_info[:, 0],
        'load': (power_load_info[:, 1].reshape((-1, 1)).dot(power_load_demand_total.reshape((1, -1)))),

        'wind_connection_index': wind_connection_index,
        'wind_output': wind_output
    }




    upper_chp_info = np.array([
        # node         Hmin(MW)      Hmax(MW)       efficiency    Gen              Cost($ / MW)    Tsmin         Tsmax
        # a0           a1            a2             a3            a4               a5              Ramp down      Ramp up    heater     bid_power      bid_heat
        [ 1,           0.00,         100,           1,            3,               100,            110,           120,
          2650 * 0.6,  14.5 * 0.6,   0.0345 * 0.6,  4.2 * 0.6,    0.03 * 0.6,      0.031 * 0.6,    50 * 0.6,      50 * 0.6,    0,          1,              1],
        [ 1,           0.00,         100,           1,            3,               100,            110,           120,
          10 / 1e3,    14.5 / 1e3,   0.0345 / 1e3,  4.2 / 1e4,    0.027 / 1e4,     0.021 / 1e4,    500,           500,         0,          1,              1]
    ])

    lower_chp_info = np.array([
        [1,            0.00,         100,           1,            3,               100,            110,           120,
         15,           36,           0.0435,        6,            0.03,            0.031,          50,            50,        0],
    ])

    upper_chp_power_index = np.array([
        2
    ])

    lower_chp_power_index = np.array([
        3
    ])

    #    P      H
    upper_chp_POWER = np.array([
        [81,     98.8,  255,   297],
        [81,     98.8,  255,   297]
    ])

    upper_chp_HEAT = np.array([
        [52.8,   0,     45,    0],
        [52.8,   0,     45,    0]
    ])

    lower_chp_POWER = np.array([
        [247,  215,   81,    98.8],
        [247,  215,   81,    98.8]
    ])

    lower_chp_HEAT = np.array([
        [ 0,   180,   104.8,    0],
        [0,    180,   104.8,    0]
    ])
    heat_network_supply = np.array([
        # Beginning node Terminal node length(m) diameter(m) roughness conductivity Mmin(Kg / h) Mmax(Kg / h) flow(kg / h)
        [        0,              1,     3500,     0.8,        0.0005,     0.12,     1e5,             1e7,      450 * 1e3     ],
        [        1,              2,     1750,     0.8,        0.0005,     0.12,     1e5,             1e7,      408.716 * 1e3 ],
        [        2,              3,     1750,     0.8,        0.0005,     0.12,     1e5,             1e7,      243.578 * 1e3 ],
        [        1,              4,     1750,     0.8,        0.0005,     0.12,     1e5,             1e7,      41.284 * 1e3  ],
        [        2,              5,     750,      0.8,        0.0005,     0.12,     1e5,             1e7,      165.138 * 1e3 ],
    ])
    heat_network_return = np.array([
        # Beginning node Terminal node length(m) diameter(m) roughness conductivity Mmin(Kg / h) Mmax(Kg / h) flow(kg / h)
        [        1,              0,     3500,     0.8,        0.0005,     0.12,     1e5,             1e7,      450 * 1e3     ],
        [        2,              1,     1750,     0.8,        0.0005,     0.12,     1e5,             1e7,      408.716 * 1e3 ],
        [        3,              2,     1750,     0.8,        0.0005,     0.12,     1e5,             1e7,      243.578 * 1e3 ],
        [        4,              1,     1750,     0.8,        0.0005,     0.12,     1e5,             1e7,      41.284 * 1e3  ],
        [        5,              2,     750,      0.8,        0.0005,     0.12,     1e5,             1e7,      165.138 * 1e3 ],
    ])
    ##    0    10    1      8     2      4     3
    #     o----------o------------o------------o
    #                |         4  |
    #              2 |            |
    #             4  o         5  o
    ##
    heat_network_node = np.array([
    #   node      Tsmin       Tsmax       Trmin     Trmax
        [0,        110 ,       120,        60,       80],
        [1,        110,        120,        60,       80],
        [2,        110,        120,        60,       80],
        [3,        110,        120,        60,       80],
        [4,        110,        120,        60,       80],
        [5,        110,        120,        60,       80],
    ])



    #     Node     load demand(MW)     flow(kg / h)
    exchanger_info = np.array([
          [3,        47.2 / 3,         243.578 * 1e3],
          [4,        8 / 3   ,         41.284  * 1e3 ],
          [5,        32 / 3  ,         165.138 * 1e3],
    ])

    #  node    flow
    heater_info = np.array([
        [0,   450 * 1e3],
    ])

    heat_load = np.array([
        50, 50, 48.06451613, 49.03225806, 49.03225806, 49.03225806, 48.06451613, 47.09677419, 45.16129032, 44.19354839,
        43.22580645, 42.25806452, 41.29032258, 41.29032258, 41.29032258, 42.25806452, 43.22580645, 44.19354839, 44.19354839, 44.19354839, 45.16129032,
        46.12903226, 47.09677419, 47.09677419])

    Heat_load_T0 = np.array([-10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10, -10,
                    -10, -10, -10])

    Water_capacity = 4.2
    Water_density = 1e3


    heat_system = {
        'node_num': len(heat_network_node),
        'pipe_num': len(heat_network_supply),
        'heat_pipe_length': heat_network_supply[:, 2].tolist(),
        'heat_pipe_start_node_supply': heat_network_supply[:, 0].astype(np.int64),
        'heat_pipe_end_node_supply': heat_network_supply[:, 1].astype(np.int64),
        'heat_pipe_start_node_return': heat_network_return[:, 0].astype(np.int64),
        'heat_pipe_end_node_return': heat_network_return[:, 1].astype(np.int64),
        'line_water_flow': heat_network_supply[:, 8],

        'heater_num': len(heater_info),
        'exchanger_num': len(exchanger_info),
        'upper_chp_connection_heater_index': upper_chp_info[:, 16],
        'lower_chp_connection_heater_index': lower_chp_info[:, 16],
        'heater_connection_index': heater_info[:, 0].astype(np.int64),
        'exchanger_connection_index': exchanger_info[:, 0].astype(np.int64),
        'heater_tempe_supply_max': heat_network_node[heater_info[:, 0].astype(np.int), 1].tolist(),
        'heater_tempe_supply_min': heat_network_node[heater_info[:, 0].astype(np.int), 2].tolist(),
        'heater_tempe_return_max': heat_network_node[heater_info[:, 0].astype(np.int), 3].tolist(),
        'heater_tempe_return_min': heat_network_node[heater_info[:, 0].astype(np.int), 4].tolist(),
        'exchanger_tempe_supply_max': heat_network_node[exchanger_info[:, 0].astype(np.int), 1].tolist(),
        'exchanger_tempe_supply_min': heat_network_node[exchanger_info[:, 0].astype(np.int), 2].tolist(),
        'exchanger_tempe_return_max': heat_network_node[exchanger_info[:, 0].astype(np.int), 3].tolist(),
        'exchanger_tempe_return_min': heat_network_node[exchanger_info[:, 0].astype(np.int), 4].tolist(),

        'load' : exchanger_info[:, 1].reshape((-1, 1)).dot(heat_load.reshape((1, -1))),

        'chp_upper_connection_power_index': upper_chp_power_index,
        'chp_lower_connection_power_index': lower_chp_power_index,
    }

    chp_system = {
        'chp_upper_num': len(upper_chp_info),
        'chp_lower_num': len(lower_chp_info),
        'chp_point_num': len(upper_chp_POWER[0]),
        'upper_chp_power_quoted_price_max': [[bid] * T for bid in upper_chp_info[:, 17]],  # its shape is (chp, T)
        'upper_chp_heat_quoted_price_max': [[bid] * T for bid in upper_chp_info[:, 18]],   # its shape is (chp, T)
        'upper_chp_POWER': upper_chp_POWER,
        'upper_chp_HEAT': upper_chp_HEAT,
        'lower_chp_POWER': lower_chp_POWER,
        'lower_chp_HEAT': lower_chp_HEAT,



        'chp_upper_coeff_p_1':   upper_chp_info[:, 8].tolist(),
        'chp_upper_coeff_p_2':   upper_chp_info[:, 9].tolist(),
        'chp_upper_coeff_h_1':   upper_chp_info[:, 10].tolist(),
        'chp_upper_coeff_h_2':   upper_chp_info[:, 11].tolist(),
        'chp_upper_coeff_cross': upper_chp_info[:, 12].tolist(),
        'chp_upper_coeff_const': upper_chp_info[:, 13].tolist(),
        'chp_lower_coeff_p_1':   upper_chp_info[:, 8].tolist(),
        'chp_lower_coeff_p_2':   upper_chp_info[:, 9].tolist(),
        'chp_lower_coeff_h_1':   upper_chp_info[:, 10].tolist(),
        'chp_lower_coeff_h_2':   upper_chp_info[:, 11].tolist(),
        'chp_lower_coeff_cross': upper_chp_info[:, 12].tolist(),
        'chp_lower_coeff_const': upper_chp_info[:, 13].tolist(),
    }

    return power_system, heat_system, chp_system
