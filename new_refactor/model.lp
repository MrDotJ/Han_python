\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 weymouth_left_aux[0,0,0] + 0 weymouth_left_aux[1,0,0]
   + 0 weymouth_left_aux[2,0,0] + 0 weymouth_left_aux[3,0,0]
   + 0 weymouth_left_aux[4,0,0] + 0 weymouth_right_aux1[0,0,0]
   + 0 weymouth_right_aux1[1,0,0] + 0 weymouth_right_aux1[2,0,0]
   + 0 weymouth_right_aux1[3,0,0] + 0 weymouth_right_aux1[4,0,0]
   + 0 weymouth_right_aux2[0,0,0] + 0 weymouth_right_aux2[1,0,0]
   + 0 weymouth_right_aux2[2,0,0] + 0 weymouth_right_aux2[3,0,0]
   + 0 weymouth_right_aux2[4,0,0] + 0 pccp_relax[0,0,0]
   + 0 pccp_relax[1,0,0] + 0 pccp_relax[2,0,0] + 0 pccp_relax[3,0,0]
   + 0 pccp_relax[4,0,0] + 0 gas_linepack[0,0,0] + 0 gas_linepack[1,0,0]
   + 0 gas_linepack[2,0,0] + 0 gas_linepack[3,0,0] + 0 gas_linepack[4,0,0]
   + 0 dual_dual_mix_constraints_supply0_0S0
   + 0 dual_dual_mix_constraints_return0_3S0
   + 0 dual_dual_mix_constraints_return0_4S0
   + 0 dual_dual_mix_constraints_return0_5S0
