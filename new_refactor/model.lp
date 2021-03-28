\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2.2 upper_well_output[0,0,0] + [
   - 2 upper_well_output[0,0,0] * dual_node_gas_balance[5,0,0] ] / 2 
Subject To
 node_gas_balance[0,0,0][EqualFeasible]: - gas_flow_out[4,0,0] = -0.5
 R1: dual_node_gas_balance[0,0,0] <= 20
 R2: dual_node_gas_balance[0,0,0] >= 1
 node_gas_balance[1,0,0][EqualFeasible]: gas_flow_in[4,0,0]
   - gas_flow_out[3,0,0] = -0.2
 R4: dual_node_gas_balance[1,0,0] <= 20
 R5: dual_node_gas_balance[1,0,0] >= 1
 node_gas_balance[2,0,0][EqualFeasible]: gas_flow_in[3,0,0]
   - gas_flow_out[2,0,0] = -0.3
 R7: dual_node_gas_balance[2,0,0] <= 20
 R8: dual_node_gas_balance[2,0,0] >= 1
 node_gas_balance[3,0,0][EqualFeasible]: gas_flow_in[2,0,0]
   - gas_flow_out[0,0,0] - gas_flow_out[1,0,0] = 0
 R10: dual_node_gas_balance[3,0,0] <= 20
 R11: dual_node_gas_balance[3,0,0] >= 1
 node_gas_balance[4,0,0][EqualFeasible]: - lower_well_output[0,0,0]
   + gas_flow_in[1,0,0] = 0
 R13: dual_node_gas_balance[4,0,0] <= 20
 R14: dual_node_gas_balance[4,0,0] >= 1
 node_gas_balance[5,0,0][EqualFeasible]: - upper_well_output[0,0,0]
   + gas_flow_in[0,0,0] = 0
 R16: dual_node_gas_balance[5,0,0] <= 20
 R17: dual_node_gas_balance[5,0,0] >= 1
 gas_linepack_equation[0,0,0][EqualFeasible]: - gas_linepack[0,0,0] = 0
 gas_linepack_with_time[0,0,0][EqualFeasible]: gas_flow_in[0,0,0]
   - gas_flow_out[0,0,0] = 0
 gas_linepack_equation[1,0,0][EqualFeasible]: - gas_linepack[1,0,0] = 0
 gas_linepack_with_time[1,0,0][EqualFeasible]: gas_flow_in[1,0,0]
   - gas_flow_out[1,0,0] = 0
 gas_linepack_equation[2,0,0][EqualFeasible]: - gas_linepack[2,0,0] = 0
 gas_linepack_with_time[2,0,0][EqualFeasible]: gas_flow_in[2,0,0]
   - gas_flow_out[2,0,0] = 0
 gas_linepack_equation[3,0,0][EqualFeasible]: - gas_linepack[3,0,0] = 0
 gas_linepack_with_time[3,0,0][EqualFeasible]: gas_flow_in[3,0,0]
   - gas_flow_out[3,0,0] = 0
 gas_linepack_equation[4,0,0][EqualFeasible]: - gas_linepack[4,0,0] = 0
 gas_linepack_with_time[4,0,0][EqualFeasible]: gas_flow_in[4,0,0]
   - gas_flow_out[4,0,0] = 0
 original_feasible_upper_well_output_min[0,0,0]: upper_well_output[0,0,0]
   >= 0
 original_feasible_M_upper_well_output_min[0,0,0]: upper_well_output[0,0,0]
   - 1e+07 upper_well_output_min[0,0,0]_binary <= 0
 dual_feasible_upper_well_output_min[0,0,0]: upper_well_output_min[0,0,0]
   >= 0
 dual_feasible_M_upper_well_output_min[0,0,0]: upper_well_output_min[0,0,0]
   + 1e+07 upper_well_output_min[0,0,0]_binary <= 1e+07
 original_feasible_upper_well_output_max[0,0,0]: - upper_well_output[0,0,0]
   >= -33.36
 original_feasible_M_upper_well_output_max[0,0,0]:
   - upper_well_output[0,0,0] - 1e+07 upper_well_output_max[0,0,0]_binary
   <= -33.36
 dual_feasible_upper_well_output_max[0,0,0]: upper_well_output_max[0,0,0]
   >= 0
 dual_feasible_M_upper_well_output_max[0,0,0]: upper_well_output_max[0,0,0]
   + 1e+07 upper_well_output_max[0,0,0]_binary <= 1e+07
 original_feasible_lower_well_output_min[0,0,0]: lower_well_output[0,0,0]
   >= 0
 original_feasible_M_lower_well_output_min[0,0,0]: lower_well_output[0,0,0]
   - 1e+07 lower_well_output_min[0,0,0]_binary <= 0
 dual_feasible_lower_well_output_min[0,0,0]: lower_well_output_min[0,0,0]
   >= 0
 dual_feasible_M_lower_well_output_min[0,0,0]: lower_well_output_min[0,0,0]
   + 1e+07 lower_well_output_min[0,0,0]_binary <= 1e+07
 original_feasible_lower_well_output_max[0,0,0]: - lower_well_output[0,0,0]
   >= 0
 original_feasible_M_lower_well_output_max[0,0,0]:
   - lower_well_output[0,0,0] - 1e+07 lower_well_output_max[0,0,0]_binary
   <= 0
 dual_feasible_lower_well_output_max[0,0,0]: lower_well_output_max[0,0,0]
   >= 0
 dual_feasible_M_lower_well_output_max[0,0,0]: lower_well_output_max[0,0,0]
   + 1e+07 lower_well_output_max[0,0,0]_binary <= 1e+07
 original_feasible_node_pressure_min[0,0,0]: gas_node_pressure[0,0,0] >= 0
 original_feasible_M_node_pressure_min[0,0,0]: gas_node_pressure[0,0,0]
   - 1e+07 node_pressure_min[0,0,0]_binary <= 0
 dual_feasible_node_pressure_min[0,0,0]: node_pressure_min[0,0,0] >= 0
 dual_feasible_M_node_pressure_min[0,0,0]: node_pressure_min[0,0,0]
   + 1e+07 node_pressure_min[0,0,0]_binary <= 1e+07
 original_feasible_node_pressure_max[0,0,0]: - gas_node_pressure[0,0,0]
   >= -82.8
 original_feasible_M_node_pressure_max[0,0,0]: - gas_node_pressure[0,0,0]
   - 1e+07 node_pressure_max[0,0,0]_binary <= -82.8
 dual_feasible_node_pressure_max[0,0,0]: node_pressure_max[0,0,0] >= 0
 dual_feasible_M_node_pressure_max[0,0,0]: node_pressure_max[0,0,0]
   + 1e+07 node_pressure_max[0,0,0]_binary <= 1e+07
 original_feasible_node_pressure_min[1,0,0]: gas_node_pressure[1,0,0] >= 0
 original_feasible_M_node_pressure_min[1,0,0]: gas_node_pressure[1,0,0]
   - 1e+07 node_pressure_min[1,0,0]_binary <= 0
 dual_feasible_node_pressure_min[1,0,0]: node_pressure_min[1,0,0] >= 0
 dual_feasible_M_node_pressure_min[1,0,0]: node_pressure_min[1,0,0]
   + 1e+07 node_pressure_min[1,0,0]_binary <= 1e+07
 original_feasible_node_pressure_max[1,0,0]: - gas_node_pressure[1,0,0]
   >= -82.8
 original_feasible_M_node_pressure_max[1,0,0]: - gas_node_pressure[1,0,0]
   - 1e+07 node_pressure_max[1,0,0]_binary <= -82.8
 dual_feasible_node_pressure_max[1,0,0]: node_pressure_max[1,0,0] >= 0
 dual_feasible_M_node_pressure_max[1,0,0]: node_pressure_max[1,0,0]
   + 1e+07 node_pressure_max[1,0,0]_binary <= 1e+07
 original_feasible_node_pressure_min[2,0,0]: gas_node_pressure[2,0,0] >= 0
 original_feasible_M_node_pressure_min[2,0,0]: gas_node_pressure[2,0,0]
   - 1e+07 node_pressure_min[2,0,0]_binary <= 0
 dual_feasible_node_pressure_min[2,0,0]: node_pressure_min[2,0,0] >= 0
 dual_feasible_M_node_pressure_min[2,0,0]: node_pressure_min[2,0,0]
   + 1e+07 node_pressure_min[2,0,0]_binary <= 1e+07
 original_feasible_node_pressure_max[2,0,0]: - gas_node_pressure[2,0,0]
   >= -82.8
 original_feasible_M_node_pressure_max[2,0,0]: - gas_node_pressure[2,0,0]
   - 1e+07 node_pressure_max[2,0,0]_binary <= -82.8
 dual_feasible_node_pressure_max[2,0,0]: node_pressure_max[2,0,0] >= 0
 dual_feasible_M_node_pressure_max[2,0,0]: node_pressure_max[2,0,0]
   + 1e+07 node_pressure_max[2,0,0]_binary <= 1e+07
 original_feasible_node_pressure_min[3,0,0]: gas_node_pressure[3,0,0] >= 0
 original_feasible_M_node_pressure_min[3,0,0]: gas_node_pressure[3,0,0]
   - 1e+07 node_pressure_min[3,0,0]_binary <= 0
 dual_feasible_node_pressure_min[3,0,0]: node_pressure_min[3,0,0] >= 0
 dual_feasible_M_node_pressure_min[3,0,0]: node_pressure_min[3,0,0]
   + 1e+07 node_pressure_min[3,0,0]_binary <= 1e+07
 original_feasible_node_pressure_max[3,0,0]: - gas_node_pressure[3,0,0]
   >= -82.8
 original_feasible_M_node_pressure_max[3,0,0]: - gas_node_pressure[3,0,0]
   - 1e+07 node_pressure_max[3,0,0]_binary <= -82.8
 dual_feasible_node_pressure_max[3,0,0]: node_pressure_max[3,0,0] >= 0
 dual_feasible_M_node_pressure_max[3,0,0]: node_pressure_max[3,0,0]
   + 1e+07 node_pressure_max[3,0,0]_binary <= 1e+07
 original_feasible_node_pressure_min[4,0,0]: gas_node_pressure[4,0,0] >= 0
 original_feasible_M_node_pressure_min[4,0,0]: gas_node_pressure[4,0,0]
   - 1e+07 node_pressure_min[4,0,0]_binary <= 0
 dual_feasible_node_pressure_min[4,0,0]: node_pressure_min[4,0,0] >= 0
 dual_feasible_M_node_pressure_min[4,0,0]: node_pressure_min[4,0,0]
   + 1e+07 node_pressure_min[4,0,0]_binary <= 1e+07
 original_feasible_node_pressure_max[4,0,0]: - gas_node_pressure[4,0,0]
   >= -82.8
 original_feasible_M_node_pressure_max[4,0,0]: - gas_node_pressure[4,0,0]
   - 1e+07 node_pressure_max[4,0,0]_binary <= -82.8
 dual_feasible_node_pressure_max[4,0,0]: node_pressure_max[4,0,0] >= 0
 dual_feasible_M_node_pressure_max[4,0,0]: node_pressure_max[4,0,0]
   + 1e+07 node_pressure_max[4,0,0]_binary <= 1e+07
 original_feasible_node_pressure_min[5,0,0]: gas_node_pressure[5,0,0] >= 0
 original_feasible_M_node_pressure_min[5,0,0]: gas_node_pressure[5,0,0]
   - 1e+07 node_pressure_min[5,0,0]_binary <= 0
 dual_feasible_node_pressure_min[5,0,0]: node_pressure_min[5,0,0] >= 0
 dual_feasible_M_node_pressure_min[5,0,0]: node_pressure_min[5,0,0]
   + 1e+07 node_pressure_min[5,0,0]_binary <= 1e+07
 original_feasible_node_pressure_max[5,0,0]: - gas_node_pressure[5,0,0]
   >= -82.8
 original_feasible_M_node_pressure_max[5,0,0]: - gas_node_pressure[5,0,0]
   - 1e+07 node_pressure_max[5,0,0]_binary <= -82.8
 dual_feasible_node_pressure_max[5,0,0]: node_pressure_max[5,0,0] >= 0
 dual_feasible_M_node_pressure_max[5,0,0]: node_pressure_max[5,0,0]
   + 1e+07 node_pressure_max[5,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_min[0,0,0]: gas_flow_in[0,0,0] >= 0
 original_feasible_M_gas_flow_in_min[0,0,0]: gas_flow_in[0,0,0]
   - 1e+07 gas_flow_in_min[0,0,0]_binary <= 0
 dual_feasible_gas_flow_in_min[0,0,0]: gas_flow_in_min[0,0,0] >= 0
 dual_feasible_M_gas_flow_in_min[0,0,0]: gas_flow_in_min[0,0,0]
   + 1e+07 gas_flow_in_min[0,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_max[0,0,0]: - gas_flow_in[0,0,0] >= -20
 original_feasible_M_gas_flow_in_max[0,0,0]: - gas_flow_in[0,0,0]
   - 1e+07 gas_flow_in_max[0,0,0]_binary <= -20
 dual_feasible_gas_flow_in_max[0,0,0]: gas_flow_in_max[0,0,0] >= 0
 dual_feasible_M_gas_flow_in_max[0,0,0]: gas_flow_in_max[0,0,0]
   + 1e+07 gas_flow_in_max[0,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_min[0,0,0]: gas_flow_out[0,0,0] >= 0
 original_feasible_M_gas_flow_out_min[0,0,0]: gas_flow_out[0,0,0]
   - 1e+07 gas_flow_out_min[0,0,0]_binary <= 0
 dual_feasible_gas_flow_out_min[0,0,0]: gas_flow_out_min[0,0,0] >= 0
 dual_feasible_M_gas_flow_out_min[0,0,0]: gas_flow_out_min[0,0,0]
   + 1e+07 gas_flow_out_min[0,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_max[0,0,0]: - gas_flow_out[0,0,0] >= -20
 original_feasible_M_gas_flow_out_max[0,0,0]: - gas_flow_out[0,0,0]
   - 1e+07 gas_flow_out_max[0,0,0]_binary <= -20
 dual_feasible_gas_flow_out_max[0,0,0]: gas_flow_out_max[0,0,0] >= 0
 dual_feasible_M_gas_flow_out_max[0,0,0]: gas_flow_out_max[0,0,0]
   + 1e+07 gas_flow_out_max[0,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_min[1,0,0]: gas_flow_in[1,0,0] >= 0
 original_feasible_M_gas_flow_in_min[1,0,0]: gas_flow_in[1,0,0]
   - 1e+07 gas_flow_in_min[1,0,0]_binary <= 0
 dual_feasible_gas_flow_in_min[1,0,0]: gas_flow_in_min[1,0,0] >= 0
 dual_feasible_M_gas_flow_in_min[1,0,0]: gas_flow_in_min[1,0,0]
   + 1e+07 gas_flow_in_min[1,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_max[1,0,0]: - gas_flow_in[1,0,0] >= -20
 original_feasible_M_gas_flow_in_max[1,0,0]: - gas_flow_in[1,0,0]
   - 1e+07 gas_flow_in_max[1,0,0]_binary <= -20
 dual_feasible_gas_flow_in_max[1,0,0]: gas_flow_in_max[1,0,0] >= 0
 dual_feasible_M_gas_flow_in_max[1,0,0]: gas_flow_in_max[1,0,0]
   + 1e+07 gas_flow_in_max[1,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_min[1,0,0]: gas_flow_out[1,0,0] >= 0
 original_feasible_M_gas_flow_out_min[1,0,0]: gas_flow_out[1,0,0]
   - 1e+07 gas_flow_out_min[1,0,0]_binary <= 0
 dual_feasible_gas_flow_out_min[1,0,0]: gas_flow_out_min[1,0,0] >= 0
 dual_feasible_M_gas_flow_out_min[1,0,0]: gas_flow_out_min[1,0,0]
   + 1e+07 gas_flow_out_min[1,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_max[1,0,0]: - gas_flow_out[1,0,0] >= -20
 original_feasible_M_gas_flow_out_max[1,0,0]: - gas_flow_out[1,0,0]
   - 1e+07 gas_flow_out_max[1,0,0]_binary <= -20
 dual_feasible_gas_flow_out_max[1,0,0]: gas_flow_out_max[1,0,0] >= 0
 dual_feasible_M_gas_flow_out_max[1,0,0]: gas_flow_out_max[1,0,0]
   + 1e+07 gas_flow_out_max[1,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_min[2,0,0]: gas_flow_in[2,0,0] >= 0
 original_feasible_M_gas_flow_in_min[2,0,0]: gas_flow_in[2,0,0]
   - 1e+07 gas_flow_in_min[2,0,0]_binary <= 0
 dual_feasible_gas_flow_in_min[2,0,0]: gas_flow_in_min[2,0,0] >= 0
 dual_feasible_M_gas_flow_in_min[2,0,0]: gas_flow_in_min[2,0,0]
   + 1e+07 gas_flow_in_min[2,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_max[2,0,0]: - gas_flow_in[2,0,0] >= -20
 original_feasible_M_gas_flow_in_max[2,0,0]: - gas_flow_in[2,0,0]
   - 1e+07 gas_flow_in_max[2,0,0]_binary <= -20
 dual_feasible_gas_flow_in_max[2,0,0]: gas_flow_in_max[2,0,0] >= 0
 dual_feasible_M_gas_flow_in_max[2,0,0]: gas_flow_in_max[2,0,0]
   + 1e+07 gas_flow_in_max[2,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_min[2,0,0]: gas_flow_out[2,0,0] >= 0
 original_feasible_M_gas_flow_out_min[2,0,0]: gas_flow_out[2,0,0]
   - 1e+07 gas_flow_out_min[2,0,0]_binary <= 0
 dual_feasible_gas_flow_out_min[2,0,0]: gas_flow_out_min[2,0,0] >= 0
 dual_feasible_M_gas_flow_out_min[2,0,0]: gas_flow_out_min[2,0,0]
   + 1e+07 gas_flow_out_min[2,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_max[2,0,0]: - gas_flow_out[2,0,0] >= -20
 original_feasible_M_gas_flow_out_max[2,0,0]: - gas_flow_out[2,0,0]
   - 1e+07 gas_flow_out_max[2,0,0]_binary <= -20
 dual_feasible_gas_flow_out_max[2,0,0]: gas_flow_out_max[2,0,0] >= 0
 dual_feasible_M_gas_flow_out_max[2,0,0]: gas_flow_out_max[2,0,0]
   + 1e+07 gas_flow_out_max[2,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_min[3,0,0]: gas_flow_in[3,0,0] >= 0
 original_feasible_M_gas_flow_in_min[3,0,0]: gas_flow_in[3,0,0]
   - 1e+07 gas_flow_in_min[3,0,0]_binary <= 0
 dual_feasible_gas_flow_in_min[3,0,0]: gas_flow_in_min[3,0,0] >= 0
 dual_feasible_M_gas_flow_in_min[3,0,0]: gas_flow_in_min[3,0,0]
   + 1e+07 gas_flow_in_min[3,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_max[3,0,0]: - gas_flow_in[3,0,0] >= -20
 original_feasible_M_gas_flow_in_max[3,0,0]: - gas_flow_in[3,0,0]
   - 1e+07 gas_flow_in_max[3,0,0]_binary <= -20
 dual_feasible_gas_flow_in_max[3,0,0]: gas_flow_in_max[3,0,0] >= 0
 dual_feasible_M_gas_flow_in_max[3,0,0]: gas_flow_in_max[3,0,0]
   + 1e+07 gas_flow_in_max[3,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_min[3,0,0]: gas_flow_out[3,0,0] >= 0
 original_feasible_M_gas_flow_out_min[3,0,0]: gas_flow_out[3,0,0]
   - 1e+07 gas_flow_out_min[3,0,0]_binary <= 0
 dual_feasible_gas_flow_out_min[3,0,0]: gas_flow_out_min[3,0,0] >= 0
 dual_feasible_M_gas_flow_out_min[3,0,0]: gas_flow_out_min[3,0,0]
   + 1e+07 gas_flow_out_min[3,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_max[3,0,0]: - gas_flow_out[3,0,0] >= -20
 original_feasible_M_gas_flow_out_max[3,0,0]: - gas_flow_out[3,0,0]
   - 1e+07 gas_flow_out_max[3,0,0]_binary <= -20
 dual_feasible_gas_flow_out_max[3,0,0]: gas_flow_out_max[3,0,0] >= 0
 dual_feasible_M_gas_flow_out_max[3,0,0]: gas_flow_out_max[3,0,0]
   + 1e+07 gas_flow_out_max[3,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_min[4,0,0]: gas_flow_in[4,0,0] >= 0
 original_feasible_M_gas_flow_in_min[4,0,0]: gas_flow_in[4,0,0]
   - 1e+07 gas_flow_in_min[4,0,0]_binary <= 0
 dual_feasible_gas_flow_in_min[4,0,0]: gas_flow_in_min[4,0,0] >= 0
 dual_feasible_M_gas_flow_in_min[4,0,0]: gas_flow_in_min[4,0,0]
   + 1e+07 gas_flow_in_min[4,0,0]_binary <= 1e+07
 original_feasible_gas_flow_in_max[4,0,0]: - gas_flow_in[4,0,0] >= -20
 original_feasible_M_gas_flow_in_max[4,0,0]: - gas_flow_in[4,0,0]
   - 1e+07 gas_flow_in_max[4,0,0]_binary <= -20
 dual_feasible_gas_flow_in_max[4,0,0]: gas_flow_in_max[4,0,0] >= 0
 dual_feasible_M_gas_flow_in_max[4,0,0]: gas_flow_in_max[4,0,0]
   + 1e+07 gas_flow_in_max[4,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_min[4,0,0]: gas_flow_out[4,0,0] >= 0
 original_feasible_M_gas_flow_out_min[4,0,0]: gas_flow_out[4,0,0]
   - 1e+07 gas_flow_out_min[4,0,0]_binary <= 0
 dual_feasible_gas_flow_out_min[4,0,0]: gas_flow_out_min[4,0,0] >= 0
 dual_feasible_M_gas_flow_out_min[4,0,0]: gas_flow_out_min[4,0,0]
   + 1e+07 gas_flow_out_min[4,0,0]_binary <= 1e+07
 original_feasible_gas_flow_out_max[4,0,0]: - gas_flow_out[4,0,0] >= -20
 original_feasible_M_gas_flow_out_max[4,0,0]: - gas_flow_out[4,0,0]
   - 1e+07 gas_flow_out_max[4,0,0]_binary <= -20
 dual_feasible_gas_flow_out_max[4,0,0]: gas_flow_out_max[4,0,0] >= 0
 dual_feasible_M_gas_flow_out_max[4,0,0]: gas_flow_out_max[4,0,0]
   + 1e+07 gas_flow_out_max[4,0,0]_binary <= 1e+07
 weymouth_left_aux[0,0,0][EqualFeasible]: 0.5 gas_flow_in[0,0,0]
   + 0.5 gas_flow_out[0,0,0] - weymouth_left_aux[0,0,0] = 0
 weymouth_left_aux[1,0,0][EqualFeasible]: 0.5 gas_flow_in[1,0,0]
   + 0.5 gas_flow_out[1,0,0] - weymouth_left_aux[1,0,0] = 0
 weymouth_left_aux[2,0,0][EqualFeasible]: 0.5 gas_flow_in[2,0,0]
   + 0.5 gas_flow_out[2,0,0] - weymouth_left_aux[2,0,0] = 0
 weymouth_left_aux[3,0,0][EqualFeasible]: 0.5 gas_flow_in[3,0,0]
   + 0.5 gas_flow_out[3,0,0] - weymouth_left_aux[3,0,0] = 0
 weymouth_left_aux[4,0,0][EqualFeasible]: 0.5 gas_flow_in[4,0,0]
   + 0.5 gas_flow_out[4,0,0] - weymouth_left_aux[4,0,0] = 0
 upper_gas_well_quoted_price_max0_well_0: upper_gas_quoted_price[0,0]
   <= 4.4
 weymouth_right_aux1[0,0,0][EqualFeasible]: - 2 gas_node_pressure[3,0,0]
   - gas_flow_in[0,0,0] - gas_flow_out[0,0,0] - weymouth_right_aux1[0,0,0]
   - pccp_relax[0,0,0] = 1
 weymouth_right_aux2[0,0,0][EqualFeasible]: - 2 gas_node_pressure[3,0,0]
   - gas_flow_in[0,0,0] - gas_flow_out[0,0,0] - weymouth_right_aux2[0,0,0]
   - pccp_relax[0,0,0] = 3
 weymouth_right_aux1[1,0,0][EqualFeasible]: - 2 gas_node_pressure[3,0,0]
   - gas_flow_in[1,0,0] - gas_flow_out[1,0,0] - weymouth_right_aux1[1,0,0]
   - pccp_relax[1,0,0] = 1
 weymouth_right_aux2[1,0,0][EqualFeasible]: - 2 gas_node_pressure[3,0,0]
   - gas_flow_in[1,0,0] - gas_flow_out[1,0,0] - weymouth_right_aux2[1,0,0]
   - pccp_relax[1,0,0] = 3
 weymouth_right_aux1[2,0,0][EqualFeasible]: - 2 gas_node_pressure[2,0,0]
   - gas_flow_in[2,0,0] - gas_flow_out[2,0,0] - weymouth_right_aux1[2,0,0]
   - pccp_relax[2,0,0] = 1
 weymouth_right_aux2[2,0,0][EqualFeasible]: - 2 gas_node_pressure[2,0,0]
   - gas_flow_in[2,0,0] - gas_flow_out[2,0,0] - weymouth_right_aux2[2,0,0]
   - pccp_relax[2,0,0] = 3
 weymouth_right_aux1[3,0,0][EqualFeasible]: - 2 gas_node_pressure[1,0,0]
   - gas_flow_in[3,0,0] - gas_flow_out[3,0,0] - weymouth_right_aux1[3,0,0]
   - pccp_relax[3,0,0] = 1
 weymouth_right_aux2[3,0,0][EqualFeasible]: - 2 gas_node_pressure[1,0,0]
   - gas_flow_in[3,0,0] - gas_flow_out[3,0,0] - weymouth_right_aux2[3,0,0]
   - pccp_relax[3,0,0] = 3
 weymouth_right_aux1[4,0,0][EqualFeasible]: - 2 gas_node_pressure[0,0,0]
   - gas_flow_in[4,0,0] - gas_flow_out[4,0,0] - weymouth_right_aux1[4,0,0]
   - pccp_relax[4,0,0] = 1
 weymouth_right_aux2[4,0,0][EqualFeasible]: - 2 gas_node_pressure[0,0,0]
   - gas_flow_in[4,0,0] - gas_flow_out[4,0,0] - weymouth_right_aux2[4,0,0]
   - pccp_relax[4,0,0] = 3
 upper_well_output[0,0,0]: upper_gas_quoted_price[0,0]
   - dual_node_gas_balance[5,0,0] - upper_well_output_min[0,0,0]
   + upper_well_output_max[0,0,0] = 0
 lower_well_output[0,0,0]: - dual_node_gas_balance[4,0,0]
   - lower_well_output_min[0,0,0] + lower_well_output_max[0,0,0] = -2.8
 gas_node_pressure[0,0,0]: - node_pressure_min[0,0,0]
   + node_pressure_max[0,0,0] - weymouth_left_soc[4,0,0]_left[1]
   - 2 dual_weymouth_right_aux1[4,0,0] - 2 dual_weymouth_right_aux2[4,0,0]
   = 0
 gas_node_pressure[1,0,0]: - node_pressure_min[1,0,0]
   + node_pressure_max[1,0,0] - weymouth_left_soc[3,0,0]_left[1]
   - weymouth_left_soc[4,0,0]_right[0] - 2 dual_weymouth_right_aux1[3,0,0]
   - 2 dual_weymouth_right_aux2[3,0,0]
   - 4 weymouth_right_soc[4,0,0]_left[0] = 0
 gas_node_pressure[2,0,0]: - node_pressure_min[2,0,0]
   + node_pressure_max[2,0,0] - weymouth_left_soc[2,0,0]_left[1]
   - weymouth_left_soc[3,0,0]_right[0] - 2 dual_weymouth_right_aux1[2,0,0]
   - 2 dual_weymouth_right_aux2[2,0,0]
   - 4 weymouth_right_soc[3,0,0]_left[0] = 0
 gas_node_pressure[3,0,0]: - node_pressure_min[3,0,0]
   + node_pressure_max[3,0,0] - weymouth_left_soc[0,0,0]_left[1]
   - weymouth_left_soc[1,0,0]_left[1] - weymouth_left_soc[2,0,0]_right[0]
   - 2 dual_weymouth_right_aux1[0,0,0] - 2 dual_weymouth_right_aux2[0,0,0]
   - 2 dual_weymouth_right_aux1[1,0,0] - 2 dual_weymouth_right_aux2[1,0,0]
   - 4 weymouth_right_soc[2,0,0]_left[0] = 0
 gas_node_pressure[4,0,0]: - node_pressure_min[4,0,0]
   + node_pressure_max[4,0,0] - weymouth_left_soc[1,0,0]_right[0]
   - 4 weymouth_right_soc[1,0,0]_left[0] = 0
 gas_node_pressure[5,0,0]: - node_pressure_min[5,0,0]
   + node_pressure_max[5,0,0] - weymouth_left_soc[0,0,0]_right[0]
   - 4 weymouth_right_soc[0,0,0]_left[0] = 0
 gas_flow_in[0,0,0]: dual_node_gas_balance[5,0,0]
   + dual_gas_linepack_with_time[0,0,0] - gas_flow_in_min[0,0,0]
   + gas_flow_in_max[0,0,0] + 0.5 dual_weymouth_left_aux[0,0,0]
   - dual_weymouth_right_aux1[0,0,0] - dual_weymouth_right_aux2[0,0,0] = 0
 gas_flow_in[1,0,0]: dual_node_gas_balance[4,0,0]
   + dual_gas_linepack_with_time[1,0,0] - gas_flow_in_min[1,0,0]
   + gas_flow_in_max[1,0,0] + 0.5 dual_weymouth_left_aux[1,0,0]
   - dual_weymouth_right_aux1[1,0,0] - dual_weymouth_right_aux2[1,0,0] = 0
 gas_flow_in[2,0,0]: dual_node_gas_balance[3,0,0]
   + dual_gas_linepack_with_time[2,0,0] - gas_flow_in_min[2,0,0]
   + gas_flow_in_max[2,0,0] + 0.5 dual_weymouth_left_aux[2,0,0]
   - dual_weymouth_right_aux1[2,0,0] - dual_weymouth_right_aux2[2,0,0] = 0
 gas_flow_in[3,0,0]: dual_node_gas_balance[2,0,0]
   + dual_gas_linepack_with_time[3,0,0] - gas_flow_in_min[3,0,0]
   + gas_flow_in_max[3,0,0] + 0.5 dual_weymouth_left_aux[3,0,0]
   - dual_weymouth_right_aux1[3,0,0] - dual_weymouth_right_aux2[3,0,0] = 0
 gas_flow_in[4,0,0]: dual_node_gas_balance[1,0,0]
   + dual_gas_linepack_with_time[4,0,0] - gas_flow_in_min[4,0,0]
   + gas_flow_in_max[4,0,0] + 0.5 dual_weymouth_left_aux[4,0,0]
   - dual_weymouth_right_aux1[4,0,0] - dual_weymouth_right_aux2[4,0,0] = 0
 gas_flow_out[0,0,0]: - dual_node_gas_balance[3,0,0]
   - dual_gas_linepack_with_time[0,0,0] - gas_flow_out_min[0,0,0]
   + gas_flow_out_max[0,0,0] + 0.5 dual_weymouth_left_aux[0,0,0]
   - dual_weymouth_right_aux1[0,0,0] - dual_weymouth_right_aux2[0,0,0] = 0
 gas_flow_out[1,0,0]: - dual_node_gas_balance[3,0,0]
   - dual_gas_linepack_with_time[1,0,0] - gas_flow_out_min[1,0,0]
   + gas_flow_out_max[1,0,0] + 0.5 dual_weymouth_left_aux[1,0,0]
   - dual_weymouth_right_aux1[1,0,0] - dual_weymouth_right_aux2[1,0,0] = 0
 gas_flow_out[2,0,0]: - dual_node_gas_balance[2,0,0]
   - dual_gas_linepack_with_time[2,0,0] - gas_flow_out_min[2,0,0]
   + gas_flow_out_max[2,0,0] + 0.5 dual_weymouth_left_aux[2,0,0]
   - dual_weymouth_right_aux1[2,0,0] - dual_weymouth_right_aux2[2,0,0] = 0
 gas_flow_out[3,0,0]: - dual_node_gas_balance[1,0,0]
   - dual_gas_linepack_with_time[3,0,0] - gas_flow_out_min[3,0,0]
   + gas_flow_out_max[3,0,0] + 0.5 dual_weymouth_left_aux[3,0,0]
   - dual_weymouth_right_aux1[3,0,0] - dual_weymouth_right_aux2[3,0,0] = 0
 gas_flow_out[4,0,0]: - dual_node_gas_balance[0,0,0]
   - dual_gas_linepack_with_time[4,0,0] - gas_flow_out_min[4,0,0]
   + gas_flow_out_max[4,0,0] + 0.5 dual_weymouth_left_aux[4,0,0]
   - dual_weymouth_right_aux1[4,0,0] - dual_weymouth_right_aux2[4,0,0] = 0
 gas_linepack[0,0,0]: - dual_gas_linepack_equation[0,0,0] = 0
 gas_linepack[1,0,0]: - dual_gas_linepack_equation[1,0,0] = 0
 gas_linepack[2,0,0]: - dual_gas_linepack_equation[2,0,0] = 0
 gas_linepack[3,0,0]: - dual_gas_linepack_equation[3,0,0] = 0
 gas_linepack[4,0,0]: - dual_gas_linepack_equation[4,0,0] = 0
 weymouth_left_soc[0,0,0][Original]: [ gas_node_pressure[3,0,0] ^2
   - gas_node_pressure[5,0,0] ^2 + weymouth_left_aux[0,0,0] ^2 ] <= 0
 weymouth_left_soc[0,0,0][Dual]: [ weymouth_left_soc[0,0,0]_left[0] ^2
   + weymouth_left_soc[0,0,0]_left[1] ^2
   - weymouth_left_soc[0,0,0]_right[0] ^2 ] <= 0
 weymouth_left_soc[0,0,0][Lagrange]: [
   gas_node_pressure[3,0,0] * weymouth_left_soc[0,0,0]_left[1]
   + gas_node_pressure[5,0,0] * weymouth_left_soc[0,0,0]_right[0]
   + weymouth_left_aux[0,0,0] * weymouth_left_soc[0,0,0]_left[0] ] = 0
 weymouth_left_soc[1,0,0][Original]: [ gas_node_pressure[3,0,0] ^2
   - gas_node_pressure[4,0,0] ^2 + weymouth_left_aux[1,0,0] ^2 ] <= 0
 weymouth_left_soc[1,0,0][Dual]: [ weymouth_left_soc[1,0,0]_left[0] ^2
   + weymouth_left_soc[1,0,0]_left[1] ^2
   - weymouth_left_soc[1,0,0]_right[0] ^2 ] <= 0
 weymouth_left_soc[1,0,0][Lagrange]: [
   gas_node_pressure[3,0,0] * weymouth_left_soc[1,0,0]_left[1]
   + gas_node_pressure[4,0,0] * weymouth_left_soc[1,0,0]_right[0]
   + weymouth_left_aux[1,0,0] * weymouth_left_soc[1,0,0]_left[0] ] = 0
 weymouth_left_soc[2,0,0][Original]: [ gas_node_pressure[2,0,0] ^2
   - gas_node_pressure[3,0,0] ^2 + weymouth_left_aux[2,0,0] ^2 ] <= 0
 weymouth_left_soc[2,0,0][Dual]: [ weymouth_left_soc[2,0,0]_left[0] ^2
   + weymouth_left_soc[2,0,0]_left[1] ^2
   - weymouth_left_soc[2,0,0]_right[0] ^2 ] <= 0
 weymouth_left_soc[2,0,0][Lagrange]: [
   gas_node_pressure[2,0,0] * weymouth_left_soc[2,0,0]_left[1]
   + gas_node_pressure[3,0,0] * weymouth_left_soc[2,0,0]_right[0]
   + weymouth_left_aux[2,0,0] * weymouth_left_soc[2,0,0]_left[0] ] = 0
 weymouth_left_soc[3,0,0][Original]: [ gas_node_pressure[1,0,0] ^2
   - gas_node_pressure[2,0,0] ^2 + weymouth_left_aux[3,0,0] ^2 ] <= 0
 weymouth_left_soc[3,0,0][Dual]: [ weymouth_left_soc[3,0,0]_left[0] ^2
   + weymouth_left_soc[3,0,0]_left[1] ^2
   - weymouth_left_soc[3,0,0]_right[0] ^2 ] <= 0
 weymouth_left_soc[3,0,0][Lagrange]: [
   gas_node_pressure[1,0,0] * weymouth_left_soc[3,0,0]_left[1]
   + gas_node_pressure[2,0,0] * weymouth_left_soc[3,0,0]_right[0]
   + weymouth_left_aux[3,0,0] * weymouth_left_soc[3,0,0]_left[0] ] = 0
 weymouth_left_soc[4,0,0][Original]: [ gas_node_pressure[0,0,0] ^2
   - gas_node_pressure[1,0,0] ^2 + weymouth_left_aux[4,0,0] ^2 ] <= 0
 weymouth_left_soc[4,0,0][Dual]: [ weymouth_left_soc[4,0,0]_left[0] ^2
   + weymouth_left_soc[4,0,0]_left[1] ^2
   - weymouth_left_soc[4,0,0]_right[0] ^2 ] <= 0
 weymouth_left_soc[4,0,0][Lagrange]: [
   gas_node_pressure[0,0,0] * weymouth_left_soc[4,0,0]_left[1]
   + gas_node_pressure[1,0,0] * weymouth_left_soc[4,0,0]_right[0]
   + weymouth_left_aux[4,0,0] * weymouth_left_soc[4,0,0]_left[0] ] = 0
 [Original]weymouth_right_soc[0,0,0]: [ 4 gas_node_pressure[5,0,0] ^2
   + weymouth_right_aux1[0,0,0] ^2 - weymouth_right_aux2[0,0,0] ^2 ] <= 0
 [Dual]weymouth_right_soc[0,0,0]: [ 4 weymouth_right_soc[0,0,0]_left[0] ^2
   + weymouth_right_soc[0,0,0]_left[1] ^2
   - weymouth_right_soc[0,0,0]_right[0] ^2 ] <= 0
 [Lagrange]weymouth_right_soc[0,0,0]: [
   4 gas_node_pressure[5,0,0] * weymouth_right_soc[0,0,0]_left[0]
   + weymouth_right_aux1[0,0,0] * weymouth_right_soc[0,0,0]_left[1]
   + weymouth_right_aux2[0,0,0] * weymouth_right_soc[0,0,0]_right[0] ] = 0
 [Original]weymouth_right_soc[1,0,0]: [ 4 gas_node_pressure[4,0,0] ^2
   + weymouth_right_aux1[1,0,0] ^2 - weymouth_right_aux2[1,0,0] ^2 ] <= 0
 [Dual]weymouth_right_soc[1,0,0]: [ 4 weymouth_right_soc[1,0,0]_left[0] ^2
   + weymouth_right_soc[1,0,0]_left[1] ^2
   - weymouth_right_soc[1,0,0]_right[0] ^2 ] <= 0
 [Lagrange]weymouth_right_soc[1,0,0]: [
   4 gas_node_pressure[4,0,0] * weymouth_right_soc[1,0,0]_left[0]
   + weymouth_right_aux1[1,0,0] * weymouth_right_soc[1,0,0]_left[1]
   + weymouth_right_aux2[1,0,0] * weymouth_right_soc[1,0,0]_right[0] ] = 0
 [Original]weymouth_right_soc[2,0,0]: [ 4 gas_node_pressure[3,0,0] ^2
   + weymouth_right_aux1[2,0,0] ^2 - weymouth_right_aux2[2,0,0] ^2 ] <= 0
 [Dual]weymouth_right_soc[2,0,0]: [ 4 weymouth_right_soc[2,0,0]_left[0] ^2
   + weymouth_right_soc[2,0,0]_left[1] ^2
   - weymouth_right_soc[2,0,0]_right[0] ^2 ] <= 0
 [Lagrange]weymouth_right_soc[2,0,0]: [
   4 gas_node_pressure[3,0,0] * weymouth_right_soc[2,0,0]_left[0]
   + weymouth_right_aux1[2,0,0] * weymouth_right_soc[2,0,0]_left[1]
   + weymouth_right_aux2[2,0,0] * weymouth_right_soc[2,0,0]_right[0] ] = 0
 [Original]weymouth_right_soc[3,0,0]: [ 4 gas_node_pressure[2,0,0] ^2
   + weymouth_right_aux1[3,0,0] ^2 - weymouth_right_aux2[3,0,0] ^2 ] <= 0
 [Dual]weymouth_right_soc[3,0,0]: [ 4 weymouth_right_soc[3,0,0]_left[0] ^2
   + weymouth_right_soc[3,0,0]_left[1] ^2
   - weymouth_right_soc[3,0,0]_right[0] ^2 ] <= 0
 [Lagrange]weymouth_right_soc[3,0,0]: [
   4 gas_node_pressure[2,0,0] * weymouth_right_soc[3,0,0]_left[0]
   + weymouth_right_aux1[3,0,0] * weymouth_right_soc[3,0,0]_left[1]
   + weymouth_right_aux2[3,0,0] * weymouth_right_soc[3,0,0]_right[0] ] = 0
 [Original]weymouth_right_soc[4,0,0]: [ 4 gas_node_pressure[1,0,0] ^2
   + weymouth_right_aux1[4,0,0] ^2 - weymouth_right_aux2[4,0,0] ^2 ] <= 0
 [Dual]weymouth_right_soc[4,0,0]: [ 4 weymouth_right_soc[4,0,0]_left[0] ^2
   + weymouth_right_soc[4,0,0]_left[1] ^2
   - weymouth_right_soc[4,0,0]_right[0] ^2 ] <= 0
 [Lagrange]weymouth_right_soc[4,0,0]: [
   4 gas_node_pressure[1,0,0] * weymouth_right_soc[4,0,0]_left[0]
   + weymouth_right_aux1[4,0,0] * weymouth_right_soc[4,0,0]_left[1]
   + weymouth_right_aux2[4,0,0] * weymouth_right_soc[4,0,0]_right[0] ] = 0
Bounds
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
 dual_node_gas_balance[0,0,0] free
 dual_node_gas_balance[1,0,0] free
 dual_node_gas_balance[2,0,0] free
 dual_node_gas_balance[3,0,0] free
 dual_node_gas_balance[4,0,0] free
 dual_node_gas_balance[5,0,0] free
 dual_gas_linepack_equation[0,0,0] free
 dual_gas_linepack_with_time[0,0,0] free
 dual_gas_linepack_equation[1,0,0] free
 dual_gas_linepack_with_time[1,0,0] free
 dual_gas_linepack_equation[2,0,0] free
 dual_gas_linepack_with_time[2,0,0] free
 dual_gas_linepack_equation[3,0,0] free
 dual_gas_linepack_with_time[3,0,0] free
 dual_gas_linepack_equation[4,0,0] free
 dual_gas_linepack_with_time[4,0,0] free
 dual_weymouth_left_aux[0,0,0] free
 weymouth_left_soc[0,0,0]_left[0] free
 weymouth_left_soc[0,0,0]_left[1] free
 dual_weymouth_left_aux[1,0,0] free
 weymouth_left_soc[1,0,0]_left[0] free
 weymouth_left_soc[1,0,0]_left[1] free
 dual_weymouth_left_aux[2,0,0] free
 weymouth_left_soc[2,0,0]_left[0] free
 weymouth_left_soc[2,0,0]_left[1] free
 dual_weymouth_left_aux[3,0,0] free
 weymouth_left_soc[3,0,0]_left[0] free
 weymouth_left_soc[3,0,0]_left[1] free
 dual_weymouth_left_aux[4,0,0] free
 weymouth_left_soc[4,0,0]_left[0] free
 weymouth_left_soc[4,0,0]_left[1] free
 dual_weymouth_right_aux1[0,0,0] free
 dual_weymouth_right_aux2[0,0,0] free
 weymouth_right_soc[0,0,0]_left[0] free
 weymouth_right_soc[0,0,0]_left[1] free
 dual_weymouth_right_aux1[1,0,0] free
 dual_weymouth_right_aux2[1,0,0] free
 weymouth_right_soc[1,0,0]_left[0] free
 weymouth_right_soc[1,0,0]_left[1] free
 dual_weymouth_right_aux1[2,0,0] free
 dual_weymouth_right_aux2[2,0,0] free
 weymouth_right_soc[2,0,0]_left[0] free
 weymouth_right_soc[2,0,0]_left[1] free
 dual_weymouth_right_aux1[3,0,0] free
 dual_weymouth_right_aux2[3,0,0] free
 weymouth_right_soc[3,0,0]_left[0] free
 weymouth_right_soc[3,0,0]_left[1] free
 dual_weymouth_right_aux1[4,0,0] free
 dual_weymouth_right_aux2[4,0,0] free
 weymouth_right_soc[4,0,0]_left[0] free
 weymouth_right_soc[4,0,0]_left[1] free
Binaries
 upper_well_output_min[0,0,0]_binary upper_well_output_max[0,0,0]_binary
 lower_well_output_min[0,0,0]_binary lower_well_output_max[0,0,0]_binary
 node_pressure_min[0,0,0]_binary node_pressure_max[0,0,0]_binary
 node_pressure_min[1,0,0]_binary node_pressure_max[1,0,0]_binary
 node_pressure_min[2,0,0]_binary node_pressure_max[2,0,0]_binary
 node_pressure_min[3,0,0]_binary node_pressure_max[3,0,0]_binary
 node_pressure_min[4,0,0]_binary node_pressure_max[4,0,0]_binary
 node_pressure_min[5,0,0]_binary node_pressure_max[5,0,0]_binary
 gas_flow_in_min[0,0,0]_binary gas_flow_in_max[0,0,0]_binary
 gas_flow_out_min[0,0,0]_binary gas_flow_out_max[0,0,0]_binary
 gas_flow_in_min[1,0,0]_binary gas_flow_in_max[1,0,0]_binary
 gas_flow_out_min[1,0,0]_binary gas_flow_out_max[1,0,0]_binary
 gas_flow_in_min[2,0,0]_binary gas_flow_in_max[2,0,0]_binary
 gas_flow_out_min[2,0,0]_binary gas_flow_out_max[2,0,0]_binary
 gas_flow_in_min[3,0,0]_binary gas_flow_in_max[3,0,0]_binary
 gas_flow_out_min[3,0,0]_binary gas_flow_out_max[3,0,0]_binary
 gas_flow_in_min[4,0,0]_binary gas_flow_in_max[4,0,0]_binary
 gas_flow_out_min[4,0,0]_binary gas_flow_out_max[4,0,0]_binary
End
