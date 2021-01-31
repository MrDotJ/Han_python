from typing import List

from numpy.core._multiarray_umath import ndarray

from model_with_gas_new import OneLayer
from second_stage import SecondLayer
from config3_with_gas import get_config, empirical_distribution, confidence_level
import numpy as np
from copy import deepcopy


def do_main():
    # build basic P_H_G system
    first_layer.build_power_system()
    first_layer.build_heat_system()
    first_layer.build_gas_system()
    first_layer.build_power_system_original_and_dual_constraints()
    first_layer.build_gas_system_original_and_dual_constrains()
    first_layer.build_heat_system_original_and_dual_constraints()

    # build upper bid price constraints
    first_layer.build_upper_constraints()

    # establish KKT derivation constraints
    # 1. build lower objective
    first_layer.build_lower_objective()
    first_layer.build_upper_objective()

    second_layer.bulid_base_model()

    distribution = empirical_distribution
    alpha = 0.6

    linearization_point: List[ndarray] = [np.ones((3, 1, 1)), np.ones((3, 1, 1)), np.ones((3, 1, 1))]
    obj_k = 'suppress a warning'

    for _ in range(3): # CCG layer
        print('===>first stage')
        for _ in range(3):   # PCCP layer
            # 2. update pccp-related objective and constraints
            first_layer.update_gas_system_pccp_original_and_dual_constraints(*linearization_point)
            # 3. establish kkt derivation constraints
            first_layer.build_kkt_derivative_constraints()
            # 4. save old information
            linearization_point_old = deepcopy(linearization_point)
            # 5. optimize the model
            # [generator, chp_power, chp_heat], [revenue_1, ..., revenue_k], [pressure_end, flow_in, flow_out]
            quoted_price, obj_k, linearization_point = first_layer.optimize(distribution)

            print('         ===>norm linearization point: ' + str(np.linalg.norm([np.vstack(linearization_point_old), np.vstack(linearization_point)])))
            print('         ===>revenue: ' + str(obj_k))
        worst_distribution = second_layer.optimize(obj_k)
        distribution = alpha * np.array(distribution) + (1 - alpha) * np.array(worst_distribution)
        print('===>second stage')
        print('         ===>norm distribution: ' + str(np.linalg.norm([worst_distribution, distribution])))


if __name__ == '__main__':
    power_system_info, heat_system_info, chp_system_info, gas_system_info = get_config()
    first_layer = OneLayer(power_system_info, heat_system_info, chp_system_info, gas_system_info)
    second_layer = SecondLayer(empirical_distribution, confidence_level)
    do_main()