Subject To
 dual_node_gas_balance_time_0_node_0S_0[EqualFeasible]:
   - gas_flow_out[4,0,0] = -0.5
 dual_node_gas_balance_time_0_node_1S_0[EqualFeasible]: gas_flow_in[4,0,0]
   - gas_flow_out[3,0,0] = -0.2
 dual_node_gas_balance_time_0_node_2S_0[EqualFeasible]: gas_flow_in[3,0,0]
   - gas_flow_out[2,0,0] = -0.3
 dual_node_gas_balance_time_0_node_3S_0[EqualFeasible]: gas_flow_in[2,0,0]
   - gas_flow_out[0,0,0] - gas_flow_out[1,0,0] = 0
 dual_node_gas_balance_time_0_node_4S_0[EqualFeasible]:
   0.9 upper_chp_heat_output[0,0,0] - lower_well_output[0,0,0]
   + gas_flow_in[1,0,0] = 0
 dual_node_gas_balance_time_0_node_5S_0[EqualFeasible]:
   0.6 lower_chp_heat_output[0,0,0] - upper_well_output[0,0,0]
   + gas_flow_in[0,0,0] = 0
 original_feasible_dual_upper_well_output_min_0_t_0_S_0:
   upper_well_output[0,0,0] >= 0
 original_feasible_M_dual_upper_well_output_min_0_t_0_S_0:
   upper_well_output[0,0,0]
   - 1e+07 dual_upper_well_output_min_0_t_0_S_0_binary <= 0
 dual_feasible_dual_upper_well_output_min_0_t_0_S_0:
   dual_upper_well_output_min_0_t_0_S_0 >= 0
 dual_feasible_M_dual_upper_well_output_min_0_t_0_S_0:
   dual_upper_well_output_min_0_t_0_S_0
   + 1e+07 dual_upper_well_output_min_0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_upper_well_output_max_0_t_0_S_0:
   - upper_well_output[0,0,0] >= -33.36
 original_feasible_M_dual_upper_well_output_max_0_t_0_S_0:
   - upper_well_output[0,0,0]
   - 1e+07 dual_upper_well_output_max_0_t_0_S_0_binary <= -33.36
 dual_feasible_dual_upper_well_output_max_0_t_0_S_0:
   dual_upper_well_output_max_0_t_0_S_0 >= 0
 dual_feasible_M_dual_upper_well_output_max_0_t_0_S_0:
   dual_upper_well_output_max_0_t_0_S_0
   + 1e+07 dual_upper_well_output_max_0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_lower_well_output_min_0_t_0_S_0:
   lower_well_output[0,0,0] >= 0
 original_feasible_M_dual_lower_well_output_min_0_t_0_S_0:
   lower_well_output[0,0,0]
   - 1e+07 dual_lower_well_output_min_0_t_0_S_0_binary <= 0
 dual_feasible_dual_lower_well_output_min_0_t_0_S_0:
   dual_lower_well_output_min_0_t_0_S_0 >= 0
 dual_feasible_M_dual_lower_well_output_min_0_t_0_S_0:
   dual_lower_well_output_min_0_t_0_S_0
   + 1e+07 dual_lower_well_output_min_0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_lower_well_output_max_0_t_0_S_0:
   - lower_well_output[0,0,0] >= 0
 original_feasible_M_dual_lower_well_output_max_0_t_0_S_0:
   - lower_well_output[0,0,0]
   - 1e+07 dual_lower_well_output_max_0_t_0_S_0_binary <= 0
 dual_feasible_dual_lower_well_output_max_0_t_0_S_0:
   dual_lower_well_output_max_0_t_0_S_0 >= 0
 dual_feasible_M_dual_lower_well_output_max_0_t_0_S_0:
   dual_lower_well_output_max_0_t_0_S_0
   + 1e+07 dual_lower_well_output_max_0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_min_0_t_0_S_0:
   gas_node_pressure[0,0,0] >= 0
 original_feasible_M_dual_node_pressure_min_0_t_0_S_0:
   gas_node_pressure[0,0,0] - 1e+07 dual_node_pressure_min_0_t_0_S_0_binary
   <= 0
 dual_feasible_dual_node_pressure_min_0_t_0_S_0:
   dual_node_pressure_min_0_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_min_0_t_0_S_0:
   dual_node_pressure_min_0_t_0_S_0
   + 1e+07 dual_node_pressure_min_0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_max_0_t_0_S_0:
   - gas_node_pressure[0,0,0] >= -82.8
 original_feasible_M_dual_node_pressure_max_0_t_0_S_0:
   - gas_node_pressure[0,0,0]
   - 1e+07 dual_node_pressure_max_0_t_0_S_0_binary <= -82.8
 dual_feasible_dual_node_pressure_max_0_t_0_S_0:
   dual_node_pressure_max_0_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_max_0_t_0_S_0:
   dual_node_pressure_max_0_t_0_S_0
   + 1e+07 dual_node_pressure_max_0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_min_1_t_0_S_0:
   gas_node_pressure[1,0,0] >= 0
 original_feasible_M_dual_node_pressure_min_1_t_0_S_0:
   gas_node_pressure[1,0,0] - 1e+07 dual_node_pressure_min_1_t_0_S_0_binary
   <= 0
 dual_feasible_dual_node_pressure_min_1_t_0_S_0:
   dual_node_pressure_min_1_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_min_1_t_0_S_0:
   dual_node_pressure_min_1_t_0_S_0
   + 1e+07 dual_node_pressure_min_1_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_max_1_t_0_S_0:
   - gas_node_pressure[1,0,0] >= -82.8
 original_feasible_M_dual_node_pressure_max_1_t_0_S_0:
   - gas_node_pressure[1,0,0]
   - 1e+07 dual_node_pressure_max_1_t_0_S_0_binary <= -82.8
 dual_feasible_dual_node_pressure_max_1_t_0_S_0:
   dual_node_pressure_max_1_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_max_1_t_0_S_0:
   dual_node_pressure_max_1_t_0_S_0
   + 1e+07 dual_node_pressure_max_1_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_min_2_t_0_S_0:
   gas_node_pressure[2,0,0] >= 0
 original_feasible_M_dual_node_pressure_min_2_t_0_S_0:
   gas_node_pressure[2,0,0] - 1e+07 dual_node_pressure_min_2_t_0_S_0_binary
   <= 0
 dual_feasible_dual_node_pressure_min_2_t_0_S_0:
   dual_node_pressure_min_2_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_min_2_t_0_S_0:
   dual_node_pressure_min_2_t_0_S_0
   + 1e+07 dual_node_pressure_min_2_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_max_2_t_0_S_0:
   - gas_node_pressure[2,0,0] >= -82.8
 original_feasible_M_dual_node_pressure_max_2_t_0_S_0:
   - gas_node_pressure[2,0,0]
   - 1e+07 dual_node_pressure_max_2_t_0_S_0_binary <= -82.8
 dual_feasible_dual_node_pressure_max_2_t_0_S_0:
   dual_node_pressure_max_2_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_max_2_t_0_S_0:
   dual_node_pressure_max_2_t_0_S_0
   + 1e+07 dual_node_pressure_max_2_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_min_3_t_0_S_0:
   gas_node_pressure[3,0,0] >= 0
 original_feasible_M_dual_node_pressure_min_3_t_0_S_0:
   gas_node_pressure[3,0,0] - 1e+07 dual_node_pressure_min_3_t_0_S_0_binary
   <= 0
 dual_feasible_dual_node_pressure_min_3_t_0_S_0:
   dual_node_pressure_min_3_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_min_3_t_0_S_0:
   dual_node_pressure_min_3_t_0_S_0
   + 1e+07 dual_node_pressure_min_3_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_max_3_t_0_S_0:
   - gas_node_pressure[3,0,0] >= -82.8
 original_feasible_M_dual_node_pressure_max_3_t_0_S_0:
   - gas_node_pressure[3,0,0]
   - 1e+07 dual_node_pressure_max_3_t_0_S_0_binary <= -82.8
 dual_feasible_dual_node_pressure_max_3_t_0_S_0:
   dual_node_pressure_max_3_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_max_3_t_0_S_0:
   dual_node_pressure_max_3_t_0_S_0
   + 1e+07 dual_node_pressure_max_3_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_min_4_t_0_S_0:
   gas_node_pressure[4,0,0] >= 0
 original_feasible_M_dual_node_pressure_min_4_t_0_S_0:
   gas_node_pressure[4,0,0] - 1e+07 dual_node_pressure_min_4_t_0_S_0_binary
   <= 0
 dual_feasible_dual_node_pressure_min_4_t_0_S_0:
   dual_node_pressure_min_4_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_min_4_t_0_S_0:
   dual_node_pressure_min_4_t_0_S_0
   + 1e+07 dual_node_pressure_min_4_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_max_4_t_0_S_0:
   - gas_node_pressure[4,0,0] >= -82.8
 original_feasible_M_dual_node_pressure_max_4_t_0_S_0:
   - gas_node_pressure[4,0,0]
   - 1e+07 dual_node_pressure_max_4_t_0_S_0_binary <= -82.8
 dual_feasible_dual_node_pressure_max_4_t_0_S_0:
   dual_node_pressure_max_4_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_max_4_t_0_S_0:
   dual_node_pressure_max_4_t_0_S_0
   + 1e+07 dual_node_pressure_max_4_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_min_5_t_0_S_0:
   gas_node_pressure[5,0,0] >= 0
 original_feasible_M_dual_node_pressure_min_5_t_0_S_0:
   gas_node_pressure[5,0,0] - 1e+07 dual_node_pressure_min_5_t_0_S_0_binary
   <= 0
 dual_feasible_dual_node_pressure_min_5_t_0_S_0:
   dual_node_pressure_min_5_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_min_5_t_0_S_0:
   dual_node_pressure_min_5_t_0_S_0
   + 1e+07 dual_node_pressure_min_5_t_0_S_0_binary <= 1e+07
 original_feasible_dual_node_pressure_max_5_t_0_S_0:
   - gas_node_pressure[5,0,0] >= -82.8
 original_feasible_M_dual_node_pressure_max_5_t_0_S_0:
   - gas_node_pressure[5,0,0]
   - 1e+07 dual_node_pressure_max_5_t_0_S_0_binary <= -82.8
 dual_feasible_dual_node_pressure_max_5_t_0_S_0:
   dual_node_pressure_max_5_t_0_S_0 >= 0
 dual_feasible_M_dual_node_pressure_max_5_t_0_S_0:
   dual_node_pressure_max_5_t_0_S_0
   + 1e+07 dual_node_pressure_max_5_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_min0_t_0_S_0: gas_flow_in[0,0,0] >= 0
 original_feasible_M_dual_gas_flow_in_min0_t_0_S_0: gas_flow_in[0,0,0]
   - 1e+07 dual_gas_flow_in_min0_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_in_min0_t_0_S_0: dual_gas_flow_in_min0_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_min0_t_0_S_0:
   dual_gas_flow_in_min0_t_0_S_0
   + 1e+07 dual_gas_flow_in_min0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_max0_t_0_S_0: - gas_flow_in[0,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_in_max0_t_0_S_0: - gas_flow_in[0,0,0]
   - 1e+07 dual_gas_flow_in_max0_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_in_max0_t_0_S_0: dual_gas_flow_in_max0_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_max0_t_0_S_0:
   dual_gas_flow_in_max0_t_0_S_0
   + 1e+07 dual_gas_flow_in_max0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_min0_t_0_S_0: gas_flow_out[0,0,0]
   >= 0
 original_feasible_M_dual_gas_flow_out_min0_t_0_S_0: gas_flow_out[0,0,0]
   - 1e+07 dual_gas_flow_out_min0_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_out_min0_t_0_S_0:
   dual_gas_flow_out_min0_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_min0_t_0_S_0:
   dual_gas_flow_out_min0_t_0_S_0
   + 1e+07 dual_gas_flow_out_min0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_max0_t_0_S_0: - gas_flow_out[0,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_out_max0_t_0_S_0: - gas_flow_out[0,0,0]
   - 1e+07 dual_gas_flow_out_max0_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_out_max0_t_0_S_0:
   dual_gas_flow_out_max0_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_max0_t_0_S_0:
   dual_gas_flow_out_max0_t_0_S_0
   + 1e+07 dual_gas_flow_out_max0_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_min1_t_0_S_0: gas_flow_in[1,0,0] >= 0
 original_feasible_M_dual_gas_flow_in_min1_t_0_S_0: gas_flow_in[1,0,0]
   - 1e+07 dual_gas_flow_in_min1_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_in_min1_t_0_S_0: dual_gas_flow_in_min1_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_min1_t_0_S_0:
   dual_gas_flow_in_min1_t_0_S_0
   + 1e+07 dual_gas_flow_in_min1_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_max1_t_0_S_0: - gas_flow_in[1,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_in_max1_t_0_S_0: - gas_flow_in[1,0,0]
   - 1e+07 dual_gas_flow_in_max1_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_in_max1_t_0_S_0: dual_gas_flow_in_max1_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_max1_t_0_S_0:
   dual_gas_flow_in_max1_t_0_S_0
   + 1e+07 dual_gas_flow_in_max1_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_min1_t_0_S_0: gas_flow_out[1,0,0]
   >= 0
 original_feasible_M_dual_gas_flow_out_min1_t_0_S_0: gas_flow_out[1,0,0]
   - 1e+07 dual_gas_flow_out_min1_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_out_min1_t_0_S_0:
   dual_gas_flow_out_min1_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_min1_t_0_S_0:
   dual_gas_flow_out_min1_t_0_S_0
   + 1e+07 dual_gas_flow_out_min1_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_max1_t_0_S_0: - gas_flow_out[1,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_out_max1_t_0_S_0: - gas_flow_out[1,0,0]
   - 1e+07 dual_gas_flow_out_max1_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_out_max1_t_0_S_0:
   dual_gas_flow_out_max1_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_max1_t_0_S_0:
   dual_gas_flow_out_max1_t_0_S_0
   + 1e+07 dual_gas_flow_out_max1_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_min2_t_0_S_0: gas_flow_in[2,0,0] >= 0
 original_feasible_M_dual_gas_flow_in_min2_t_0_S_0: gas_flow_in[2,0,0]
   - 1e+07 dual_gas_flow_in_min2_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_in_min2_t_0_S_0: dual_gas_flow_in_min2_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_min2_t_0_S_0:
   dual_gas_flow_in_min2_t_0_S_0
   + 1e+07 dual_gas_flow_in_min2_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_max2_t_0_S_0: - gas_flow_in[2,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_in_max2_t_0_S_0: - gas_flow_in[2,0,0]
   - 1e+07 dual_gas_flow_in_max2_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_in_max2_t_0_S_0: dual_gas_flow_in_max2_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_max2_t_0_S_0:
   dual_gas_flow_in_max2_t_0_S_0
   + 1e+07 dual_gas_flow_in_max2_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_min2_t_0_S_0: gas_flow_out[2,0,0]
   >= 0
 original_feasible_M_dual_gas_flow_out_min2_t_0_S_0: gas_flow_out[2,0,0]
   - 1e+07 dual_gas_flow_out_min2_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_out_min2_t_0_S_0:
   dual_gas_flow_out_min2_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_min2_t_0_S_0:
   dual_gas_flow_out_min2_t_0_S_0
   + 1e+07 dual_gas_flow_out_min2_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_max2_t_0_S_0: - gas_flow_out[2,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_out_max2_t_0_S_0: - gas_flow_out[2,0,0]
   - 1e+07 dual_gas_flow_out_max2_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_out_max2_t_0_S_0:
   dual_gas_flow_out_max2_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_max2_t_0_S_0:
   dual_gas_flow_out_max2_t_0_S_0
   + 1e+07 dual_gas_flow_out_max2_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_min3_t_0_S_0: gas_flow_in[3,0,0] >= 0
 original_feasible_M_dual_gas_flow_in_min3_t_0_S_0: gas_flow_in[3,0,0]
   - 1e+07 dual_gas_flow_in_min3_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_in_min3_t_0_S_0: dual_gas_flow_in_min3_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_min3_t_0_S_0:
   dual_gas_flow_in_min3_t_0_S_0
   + 1e+07 dual_gas_flow_in_min3_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_max3_t_0_S_0: - gas_flow_in[3,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_in_max3_t_0_S_0: - gas_flow_in[3,0,0]
   - 1e+07 dual_gas_flow_in_max3_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_in_max3_t_0_S_0: dual_gas_flow_in_max3_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_max3_t_0_S_0:
   dual_gas_flow_in_max3_t_0_S_0
   + 1e+07 dual_gas_flow_in_max3_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_min3_t_0_S_0: gas_flow_out[3,0,0]
   >= 0
 original_feasible_M_dual_gas_flow_out_min3_t_0_S_0: gas_flow_out[3,0,0]
   - 1e+07 dual_gas_flow_out_min3_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_out_min3_t_0_S_0:
   dual_gas_flow_out_min3_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_min3_t_0_S_0:
   dual_gas_flow_out_min3_t_0_S_0
   + 1e+07 dual_gas_flow_out_min3_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_max3_t_0_S_0: - gas_flow_out[3,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_out_max3_t_0_S_0: - gas_flow_out[3,0,0]
   - 1e+07 dual_gas_flow_out_max3_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_out_max3_t_0_S_0:
   dual_gas_flow_out_max3_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_max3_t_0_S_0:
   dual_gas_flow_out_max3_t_0_S_0
   + 1e+07 dual_gas_flow_out_max3_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_min4_t_0_S_0: gas_flow_in[4,0,0] >= 0
 original_feasible_M_dual_gas_flow_in_min4_t_0_S_0: gas_flow_in[4,0,0]
   - 1e+07 dual_gas_flow_in_min4_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_in_min4_t_0_S_0: dual_gas_flow_in_min4_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_min4_t_0_S_0:
   dual_gas_flow_in_min4_t_0_S_0
   + 1e+07 dual_gas_flow_in_min4_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_in_max4_t_0_S_0: - gas_flow_in[4,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_in_max4_t_0_S_0: - gas_flow_in[4,0,0]
   - 1e+07 dual_gas_flow_in_max4_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_in_max4_t_0_S_0: dual_gas_flow_in_max4_t_0_S_0
   >= 0
 dual_feasible_M_dual_gas_flow_in_max4_t_0_S_0:
   dual_gas_flow_in_max4_t_0_S_0
   + 1e+07 dual_gas_flow_in_max4_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_min4_t_0_S_0: gas_flow_out[4,0,0]
   >= 0
 original_feasible_M_dual_gas_flow_out_min4_t_0_S_0: gas_flow_out[4,0,0]
   - 1e+07 dual_gas_flow_out_min4_t_0_S_0_binary <= 0
 dual_feasible_dual_gas_flow_out_min4_t_0_S_0:
   dual_gas_flow_out_min4_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_min4_t_0_S_0:
   dual_gas_flow_out_min4_t_0_S_0
   + 1e+07 dual_gas_flow_out_min4_t_0_S_0_binary <= 1e+07
 original_feasible_dual_gas_flow_out_max4_t_0_S_0: - gas_flow_out[4,0,0]
   >= -20
 original_feasible_M_dual_gas_flow_out_max4_t_0_S_0: - gas_flow_out[4,0,0]
   - 1e+07 dual_gas_flow_out_max4_t_0_S_0_binary <= -20
 dual_feasible_dual_gas_flow_out_max4_t_0_S_0:
   dual_gas_flow_out_max4_t_0_S_0 >= 0
 dual_feasible_M_dual_gas_flow_out_max4_t_0_S_0:
   dual_gas_flow_out_max4_t_0_S_0
   + 1e+07 dual_gas_flow_out_max4_t_0_S_0_binary <= 1e+07
 dual_weymouth_simplify000[EqualFeasible]: gas_node_pressure[3,0,0]
   - gas_node_pressure[5,0,0] + gas_flow_in[0,0,0] + gas_flow_out[0,0,0]
   = 0
 dual_weymouth_simplify100[EqualFeasible]: gas_node_pressure[3,0,0]
   - gas_node_pressure[4,0,0] + gas_flow_in[1,0,0] + gas_flow_out[1,0,0]
   = 0
 dual_weymouth_simplify200[EqualFeasible]: gas_node_pressure[2,0,0]
   - gas_node_pressure[3,0,0] + gas_flow_in[2,0,0] + gas_flow_out[2,0,0]
   = 0
 dual_weymouth_simplify300[EqualFeasible]: gas_node_pressure[1,0,0]
   - gas_node_pressure[2,0,0] + gas_flow_in[3,0,0] + gas_flow_out[3,0,0]
   = 0
 dual_weymouth_simplify400[EqualFeasible]: gas_node_pressure[0,0,0]
   - gas_node_pressure[1,0,0] + gas_flow_in[4,0,0] + gas_flow_out[4,0,0]
   = 0
 dual_upper_chp_heat_output_0_0S0[EqualFeasible]:
   0.528 upper_chp_point[0,0,0,0] + 0.8 upper_chp_point[0,1,0,0]
   + 0.45 upper_chp_point[0,2,0,0] - upper_chp_heat_output[0,0,0] = 0
 dual_upper_chp_point_sum_one0_0S0[EqualFeasible]:
   - upper_chp_point[0,0,0,0] - upper_chp_point[0,1,0,0]
   - upper_chp_point[0,2,0,0] - upper_chp_point[0,3,0,0] = -1
 dual_lower_chp_heat_output_0_0S0[EqualFeasible]:
   0.03 lower_chp_point[0,0,0,0] + 0.02 lower_chp_point[0,1,0,0]
   + 0.01 lower_chp_point[0,2,0,0] - lower_chp_heat_output[0,0,0] = 0
 dual_lower_chp_point_sum_one0_0S0[EqualFeasible]:
   - lower_chp_point[0,0,0,0] - lower_chp_point[0,1,0,0]
   - lower_chp_point[0,2,0,0] - lower_chp_point[0,3,0,0] = -1
 original_feasible_dual_upper_chp_point_great_zero0_0S00:
   upper_chp_point[0,0,0,0] >= 0
 original_feasible_M_dual_upper_chp_point_great_zero0_0S00:
   upper_chp_point[0,0,0,0]
   - 1e+07 dual_upper_chp_point_great_zero0_0S00_binary <= 0
 dual_feasible_dual_upper_chp_point_great_zero0_0S00:
   dual_upper_chp_point_great_zero0_0S00 >= 0
 dual_feasible_M_dual_upper_chp_point_great_zero0_0S00:
   dual_upper_chp_point_great_zero0_0S00
   + 1e+07 dual_upper_chp_point_great_zero0_0S00_binary <= 1e+07
 original_feasible_dual_upper_chp_point_less_one0_0S00:
   - upper_chp_point[0,0,0,0] >= -1
 original_feasible_M_dual_upper_chp_point_less_one0_0S00:
   - upper_chp_point[0,0,0,0]
   - 1e+07 dual_upper_chp_point_less_one0_0S00_binary <= -1
 dual_feasible_dual_upper_chp_point_less_one0_0S00:
   dual_upper_chp_point_less_one0_0S00 >= 0
 dual_feasible_M_dual_upper_chp_point_less_one0_0S00:
   dual_upper_chp_point_less_one0_0S00
   + 1e+07 dual_upper_chp_point_less_one0_0S00_binary <= 1e+07
 original_feasible_dual_upper_chp_point_great_zero0_0S01:
   upper_chp_point[0,1,0,0] >= 0
 original_feasible_M_dual_upper_chp_point_great_zero0_0S01:
   upper_chp_point[0,1,0,0]
   - 1e+07 dual_upper_chp_point_great_zero0_0S01_binary <= 0
 dual_feasible_dual_upper_chp_point_great_zero0_0S01:
   dual_upper_chp_point_great_zero0_0S01 >= 0
 dual_feasible_M_dual_upper_chp_point_great_zero0_0S01:
   dual_upper_chp_point_great_zero0_0S01
   + 1e+07 dual_upper_chp_point_great_zero0_0S01_binary <= 1e+07
 original_feasible_dual_upper_chp_point_less_one0_0S01:
   - upper_chp_point[0,1,0,0] >= -1
 original_feasible_M_dual_upper_chp_point_less_one0_0S01:
   - upper_chp_point[0,1,0,0]
   - 1e+07 dual_upper_chp_point_less_one0_0S01_binary <= -1
 dual_feasible_dual_upper_chp_point_less_one0_0S01:
   dual_upper_chp_point_less_one0_0S01 >= 0
 dual_feasible_M_dual_upper_chp_point_less_one0_0S01:
   dual_upper_chp_point_less_one0_0S01
   + 1e+07 dual_upper_chp_point_less_one0_0S01_binary <= 1e+07
 original_feasible_dual_upper_chp_point_great_zero0_0S02:
   upper_chp_point[0,2,0,0] >= 0
 original_feasible_M_dual_upper_chp_point_great_zero0_0S02:
   upper_chp_point[0,2,0,0]
   - 1e+07 dual_upper_chp_point_great_zero0_0S02_binary <= 0
 dual_feasible_dual_upper_chp_point_great_zero0_0S02:
   dual_upper_chp_point_great_zero0_0S02 >= 0
 dual_feasible_M_dual_upper_chp_point_great_zero0_0S02:
   dual_upper_chp_point_great_zero0_0S02
   + 1e+07 dual_upper_chp_point_great_zero0_0S02_binary <= 1e+07
 original_feasible_dual_upper_chp_point_less_one0_0S02:
   - upper_chp_point[0,2,0,0] >= -1
 original_feasible_M_dual_upper_chp_point_less_one0_0S02:
   - upper_chp_point[0,2,0,0]
   - 1e+07 dual_upper_chp_point_less_one0_0S02_binary <= -1
 dual_feasible_dual_upper_chp_point_less_one0_0S02:
   dual_upper_chp_point_less_one0_0S02 >= 0
 dual_feasible_M_dual_upper_chp_point_less_one0_0S02:
   dual_upper_chp_point_less_one0_0S02
   + 1e+07 dual_upper_chp_point_less_one0_0S02_binary <= 1e+07
 original_feasible_dual_upper_chp_point_great_zero0_0S03:
   upper_chp_point[0,3,0,0] >= 0
 original_feasible_M_dual_upper_chp_point_great_zero0_0S03:
   upper_chp_point[0,3,0,0]
   - 1e+07 dual_upper_chp_point_great_zero0_0S03_binary <= 0
 dual_feasible_dual_upper_chp_point_great_zero0_0S03:
   dual_upper_chp_point_great_zero0_0S03 >= 0
 dual_feasible_M_dual_upper_chp_point_great_zero0_0S03:
   dual_upper_chp_point_great_zero0_0S03
   + 1e+07 dual_upper_chp_point_great_zero0_0S03_binary <= 1e+07
 original_feasible_dual_upper_chp_point_less_one0_0S03:
   - upper_chp_point[0,3,0,0] >= -1
 original_feasible_M_dual_upper_chp_point_less_one0_0S03:
   - upper_chp_point[0,3,0,0]
   - 1e+07 dual_upper_chp_point_less_one0_0S03_binary <= -1
 dual_feasible_dual_upper_chp_point_less_one0_0S03:
   dual_upper_chp_point_less_one0_0S03 >= 0
 dual_feasible_M_dual_upper_chp_point_less_one0_0S03:
   dual_upper_chp_point_less_one0_0S03
   + 1e+07 dual_upper_chp_point_less_one0_0S03_binary <= 1e+07
 original_feasible_dual_lower_chp_point_great_zero0_0S00:
   lower_chp_point[0,0,0,0] >= 0
 original_feasible_M_dual_lower_chp_point_great_zero0_0S00:
   lower_chp_point[0,0,0,0]
   - 1e+07 dual_lower_chp_point_great_zero0_0S00_binary <= 0
 dual_feasible_dual_lower_chp_point_great_zero0_0S00:
   dual_lower_chp_point_great_zero0_0S00 >= 0
 dual_feasible_M_dual_lower_chp_point_great_zero0_0S00:
   dual_lower_chp_point_great_zero0_0S00
   + 1e+07 dual_lower_chp_point_great_zero0_0S00_binary <= 1e+07
 original_feasible_dual_lower_chp_point_less_one0_0S00:
   - lower_chp_point[0,0,0,0] >= -1
 original_feasible_M_dual_lower_chp_point_less_one0_0S00:
   - lower_chp_point[0,0,0,0]
   - 1e+07 dual_lower_chp_point_less_one0_0S00_binary <= -1
 dual_feasible_dual_lower_chp_point_less_one0_0S00:
   dual_lower_chp_point_less_one0_0S00 >= 0
 dual_feasible_M_dual_lower_chp_point_less_one0_0S00:
   dual_lower_chp_point_less_one0_0S00
   + 1e+07 dual_lower_chp_point_less_one0_0S00_binary <= 1e+07
 original_feasible_dual_lower_chp_point_great_zero0_0S01:
   lower_chp_point[0,1,0,0] >= 0
 original_feasible_M_dual_lower_chp_point_great_zero0_0S01:
   lower_chp_point[0,1,0,0]
   - 1e+07 dual_lower_chp_point_great_zero0_0S01_binary <= 0
 dual_feasible_dual_lower_chp_point_great_zero0_0S01:
   dual_lower_chp_point_great_zero0_0S01 >= 0
 dual_feasible_M_dual_lower_chp_point_great_zero0_0S01:
   dual_lower_chp_point_great_zero0_0S01
   + 1e+07 dual_lower_chp_point_great_zero0_0S01_binary <= 1e+07
 original_feasible_dual_lower_chp_point_less_one0_0S01:
   - lower_chp_point[0,1,0,0] >= -1
 original_feasible_M_dual_lower_chp_point_less_one0_0S01:
   - lower_chp_point[0,1,0,0]
   - 1e+07 dual_lower_chp_point_less_one0_0S01_binary <= -1
 dual_feasible_dual_lower_chp_point_less_one0_0S01:
   dual_lower_chp_point_less_one0_0S01 >= 0
 dual_feasible_M_dual_lower_chp_point_less_one0_0S01:
   dual_lower_chp_point_less_one0_0S01
   + 1e+07 dual_lower_chp_point_less_one0_0S01_binary <= 1e+07
 original_feasible_dual_lower_chp_point_great_zero0_0S02:
   lower_chp_point[0,2,0,0] >= 0
 original_feasible_M_dual_lower_chp_point_great_zero0_0S02:
   lower_chp_point[0,2,0,0]
   - 1e+07 dual_lower_chp_point_great_zero0_0S02_binary <= 0
 dual_feasible_dual_lower_chp_point_great_zero0_0S02:
   dual_lower_chp_point_great_zero0_0S02 >= 0
 dual_feasible_M_dual_lower_chp_point_great_zero0_0S02:
   dual_lower_chp_point_great_zero0_0S02
   + 1e+07 dual_lower_chp_point_great_zero0_0S02_binary <= 1e+07
 original_feasible_dual_lower_chp_point_less_one0_0S02:
   - lower_chp_point[0,2,0,0] >= -1
 original_feasible_M_dual_lower_chp_point_less_one0_0S02:
   - lower_chp_point[0,2,0,0]
   - 1e+07 dual_lower_chp_point_less_one0_0S02_binary <= -1
 dual_feasible_dual_lower_chp_point_less_one0_0S02:
   dual_lower_chp_point_less_one0_0S02 >= 0
 dual_feasible_M_dual_lower_chp_point_less_one0_0S02:
   dual_lower_chp_point_less_one0_0S02
   + 1e+07 dual_lower_chp_point_less_one0_0S02_binary <= 1e+07
 original_feasible_dual_lower_chp_point_great_zero0_0S03:
   lower_chp_point[0,3,0,0] >= 0
 original_feasible_M_dual_lower_chp_point_great_zero0_0S03:
   lower_chp_point[0,3,0,0]
   - 1e+07 dual_lower_chp_point_great_zero0_0S03_binary <= 0
 dual_feasible_dual_lower_chp_point_great_zero0_0S03:
   dual_lower_chp_point_great_zero0_0S03 >= 0
 dual_feasible_M_dual_lower_chp_point_great_zero0_0S03:
   dual_lower_chp_point_great_zero0_0S03
   + 1e+07 dual_lower_chp_point_great_zero0_0S03_binary <= 1e+07
 original_feasible_dual_lower_chp_point_less_one0_0S03:
   - lower_chp_point[0,3,0,0] >= -1
 original_feasible_M_dual_lower_chp_point_less_one0_0S03:
   - lower_chp_point[0,3,0,0]
   - 1e+07 dual_lower_chp_point_less_one0_0S03_binary <= -1
 dual_feasible_dual_lower_chp_point_less_one0_0S03:
   dual_lower_chp_point_less_one0_0S03 >= 0
 dual_feasible_M_dual_lower_chp_point_less_one0_0S03:
   dual_lower_chp_point_less_one0_0S03
   + 1e+07 dual_lower_chp_point_less_one0_0S03_binary <= 1e+07
 dual_heater_balance0_0S0[EqualFeasible]: - upper_chp_heat_output[0,0,0]
   - lower_chp_heat_output[0,0,0] + 0.1 heat_node_tempe_supply[0,0,0]
   - 0.1 heat_node_tempe_return[0,0,0] = 0
 dual_exchanger_balance0_00[EqualFeasible]:
   - 0.04 heat_node_tempe_supply[3,0,0]
   + 0.04 heat_node_tempe_return[3,0,0] = -0.3266666666666667
 dual_exchanger_balance0_10[EqualFeasible]:
   - 0.02 heat_node_tempe_supply[4,0,0]
   + 0.02 heat_node_tempe_return[4,0,0] = -0.3266666666666667
 dual_exchanger_balance0_20[EqualFeasible]:
   - 0.04 heat_node_tempe_supply[5,0,0]
   + 0.04 heat_node_tempe_return[5,0,0] = -0.3266666666666667
 dual_line_temp_start_supply_0_0S0[EqualFeasible]:
   - heat_node_tempe_supply[0,0,0]
   + heat_pipe_start_tempe_supply_network[0,0,0] = 0
 dual_line_temp_start_return0_0S0[EqualFeasible]:
   - heat_node_tempe_return[1,0,0]
   + heat_pipe_start_tempe_return_network[0,0,0] = 0
 dual_line_temp_start_supply_0_1S0[EqualFeasible]:
   - heat_node_tempe_supply[1,0,0]
   + heat_pipe_start_tempe_supply_network[1,0,0] = 0
 dual_line_temp_start_return0_1S0[EqualFeasible]:
   - heat_node_tempe_return[2,0,0]
   + heat_pipe_start_tempe_return_network[1,0,0] = 0
 dual_line_temp_start_supply_0_2S0[EqualFeasible]:
   - heat_node_tempe_supply[2,0,0]
   + heat_pipe_start_tempe_supply_network[2,0,0] = 0
 dual_line_temp_start_return0_2S0[EqualFeasible]:
   - heat_node_tempe_return[3,0,0]
   + heat_pipe_start_tempe_return_network[2,0,0] = 0
 dual_line_temp_start_supply_0_3S0[EqualFeasible]:
   - heat_node_tempe_supply[1,0,0]
   + heat_pipe_start_tempe_supply_network[3,0,0] = 0
 dual_line_temp_start_return0_3S0[EqualFeasible]:
   - heat_node_tempe_return[4,0,0]
   + heat_pipe_start_tempe_return_network[3,0,0] = 0
 dual_line_temp_start_supply_0_4S0[EqualFeasible]:
   - heat_node_tempe_supply[2,0,0]
   + heat_pipe_start_tempe_supply_network[4,0,0] = 0
 dual_line_temp_start_return0_4S0[EqualFeasible]:
   - heat_node_tempe_return[5,0,0]
   + heat_pipe_start_tempe_return_network[4,0,0] = 0
 dual_mix_constraints_supply0_0S0[EqualFeasible]: = 0
 dual_mix_constraints_return0_0S0[EqualFeasible]:
   heat_node_tempe_return[0,0,0]
   - heat_pipe_end_tempe_return_network[0,0,0] = 0
 dual_mix_constraints_supply0_1S0[EqualFeasible]:
   heat_node_tempe_supply[1,0,0]
   - heat_pipe_end_tempe_supply_network[0,0,0] = 0
 dual_mix_constraints_return0_1S0[EqualFeasible]:
   heat_node_tempe_return[1,0,0]
   - 0.8 heat_pipe_end_tempe_return_network[1,0,0]
   - 0.2 heat_pipe_end_tempe_return_network[3,0,0] = 0
 dual_mix_constraints_supply0_2S0[EqualFeasible]:
   0.8 heat_node_tempe_supply[2,0,0]
   - 0.8 heat_pipe_end_tempe_supply_network[1,0,0] = 0
 dual_mix_constraints_return0_2S0[EqualFeasible]:
   0.8 heat_node_tempe_return[2,0,0]
   - 0.4 heat_pipe_end_tempe_return_network[2,0,0]
   - 0.4 heat_pipe_end_tempe_return_network[4,0,0] = 0
 dual_mix_constraints_supply0_3S0[EqualFeasible]:
   0.4 heat_node_tempe_supply[3,0,0]
   - 0.4 heat_pipe_end_tempe_supply_network[2,0,0] = 0
 dual_mix_constraints_return0_3S0[EqualFeasible]: = 0
 dual_mix_constraints_supply0_4S0[EqualFeasible]:
   0.2 heat_node_tempe_supply[4,0,0]
   - 0.2 heat_pipe_end_tempe_supply_network[3,0,0] = 0
 dual_mix_constraints_return0_4S0[EqualFeasible]: = 0
 dual_mix_constraints_supply0_5S0[EqualFeasible]:
   0.4 heat_node_tempe_supply[5,0,0]
   - 0.4 heat_pipe_end_tempe_supply_network[4,0,0] = 0
 dual_mix_constraints_return0_5S0[EqualFeasible]: = 0
 dual_heat_loss_supply0_0S0[EqualFeasible]:
   heat_pipe_start_tempe_supply_network[0,0,0]
   - heat_pipe_end_tempe_supply_network[0,0,0] = 0
 dual_heat_loss_return0_0S0[EqualFeasible]:
   heat_pipe_start_tempe_return_network[0,0,0]
   - heat_pipe_end_tempe_return_network[0,0,0] = 0
 dual_heat_loss_supply0_1S0[EqualFeasible]:
   heat_pipe_start_tempe_supply_network[1,0,0]
   - heat_pipe_end_tempe_supply_network[1,0,0] = 0
 dual_heat_loss_return0_1S0[EqualFeasible]:
   heat_pipe_start_tempe_return_network[1,0,0]
   - heat_pipe_end_tempe_return_network[1,0,0] = 0
 dual_heat_loss_supply0_2S0[EqualFeasible]:
   heat_pipe_start_tempe_supply_network[2,0,0]
   - heat_pipe_end_tempe_supply_network[2,0,0] = 0
 dual_heat_loss_return0_2S0[EqualFeasible]:
   heat_pipe_start_tempe_return_network[2,0,0]
   - heat_pipe_end_tempe_return_network[2,0,0] = 0
 dual_heat_loss_supply0_3S0[EqualFeasible]:
   heat_pipe_start_tempe_supply_network[3,0,0]
   - heat_pipe_end_tempe_supply_network[3,0,0] = 0
 dual_heat_loss_return0_3S0[EqualFeasible]:
   heat_pipe_start_tempe_return_network[3,0,0]
   - heat_pipe_end_tempe_return_network[3,0,0] = 0
 dual_heat_loss_supply0_4S0[EqualFeasible]:
   heat_pipe_start_tempe_supply_network[4,0,0]
   - heat_pipe_end_tempe_supply_network[4,0,0] = 0
 dual_heat_loss_return0_4S0[EqualFeasible]:
   heat_pipe_start_tempe_return_network[4,0,0]
   - heat_pipe_end_tempe_return_network[4,0,0] = 0
 original_feasible_dual_heater_supply_min0_0S0:
   heat_node_tempe_supply[0,0,0] >= 0
 original_feasible_M_dual_heater_supply_min0_0S0:
   heat_node_tempe_supply[0,0,0] - 1e+07 dual_heater_supply_min0_0S0_binary
   <= 0
 dual_feasible_dual_heater_supply_min0_0S0: dual_heater_supply_min0_0S0
   >= 0
 dual_feasible_M_dual_heater_supply_min0_0S0: dual_heater_supply_min0_0S0
   + 1e+07 dual_heater_supply_min0_0S0_binary <= 1e+07
 original_feasible_dual_heater_supply_max0_0S0:
   - heat_node_tempe_supply[0,0,0] >= -100
 original_feasible_M_dual_heater_supply_max0_0S0:
   - heat_node_tempe_supply[0,0,0]
   - 1e+07 dual_heater_supply_max0_0S0_binary <= -100
 dual_feasible_dual_heater_supply_max0_0S0: dual_heater_supply_max0_0S0
   >= 0
 dual_feasible_M_dual_heater_supply_max0_0S0: dual_heater_supply_max0_0S0
   + 1e+07 dual_heater_supply_max0_0S0_binary <= 1e+07
 original_feasible_dual_heater_return_min0_0S0:
   heat_node_tempe_return[0,0,0] >= 0
 original_feasible_M_dual_heater_return_min0_0S0:
   heat_node_tempe_return[0,0,0] - 1e+07 dual_heater_return_min0_0S0_binary
   <= 0
 dual_feasible_dual_heater_return_min0_0S0: dual_heater_return_min0_0S0
   >= 0
 dual_feasible_M_dual_heater_return_min0_0S0: dual_heater_return_min0_0S0
   + 1e+07 dual_heater_return_min0_0S0_binary <= 1e+07
 original_feasible_dual_heater_return_max0_0S0:
   - heat_node_tempe_return[0,0,0] >= -100
 original_feasible_M_dual_heater_return_max0_0S0:
   - heat_node_tempe_return[0,0,0]
   - 1e+07 dual_heater_return_max0_0S0_binary <= -100
 dual_feasible_dual_heater_return_max0_0S0: dual_heater_return_max0_0S0
   >= 0
 dual_feasible_M_dual_heater_return_max0_0S0: dual_heater_return_max0_0S0
   + 1e+07 dual_heater_return_max0_0S0_binary <= 1e+07
 original_feasible_dual_exchanger_supply_min0_0S0:
   heat_node_tempe_supply[3,0,0] >= 0
 original_feasible_M_dual_exchanger_supply_min0_0S0:
   heat_node_tempe_supply[3,0,0]
   - 1e+07 dual_exchanger_supply_min0_0S0_binary <= 0
 dual_feasible_dual_exchanger_supply_min0_0S0:
   dual_exchanger_supply_min0_0S0 >= 0
 dual_feasible_M_dual_exchanger_supply_min0_0S0:
   dual_exchanger_supply_min0_0S0
   + 1e+07 dual_exchanger_supply_min0_0S0_binary <= 1e+07
 original_feasible_dual_exchanger_supply_max0_0S0:
   - heat_node_tempe_supply[3,0,0] >= -100
 original_feasible_M_dual_exchanger_supply_max0_0S0:
   - heat_node_tempe_supply[3,0,0]
   - 1e+07 dual_exchanger_supply_max0_0S0_binary <= -100
 dual_feasible_dual_exchanger_supply_max0_0S0:
   dual_exchanger_supply_max0_0S0 >= 0
 dual_feasible_M_dual_exchanger_supply_max0_0S0:
   dual_exchanger_supply_max0_0S0
   + 1e+07 dual_exchanger_supply_max0_0S0_binary <= 1e+07
 original_feasible_dual_exchanger_return_min0_0S0:
   heat_node_tempe_return[3,0,0] >= 0
 original_feasible_M_dual_exchanger_return_min0_0S0:
   heat_node_tempe_return[3,0,0]
   - 1e+07 dual_exchanger_return_min0_0S0_binary <= 0
 dual_feasible_dual_exchanger_return_min0_0S0:
   dual_exchanger_return_min0_0S0 >= 0
 dual_feasible_M_dual_exchanger_return_min0_0S0:
   dual_exchanger_return_min0_0S0
   + 1e+07 dual_exchanger_return_min0_0S0_binary <= 1e+07
 original_feasible_dual_exchanger_return_max0_0S0:
   - heat_node_tempe_return[3,0,0] >= -100
 original_feasible_M_dual_exchanger_return_max0_0S0:
   - heat_node_tempe_return[3,0,0]
   - 1e+07 dual_exchanger_return_max0_0S0_binary <= -100
 dual_feasible_dual_exchanger_return_max0_0S0:
   dual_exchanger_return_max0_0S0 >= 0
 dual_feasible_M_dual_exchanger_return_max0_0S0:
   dual_exchanger_return_max0_0S0
   + 1e+07 dual_exchanger_return_max0_0S0_binary <= 1e+07
 original_feasible_dual_exchanger_supply_min0_1S0:
   heat_node_tempe_supply[4,0,0] >= 0
 original_feasible_M_dual_exchanger_supply_min0_1S0:
   heat_node_tempe_supply[4,0,0]
   - 1e+07 dual_exchanger_supply_min0_1S0_binary <= 0
 dual_feasible_dual_exchanger_supply_min0_1S0:
   dual_exchanger_supply_min0_1S0 >= 0
 dual_feasible_M_dual_exchanger_supply_min0_1S0:
   dual_exchanger_supply_min0_1S0
   + 1e+07 dual_exchanger_supply_min0_1S0_binary <= 1e+07
 original_feasible_dual_exchanger_supply_max0_1S0:
   - heat_node_tempe_supply[4,0,0] >= -100
 original_feasible_M_dual_exchanger_supply_max0_1S0:
   - heat_node_tempe_supply[4,0,0]
   - 1e+07 dual_exchanger_supply_max0_1S0_binary <= -100
 dual_feasible_dual_exchanger_supply_max0_1S0:
   dual_exchanger_supply_max0_1S0 >= 0
 dual_feasible_M_dual_exchanger_supply_max0_1S0:
   dual_exchanger_supply_max0_1S0
   + 1e+07 dual_exchanger_supply_max0_1S0_binary <= 1e+07
 original_feasible_dual_exchanger_return_min0_1S0:
   heat_node_tempe_return[4,0,0] >= 0
 original_feasible_M_dual_exchanger_return_min0_1S0:
   heat_node_tempe_return[4,0,0]
   - 1e+07 dual_exchanger_return_min0_1S0_binary <= 0
 dual_feasible_dual_exchanger_return_min0_1S0:
   dual_exchanger_return_min0_1S0 >= 0
 dual_feasible_M_dual_exchanger_return_min0_1S0:
   dual_exchanger_return_min0_1S0
   + 1e+07 dual_exchanger_return_min0_1S0_binary <= 1e+07
 original_feasible_dual_exchanger_return_max0_1S0:
   - heat_node_tempe_return[4,0,0] >= -100
 original_feasible_M_dual_exchanger_return_max0_1S0:
   - heat_node_tempe_return[4,0,0]
   - 1e+07 dual_exchanger_return_max0_1S0_binary <= -100
 dual_feasible_dual_exchanger_return_max0_1S0:
   dual_exchanger_return_max0_1S0 >= 0
 dual_feasible_M_dual_exchanger_return_max0_1S0:
   dual_exchanger_return_max0_1S0
   + 1e+07 dual_exchanger_return_max0_1S0_binary <= 1e+07
 original_feasible_dual_exchanger_supply_min0_2S0:
   heat_node_tempe_supply[5,0,0] >= 0
 original_feasible_M_dual_exchanger_supply_min0_2S0:
   heat_node_tempe_supply[5,0,0]
   - 1e+07 dual_exchanger_supply_min0_2S0_binary <= 0
 dual_feasible_dual_exchanger_supply_min0_2S0:
   dual_exchanger_supply_min0_2S0 >= 0
 dual_feasible_M_dual_exchanger_supply_min0_2S0:
   dual_exchanger_supply_min0_2S0
   + 1e+07 dual_exchanger_supply_min0_2S0_binary <= 1e+07
 original_feasible_dual_exchanger_supply_max0_2S0:
   - heat_node_tempe_supply[5,0,0] >= -100
 original_feasible_M_dual_exchanger_supply_max0_2S0:
   - heat_node_tempe_supply[5,0,0]
   - 1e+07 dual_exchanger_supply_max0_2S0_binary <= -100
 dual_feasible_dual_exchanger_supply_max0_2S0:
   dual_exchanger_supply_max0_2S0 >= 0
 dual_feasible_M_dual_exchanger_supply_max0_2S0:
   dual_exchanger_supply_max0_2S0
   + 1e+07 dual_exchanger_supply_max0_2S0_binary <= 1e+07
 original_feasible_dual_exchanger_return_min0_2S0:
   heat_node_tempe_return[5,0,0] >= 0
 original_feasible_M_dual_exchanger_return_min0_2S0:
   heat_node_tempe_return[5,0,0]
   - 1e+07 dual_exchanger_return_min0_2S0_binary <= 0
 dual_feasible_dual_exchanger_return_min0_2S0:
   dual_exchanger_return_min0_2S0 >= 0
 dual_feasible_M_dual_exchanger_return_min0_2S0:
   dual_exchanger_return_min0_2S0
   + 1e+07 dual_exchanger_return_min0_2S0_binary <= 1e+07
 original_feasible_dual_exchanger_return_max0_2S0:
   - heat_node_tempe_return[5,0,0] >= -100
 original_feasible_M_dual_exchanger_return_max0_2S0:
   - heat_node_tempe_return[5,0,0]
   - 1e+07 dual_exchanger_return_max0_2S0_binary <= -100
 dual_feasible_dual_exchanger_return_max0_2S0:
   dual_exchanger_return_max0_2S0 >= 0
 dual_feasible_M_dual_exchanger_return_max0_2S0:
   dual_exchanger_return_max0_2S0
   + 1e+07 dual_exchanger_return_max0_2S0_binary <= 1e+07
 upper_chp_heat_quoted_price_max0chp_0: upper_chp_heat_quoted_price[0,0]
   <= 10
 upper_chp_gas_quoted_price_max0chp_0: upper_chp_gas_quoted_price[0,0]
   <= 5
 upper_gas_well_quoted_price_max0_well_0: upper_gas_quoted_price[0,0]
   <= 4.4
 upper_chp_point[0,0,0,0]: 0.528 dual_dual_upper_chp_heat_output_0_0S0
   - dual_dual_upper_chp_point_sum_one0_0S0
   - dual_upper_chp_point_great_zero0_0S00
   + dual_upper_chp_point_less_one0_0S00 = 0
 upper_chp_point[0,1,0,0]: 0.8 dual_dual_upper_chp_heat_output_0_0S0
   - dual_dual_upper_chp_point_sum_one0_0S0
   - dual_upper_chp_point_great_zero0_0S01
   + dual_upper_chp_point_less_one0_0S01 = 0
 upper_chp_point[0,2,0,0]: 0.45 dual_dual_upper_chp_heat_output_0_0S0
   - dual_dual_upper_chp_point_sum_one0_0S0
   - dual_upper_chp_point_great_zero0_0S02
   + dual_upper_chp_point_less_one0_0S02 = 0
 upper_chp_point[0,3,0,0]: - dual_dual_upper_chp_point_sum_one0_0S0
   - dual_upper_chp_point_great_zero0_0S03
   + dual_upper_chp_point_less_one0_0S03 = 0
 lower_chp_point[0,0,0,0]: 0.03 dual_dual_lower_chp_heat_output_0_0S0
   - dual_dual_lower_chp_point_sum_one0_0S0
   - dual_lower_chp_point_great_zero0_0S00
   + dual_lower_chp_point_less_one0_0S00 = 0
 lower_chp_point[0,1,0,0]: 0.02 dual_dual_lower_chp_heat_output_0_0S0
   - dual_dual_lower_chp_point_sum_one0_0S0
   - dual_lower_chp_point_great_zero0_0S01
   + dual_lower_chp_point_less_one0_0S01 = 0
 lower_chp_point[0,2,0,0]: 0.01 dual_dual_lower_chp_heat_output_0_0S0
   - dual_dual_lower_chp_point_sum_one0_0S0
   - dual_lower_chp_point_great_zero0_0S02
   + dual_lower_chp_point_less_one0_0S02 = 0
 lower_chp_point[0,3,0,0]: - dual_dual_lower_chp_point_sum_one0_0S0
   - dual_lower_chp_point_great_zero0_0S03
   + dual_lower_chp_point_less_one0_0S03 = 0
 upper_chp_heat_output[0,0,0]: upper_chp_heat_quoted_price[0,0]
   - 0.9 upper_chp_gas_quoted_price[0,0]
   + 0.9 dual_dual_node_gas_balance_time_0_node_4S_0
   - dual_dual_upper_chp_heat_output_0_0S0 - dual_dual_heater_balance0_0S0
   = 0
 lower_chp_heat_output[0,0,0]:
   0.6 dual_dual_node_gas_balance_time_0_node_5S_0
   - dual_dual_lower_chp_heat_output_0_0S0 - dual_dual_heater_balance0_0S0
   = 0
 heat_node_tempe_supply[0,0,0]: 0.1 dual_dual_heater_balance0_0S0
   - dual_dual_line_temp_start_supply_0_0S0 - dual_heater_supply_min0_0S0
   + dual_heater_supply_max0_0S0 = 0
 heat_node_tempe_supply[1,0,0]: - dual_dual_line_temp_start_supply_0_1S0
   - dual_dual_line_temp_start_supply_0_3S0
   + dual_dual_mix_constraints_supply0_1S0 = 0
 heat_node_tempe_supply[2,0,0]: - dual_dual_line_temp_start_supply_0_2S0
   - dual_dual_line_temp_start_supply_0_4S0
   + 0.8 dual_dual_mix_constraints_supply0_2S0 = 0
 heat_node_tempe_supply[3,0,0]: - 0.04 dual_dual_exchanger_balance0_00
   + 0.4 dual_dual_mix_constraints_supply0_3S0
   - dual_exchanger_supply_min0_0S0 + dual_exchanger_supply_max0_0S0 = 0
 heat_node_tempe_supply[4,0,0]: - 0.02 dual_dual_exchanger_balance0_10
   + 0.2 dual_dual_mix_constraints_supply0_4S0
   - dual_exchanger_supply_min0_1S0 + dual_exchanger_supply_max0_1S0 = 0
 heat_node_tempe_supply[5,0,0]: - 0.04 dual_dual_exchanger_balance0_20
   + 0.4 dual_dual_mix_constraints_supply0_5S0
   - dual_exchanger_supply_min0_2S0 + dual_exchanger_supply_max0_2S0 = 0
 heat_node_tempe_return[0,0,0]: - 0.1 dual_dual_heater_balance0_0S0
   + dual_dual_mix_constraints_return0_0S0 - dual_heater_return_min0_0S0
   + dual_heater_return_max0_0S0 = 0
 heat_node_tempe_return[1,0,0]: - dual_dual_line_temp_start_return0_0S0
   + dual_dual_mix_constraints_return0_1S0 = 0
 heat_node_tempe_return[2,0,0]: - dual_dual_line_temp_start_return0_1S0
   + 0.8 dual_dual_mix_constraints_return0_2S0 = 0
 heat_node_tempe_return[3,0,0]: 0.04 dual_dual_exchanger_balance0_00
   - dual_dual_line_temp_start_return0_2S0 - dual_exchanger_return_min0_0S0
   + dual_exchanger_return_max0_0S0 = 0
 heat_node_tempe_return[4,0,0]: 0.02 dual_dual_exchanger_balance0_10
   - dual_dual_line_temp_start_return0_3S0 - dual_exchanger_return_min0_1S0
   + dual_exchanger_return_max0_1S0 = 0
 heat_node_tempe_return[5,0,0]: 0.04 dual_dual_exchanger_balance0_20
   - dual_dual_line_temp_start_return0_4S0 - dual_exchanger_return_min0_2S0
   + dual_exchanger_return_max0_2S0 = 0
 heat_pipe_start_tempe_supply_network[0,0,0]:
   dual_dual_line_temp_start_supply_0_0S0 + dual_dual_heat_loss_supply0_0S0
   = 0
 heat_pipe_start_tempe_supply_network[1,0,0]:
   dual_dual_line_temp_start_supply_0_1S0 + dual_dual_heat_loss_supply0_1S0
   = 0
 heat_pipe_start_tempe_supply_network[2,0,0]:
   dual_dual_line_temp_start_supply_0_2S0 + dual_dual_heat_loss_supply0_2S0
   = 0
 heat_pipe_start_tempe_supply_network[3,0,0]:
   dual_dual_line_temp_start_supply_0_3S0 + dual_dual_heat_loss_supply0_3S0
   = 0
 heat_pipe_start_tempe_supply_network[4,0,0]:
   dual_dual_line_temp_start_supply_0_4S0 + dual_dual_heat_loss_supply0_4S0
   = 0
 heat_pipe_end_tempe_supply_network[0,0,0]:
   - dual_dual_mix_constraints_supply0_1S0
   - dual_dual_heat_loss_supply0_0S0 = 0
 heat_pipe_end_tempe_supply_network[1,0,0]:
   - 0.8 dual_dual_mix_constraints_supply0_2S0
   - dual_dual_heat_loss_supply0_1S0 = 0
 heat_pipe_end_tempe_supply_network[2,0,0]:
   - 0.4 dual_dual_mix_constraints_supply0_3S0
   - dual_dual_heat_loss_supply0_2S0 = 0
 heat_pipe_end_tempe_supply_network[3,0,0]:
   - 0.2 dual_dual_mix_constraints_supply0_4S0
   - dual_dual_heat_loss_supply0_3S0 = 0
 heat_pipe_end_tempe_supply_network[4,0,0]:
   - 0.4 dual_dual_mix_constraints_supply0_5S0
   - dual_dual_heat_loss_supply0_4S0 = 0
 heat_pipe_start_tempe_return_network[0,0,0]:
   dual_dual_line_temp_start_return0_0S0 + dual_dual_heat_loss_return0_0S0
   = 0
 heat_pipe_start_tempe_return_network[1,0,0]:
   dual_dual_line_temp_start_return0_1S0 + dual_dual_heat_loss_return0_1S0
   = 0
 heat_pipe_start_tempe_return_network[2,0,0]:
   dual_dual_line_temp_start_return0_2S0 + dual_dual_heat_loss_return0_2S0
   = 0
 heat_pipe_start_tempe_return_network[3,0,0]:
   dual_dual_line_temp_start_return0_3S0 + dual_dual_heat_loss_return0_3S0
   = 0
 heat_pipe_start_tempe_return_network[4,0,0]:
   dual_dual_line_temp_start_return0_4S0 + dual_dual_heat_loss_return0_4S0
   = 0
 heat_pipe_end_tempe_return_network[0,0,0]:
   - dual_dual_mix_constraints_return0_0S0
   - dual_dual_heat_loss_return0_0S0 = 0
 heat_pipe_end_tempe_return_network[1,0,0]:
   - 0.8 dual_dual_mix_constraints_return0_1S0
   - dual_dual_heat_loss_return0_1S0 = 0
 heat_pipe_end_tempe_return_network[2,0,0]:
   - 0.4 dual_dual_mix_constraints_return0_2S0
   - dual_dual_heat_loss_return0_2S0 = 0
 heat_pipe_end_tempe_return_network[3,0,0]:
   - 0.2 dual_dual_mix_constraints_return0_1S0
   - dual_dual_heat_loss_return0_3S0 = 0
 heat_pipe_end_tempe_return_network[4,0,0]:
   - 0.4 dual_dual_mix_constraints_return0_2S0
   - dual_dual_heat_loss_return0_4S0 = 0
 upper_well_output[0,0,0]: upper_gas_quoted_price[0,0]
   - dual_dual_node_gas_balance_time_0_node_5S_0
   - dual_upper_well_output_min_0_t_0_S_0
   + dual_upper_well_output_max_0_t_0_S_0 = 0
 lower_well_output[0,0,0]: - dual_dual_node_gas_balance_time_0_node_4S_0
   - dual_lower_well_output_min_0_t_0_S_0
   + dual_lower_well_output_max_0_t_0_S_0 = -2.8
 gas_node_pressure[0,0,0]: - dual_node_pressure_min_0_t_0_S_0
   + dual_node_pressure_max_0_t_0_S_0 + dual_dual_weymouth_simplify400 = 0
 gas_node_pressure[1,0,0]: - dual_node_pressure_min_1_t_0_S_0
   + dual_node_pressure_max_1_t_0_S_0 + dual_dual_weymouth_simplify300
   - dual_dual_weymouth_simplify400 = 0
 gas_node_pressure[2,0,0]: - dual_node_pressure_min_2_t_0_S_0
   + dual_node_pressure_max_2_t_0_S_0 + dual_dual_weymouth_simplify200
   - dual_dual_weymouth_simplify300 = 0
 gas_node_pressure[3,0,0]: - dual_node_pressure_min_3_t_0_S_0
   + dual_node_pressure_max_3_t_0_S_0 + dual_dual_weymouth_simplify000
   + dual_dual_weymouth_simplify100 - dual_dual_weymouth_simplify200 = 0
 gas_node_pressure[4,0,0]: - dual_node_pressure_min_4_t_0_S_0
   + dual_node_pressure_max_4_t_0_S_0 - dual_dual_weymouth_simplify100 = 0
 gas_node_pressure[5,0,0]: - dual_node_pressure_min_5_t_0_S_0
   + dual_node_pressure_max_5_t_0_S_0 - dual_dual_weymouth_simplify000 = 0
 gas_flow_in[0,0,0]: dual_dual_node_gas_balance_time_0_node_5S_0
   - dual_gas_flow_in_min0_t_0_S_0 + dual_gas_flow_in_max0_t_0_S_0
   + dual_dual_weymouth_simplify000 = 0
 gas_flow_in[1,0,0]: dual_dual_node_gas_balance_time_0_node_4S_0
   - dual_gas_flow_in_min1_t_0_S_0 + dual_gas_flow_in_max1_t_0_S_0
   + dual_dual_weymouth_simplify100 = 0
 gas_flow_in[2,0,0]: dual_dual_node_gas_balance_time_0_node_3S_0
   - dual_gas_flow_in_min2_t_0_S_0 + dual_gas_flow_in_max2_t_0_S_0
   + dual_dual_weymouth_simplify200 = 0
 gas_flow_in[3,0,0]: dual_dual_node_gas_balance_time_0_node_2S_0
   - dual_gas_flow_in_min3_t_0_S_0 + dual_gas_flow_in_max3_t_0_S_0
   + dual_dual_weymouth_simplify300 = 0
 gas_flow_in[4,0,0]: dual_dual_node_gas_balance_time_0_node_1S_0
   - dual_gas_flow_in_min4_t_0_S_0 + dual_gas_flow_in_max4_t_0_S_0
   + dual_dual_weymouth_simplify400 = 0
 gas_flow_out[0,0,0]: - dual_dual_node_gas_balance_time_0_node_3S_0
   - dual_gas_flow_out_min0_t_0_S_0 + dual_gas_flow_out_max0_t_0_S_0
   + dual_dual_weymouth_simplify000 = 0
 gas_flow_out[1,0,0]: - dual_dual_node_gas_balance_time_0_node_3S_0
   - dual_gas_flow_out_min1_t_0_S_0 + dual_gas_flow_out_max1_t_0_S_0
   + dual_dual_weymouth_simplify100 = 0
 gas_flow_out[2,0,0]: - dual_dual_node_gas_balance_time_0_node_2S_0
   - dual_gas_flow_out_min2_t_0_S_0 + dual_gas_flow_out_max2_t_0_S_0
   + dual_dual_weymouth_simplify200 = 0
 gas_flow_out[3,0,0]: - dual_dual_node_gas_balance_time_0_node_1S_0
   - dual_gas_flow_out_min3_t_0_S_0 + dual_gas_flow_out_max3_t_0_S_0
   + dual_dual_weymouth_simplify300 = 0
 gas_flow_out[4,0,0]: - dual_dual_node_gas_balance_time_0_node_0S_0
   - dual_gas_flow_out_min4_t_0_S_0 + dual_gas_flow_out_max4_t_0_S_0
   + dual_dual_weymouth_simplify400 = 0
Bounds
 upper_chp_point[0,0,0,0] free
 upper_chp_point[0,1,0,0] free
 upper_chp_point[0,2,0,0] free
 upper_chp_point[0,3,0,0] free
 lower_chp_point[0,0,0,0] free
 lower_chp_point[0,1,0,0] free
 lower_chp_point[0,2,0,0] free
 lower_chp_point[0,3,0,0] free
 upper_chp_heat_output[0,0,0] free
 lower_chp_heat_output[0,0,0] free
 heat_node_tempe_supply[0,0,0] free
 heat_node_tempe_supply[1,0,0] free
 heat_node_tempe_supply[2,0,0] free
 heat_node_tempe_supply[3,0,0] free
 heat_node_tempe_supply[4,0,0] free
 heat_node_tempe_supply[5,0,0] free
 heat_node_tempe_return[0,0,0] free
 heat_node_tempe_return[1,0,0] free
 heat_node_tempe_return[2,0,0] free
 heat_node_tempe_return[3,0,0] free
 heat_node_tempe_return[4,0,0] free
 heat_node_tempe_return[5,0,0] free
 heat_pipe_start_tempe_supply_network[0,0,0] free
 heat_pipe_start_tempe_supply_network[1,0,0] free
 heat_pipe_start_tempe_supply_network[2,0,0] free
 heat_pipe_start_tempe_supply_network[3,0,0] free
 heat_pipe_start_tempe_supply_network[4,0,0] free
 heat_pipe_end_tempe_supply_network[0,0,0] free
 heat_pipe_end_tempe_supply_network[1,0,0] free
 heat_pipe_end_tempe_supply_network[2,0,0] free
 heat_pipe_end_tempe_supply_network[3,0,0] free
 heat_pipe_end_tempe_supply_network[4,0,0] free
 heat_pipe_start_tempe_return_network[0,0,0] free
 heat_pipe_start_tempe_return_network[1,0,0] free
 heat_pipe_start_tempe_return_network[2,0,0] free
 heat_pipe_start_tempe_return_network[3,0,0] free
 heat_pipe_start_tempe_return_network[4,0,0] free
 heat_pipe_end_tempe_return_network[0,0,0] free
 heat_pipe_end_tempe_return_network[1,0,0] free
 heat_pipe_end_tempe_return_network[2,0,0] free
 heat_pipe_end_tempe_return_network[3,0,0] free
 heat_pipe_end_tempe_return_network[4,0,0] free
 upper_well_output[0,0,0] free
 lower_well_output[0,0,0] free
 gas_node_pressure[0,0,0] free
 gas_node_pressure[1,0,0] free
 gas_node_pressure[2,0,0] free
 gas_node_pressure[3,0,0] free
 gas_node_pressure[4,0,0] free
 gas_node_pressure[5,0,0] free
 gas_flow_in[0,0,0] free
 gas_flow_in[1,0,0] free
 gas_flow_in[2,0,0] free
 gas_flow_in[3,0,0] free
 gas_flow_in[4,0,0] free
 gas_flow_out[0,0,0] free
 gas_flow_out[1,0,0] free
 gas_flow_out[2,0,0] free
 gas_flow_out[3,0,0] free
 gas_flow_out[4,0,0] free
 weymouth_left_aux[0,0,0] free
 weymouth_left_aux[1,0,0] free
 weymouth_left_aux[2,0,0] free
 weymouth_left_aux[3,0,0] free
 weymouth_left_aux[4,0,0] free
 weymouth_right_aux1[0,0,0] free
 weymouth_right_aux1[1,0,0] free
 weymouth_right_aux1[2,0,0] free
 weymouth_right_aux1[3,0,0] free
 weymouth_right_aux1[4,0,0] free
 weymouth_right_aux2[0,0,0] free
 weymouth_right_aux2[1,0,0] free
 weymouth_right_aux2[2,0,0] free
 weymouth_right_aux2[3,0,0] free
 weymouth_right_aux2[4,0,0] free
 pccp_relax[0,0,0] free
 pccp_relax[1,0,0] free
 pccp_relax[2,0,0] free
 pccp_relax[3,0,0] free
 pccp_relax[4,0,0] free
 gas_linepack[0,0,0] free
 gas_linepack[1,0,0] free
 gas_linepack[2,0,0] free
 gas_linepack[3,0,0] free
 gas_linepack[4,0,0] free
 dual_dual_node_gas_balance_time_0_node_0S_0 free
 dual_dual_node_gas_balance_time_0_node_1S_0 free
 dual_dual_node_gas_balance_time_0_node_2S_0 free
 dual_dual_node_gas_balance_time_0_node_3S_0 free
 dual_dual_node_gas_balance_time_0_node_4S_0 free
 dual_dual_node_gas_balance_time_0_node_5S_0 free
 dual_dual_weymouth_simplify000 free
 dual_dual_weymouth_simplify100 free
 dual_dual_weymouth_simplify200 free
 dual_dual_weymouth_simplify300 free
 dual_dual_weymouth_simplify400 free
 dual_dual_upper_chp_heat_output_0_0S0 free
 dual_dual_upper_chp_point_sum_one0_0S0 free
 dual_dual_lower_chp_heat_output_0_0S0 free
 dual_dual_lower_chp_point_sum_one0_0S0 free
 dual_dual_heater_balance0_0S0 free
 dual_dual_exchanger_balance0_00 free
 dual_dual_exchanger_balance0_10 free
 dual_dual_exchanger_balance0_20 free
 dual_dual_line_temp_start_supply_0_0S0 free
 dual_dual_line_temp_start_return0_0S0 free
 dual_dual_line_temp_start_supply_0_1S0 free
 dual_dual_line_temp_start_return0_1S0 free
 dual_dual_line_temp_start_supply_0_2S0 free
 dual_dual_line_temp_start_return0_2S0 free
 dual_dual_line_temp_start_supply_0_3S0 free
 dual_dual_line_temp_start_return0_3S0 free
 dual_dual_line_temp_start_supply_0_4S0 free
 dual_dual_line_temp_start_return0_4S0 free
 dual_dual_mix_constraints_supply0_0S0 free
 dual_dual_mix_constraints_return0_0S0 free
 dual_dual_mix_constraints_supply0_1S0 free
 dual_dual_mix_constraints_return0_1S0 free
 dual_dual_mix_constraints_supply0_2S0 free
 dual_dual_mix_constraints_return0_2S0 free
 dual_dual_mix_constraints_supply0_3S0 free
 dual_dual_mix_constraints_return0_3S0 free
 dual_dual_mix_constraints_supply0_4S0 free
 dual_dual_mix_constraints_return0_4S0 free
 dual_dual_mix_constraints_supply0_5S0 free
 dual_dual_mix_constraints_return0_5S0 free
 dual_dual_heat_loss_supply0_0S0 free
 dual_dual_heat_loss_return0_0S0 free
 dual_dual_heat_loss_supply0_1S0 free
 dual_dual_heat_loss_return0_1S0 free
 dual_dual_heat_loss_supply0_2S0 free
 dual_dual_heat_loss_return0_2S0 free
 dual_dual_heat_loss_supply0_3S0 free
 dual_dual_heat_loss_return0_3S0 free
 dual_dual_heat_loss_supply0_4S0 free
 dual_dual_heat_loss_return0_4S0 free
Binaries
 dual_upper_well_output_min_0_t_0_S_0_binary
 dual_upper_well_output_max_0_t_0_S_0_binary
 dual_lower_well_output_min_0_t_0_S_0_binary
 dual_lower_well_output_max_0_t_0_S_0_binary
 dual_node_pressure_min_0_t_0_S_0_binary
 dual_node_pressure_max_0_t_0_S_0_binary
 dual_node_pressure_min_1_t_0_S_0_binary
 dual_node_pressure_max_1_t_0_S_0_binary
 dual_node_pressure_min_2_t_0_S_0_binary
 dual_node_pressure_max_2_t_0_S_0_binary
 dual_node_pressure_min_3_t_0_S_0_binary
 dual_node_pressure_max_3_t_0_S_0_binary
 dual_node_pressure_min_4_t_0_S_0_binary
 dual_node_pressure_max_4_t_0_S_0_binary
 dual_node_pressure_min_5_t_0_S_0_binary
 dual_node_pressure_max_5_t_0_S_0_binary
 dual_gas_flow_in_min0_t_0_S_0_binary dual_gas_flow_in_max0_t_0_S_0_binary
 dual_gas_flow_out_min0_t_0_S_0_binary
 dual_gas_flow_out_max0_t_0_S_0_binary dual_gas_flow_in_min1_t_0_S_0_binary
 dual_gas_flow_in_max1_t_0_S_0_binary dual_gas_flow_out_min1_t_0_S_0_binary
 dual_gas_flow_out_max1_t_0_S_0_binary dual_gas_flow_in_min2_t_0_S_0_binary
 dual_gas_flow_in_max2_t_0_S_0_binary dual_gas_flow_out_min2_t_0_S_0_binary
 dual_gas_flow_out_max2_t_0_S_0_binary dual_gas_flow_in_min3_t_0_S_0_binary
 dual_gas_flow_in_max3_t_0_S_0_binary dual_gas_flow_out_min3_t_0_S_0_binary
 dual_gas_flow_out_max3_t_0_S_0_binary dual_gas_flow_in_min4_t_0_S_0_binary
 dual_gas_flow_in_max4_t_0_S_0_binary dual_gas_flow_out_min4_t_0_S_0_binary
 dual_gas_flow_out_max4_t_0_S_0_binary
 dual_upper_chp_point_great_zero0_0S00_binary
 dual_upper_chp_point_less_one0_0S00_binary
 dual_upper_chp_point_great_zero0_0S01_binary
 dual_upper_chp_point_less_one0_0S01_binary
 dual_upper_chp_point_great_zero0_0S02_binary
 dual_upper_chp_point_less_one0_0S02_binary
 dual_upper_chp_point_great_zero0_0S03_binary
 dual_upper_chp_point_less_one0_0S03_binary
 dual_lower_chp_point_great_zero0_0S00_binary
 dual_lower_chp_point_less_one0_0S00_binary
 dual_lower_chp_point_great_zero0_0S01_binary
 dual_lower_chp_point_less_one0_0S01_binary
 dual_lower_chp_point_great_zero0_0S02_binary
 dual_lower_chp_point_less_one0_0S02_binary
 dual_lower_chp_point_great_zero0_0S03_binary
 dual_lower_chp_point_less_one0_0S03_binary
 dual_heater_supply_min0_0S0_binary dual_heater_supply_max0_0S0_binary
 dual_heater_return_min0_0S0_binary dual_heater_return_max0_0S0_binary
 dual_exchanger_supply_min0_0S0_binary
 dual_exchanger_supply_max0_0S0_binary
 dual_exchanger_return_min0_0S0_binary
 dual_exchanger_return_max0_0S0_binary
 dual_exchanger_supply_min0_1S0_binary
 dual_exchanger_supply_max0_1S0_binary
 dual_exchanger_return_min0_1S0_binary
 dual_exchanger_return_max0_1S0_binary
 dual_exchanger_supply_min0_2S0_binary
 dual_exchanger_supply_max0_2S0_binary
 dual_exchanger_return_min0_2S0_binary
 dual_exchanger_return_max0_2S0_binary
End
