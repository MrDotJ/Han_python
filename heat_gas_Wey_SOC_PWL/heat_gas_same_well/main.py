from typing import List

from numpy.core._multiarray_umath import ndarray

from first_stage_heat_gas_pccp_PWL_total_capacity import OneLayer
from second_stage import SecondLayer
from resource.config4_with_gas import get_config, empirical_distribution, confidence_level
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


    second_layer.bulid_base_model()

    distribution = empirical_distribution
    alpha = 0.6

    linearization_point: List[ndarray] = [np.zeros((5, 5, 5)), np.zeros((5, 5, 5)), np.zeros((5, 5, 5)), np.zeros((5, 5, 5))]
    linearization_point: List[ndarray] = [np.ones((5, 5, 5)), np.ones((5, 5, 5)), np.ones((5, 5, 5)), np.ones((5, 5, 5))]
    obj_k = 'suppress a warning'
    PUNISH = 2

    for _ in range(1): # CCG layer
        print('===>first stage')
        penalty = 0
        for index in range(1):   # PCCP layer
            # 2. update pccp-related objective and constraints
            first_layer.update_gas_system_pccp_original_and_dual_constraints(linearization_point[1], linearization_point[2], linearization_point[3])
            # 3. establish kkt derivation constraints
            first_layer.build_kkt_derivative_constraints(penalty)
            # 4. save old information and update penalty
            linearization_point_old = deepcopy(linearization_point[1:])
            penalty = penalty * PUNISH if index > 0 else 0
            # 5. optimize the model
            # [generator, chp_power, chp_heat], [revenue_1, ..., revenue_k], [pressure_end, flow_in, flow_out]
            first_layer.build_upper_objective()
            quoted_price, obj_k, linearization_point, pccp, weymouth_left, weymouth_right = first_layer.optimize(distribution)

            print('         ===>PCCP: norm linearization point : ' + str(np.linalg.norm(np.vstack(linearization_point_old) - np.vstack(linearization_point[1:]))))
            print('             ===>1. linearization point pressure start: ' + str(linearization_point[0].flatten()))
            print('             ===>2. linearization point pressure end  : ' + str(linearization_point[1].flatten()))
            print('             ===>3. linearization point flow in       : ' + str(linearization_point[2].flatten()))
            print('             ===>4. linearization point flow out      : ' + str(linearization_point[3].flatten()))
            print('             ===>5. pccp                              : ' + str(pccp.flatten()))
            print('             ===>6. weymouth_left                     : ' + str(weymouth_left.flatten()))
            print('             ===>7. weymouth_right                    : ' + str(weymouth_right.flatten()))
            print('             ===>8. revenue                           : ' + str(obj_k))
        worst_distribution = second_layer.optimize(obj_k)
        distribution = alpha * np.array(distribution) + (1 - alpha) * np.array(worst_distribution)
        print('===>second stage')
        print('         ===>CCG: norm distribution : ' + str(np.linalg.norm(worst_distribution - distribution)))
        print('             ===>1. worst distribution  : ' + str(distribution))


if __name__ == '__main__':
    power_system_info, heat_system_info, chp_system_info, gas_system_info = get_config()
    first_layer = OneLayer(power_system_info, heat_system_info, chp_system_info, gas_system_info)
    second_layer = SecondLayer(empirical_distribution, confidence_level)
    do_main()
