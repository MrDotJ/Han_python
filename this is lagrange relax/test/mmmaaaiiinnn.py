from resource.config4_with_gas import get_config
from give_bid_price_cal_original_problem import OneLayer1
from fix_binary_variable_derive_kkt import OneLayer2
import numpy as np

if __name__ == '__main__':
    value_chp_heat_quoted_price = np.ones((10, 10)) * 2
    value_well_quoted_price = np.ones((10, 10)) * 2
    segment_num = 8
    for i in range(10):
        print('-----------------------------------------------------------')
        segment_num = int(segment_num * 1)
        print(str(i) + 'th iteration, ' + 'segment number : ' + str(segment_num))
        power_system_info, heat_system_info, chp_system_info, gas_system_info = get_config()
        one1 = OneLayer1(power_system_info, heat_system_info, chp_system_info, gas_system_info, segment_num)
        one1.build_power_system()
        one1.build_gas_system()
        one1.build_heat_system()
        one1.build_power_system_original_and_dual_constraints()
        one1.build_heat_system_original_and_dual_constraints()
        one1.build_gas_system_original_and_dual_constrains()
        one1.build_lower_objective(value_chp_heat_quoted_price, value_well_quoted_price)
        bin1, bin2 = one1.optimize()
        # print(np.where(bin1[0].reshape(-1) == 1))
        # print(np.where(bin1[1].reshape(-1) == 1))
        # print(np.where(bin1[2].reshape(-1) == 1))
        # print(np.where(bin1[3].reshape(-1) == 1))
        # print(np.where(bin1[4].reshape(-1) == 1))
        # print(np.where(bin2[0].reshape(-1) == 1))


        one2 = OneLayer2(power_system_info, heat_system_info, chp_system_info, gas_system_info, segment_num)
        one2.build_power_system()
        one2.build_gas_system()
        one2.build_heat_system()
        one2.build_power_system_original_and_dual_constraints()
        one2.build_heat_system_original_and_dual_constraints()
        one2.build_gas_system_original_and_dual_constrains(bin1, bin2)
        one2.build_lower_objective()
        one2.build_kkt_derivative_constraints()
        one2.build_upper_constraints()
        one2.build_upper_objective()
        d = one2.optimize([1])
        bid = d[0]
        value_generator_quoted_price, value_chp_power_quoted_price, value_chp_heat_quoted_price, value_well_quoted_price = \
            bid[0].astype(np.float), bid[1].astype(np.float), bid[2].astype(np.float), bid[3].astype(np.float)
        print(value_well_quoted_price.reshape((1, -1)))

        # print(value_chp_heat_quoted_price.reshape((1, -1)))