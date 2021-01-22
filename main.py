from model_only_gas_system import OneLayer
from second_stage import SecondLayer
from config3_with_gas import get_config, empirical_distribution, confidence_level
import numpy as np


def do_main():
    first_layer.build_power_system()
    first_layer.build_heat_system()
    first_layer.build_gas_system()

    first_layer.build_power_system_original_and_dual_constraints()
    first_layer.build_gas_system_original_and_dual_constrains()
    first_layer.build_heat_system_original_and_dual_constraints()

    first_layer.build_lower_objective()
    first_layer.build_kkt_derivative_constraints()

    first_layer.build_upper_constraints()
    first_layer.build_upper_objective()

    second_layer.bulid_base_model()

    distribution = empirical_distribution
    alpha = 0.6
    if 1:
        print('first stage')
        value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price, obj_k = \
            first_layer.optimize(distribution)
        print('second stage')
        worst_distribution = second_layer.optimize(obj_k)
        distribution = alpha * np.array(distribution) + (1 - alpha) * np.array(worst_distribution)


if __name__ == '__main__':
    power_system_info, heat_system_info, chp_system_info, gas_system_info = get_config()
    first_layer = OneLayer(power_system_info, heat_system_info, chp_system_info, gas_system_info)
    second_layer = SecondLayer(empirical_distribution, confidence_level)
    do_main()
