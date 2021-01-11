import gurobipy as gurobi
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd

start1 = time.time()
# 气网差分的优化程序
# 单管道参数
Nc = 1
T = 800 * 1
Time = T
L = 8000
Node = 26 * Nc
delta_T = 1
Lij = 367 / Nc
# gas_load = [120] * 2 + [150] * 100 + [130] * 100+ [140] * 100+ [160] * 100+ [150] * 100+ [120] * 100+ [120] * 100+ [120] * 100+ [110] * 100+ [130] * 100+ [130] * 100+ [130] * 100
# gas_load = np.array([[1] * 50 + [1.2] * 300 + [1.2] * 300 + [1.2] * 300 + [1.2] * 300 + [1.2] * 3000,
#                      [1] * 50 + [1] * 300 + [1] * 300 + [1] * 300 + [1] * 300 + [1] * 3000])
t_1=150
gas_load = np.array([[1.3570 ] * t_1 + [1.8113 ] * t_1 + [2.1450] * t_1 + [2.4789] * t_1+ [1.1441] * t_1 + [1.3569] * 3000,
                     [1] * t_1 + [1] * t_1+ [1] * t_1 + [1] * t_1 + [1] * t_1 + [1] * 3000])

# 1.3570     1.8113    2.1450  2.4789  1.1441  1.3569
# 网络参数
# 气源     节点
gas_holder = np.array([[0]])
# 管道
# net_pipe=np.array( ['start','end','length','diam','index'])
gas_net_pipe = np.array([[0, 1, 8000, 0.5, 1],
                         [1, 2, 8000, 0.5, 2],
                         [1, 3, 8000, 0.5, 3],
                         [2, 4, 8000, 0.5, 4],
                         [3, 4, 8000, 0.5, 5],
                         [4, 5, 8000, 0.5, 6],
                         [5, 6, 8000, 0.5, 7],
                         [6, 7, 8000, 0.5, 8],
                         [6, 8, 8000, 0.5, 8],
                         ])
# [ 2, 4, 8000, 0.5, 1]])
# 节点
gas_net_node = np.array([   [0], [1], [2], [3] , [4], [5], [6], [7], [8] ])
# 负荷 负荷量
gas_net_demand = []
for i in range(2):
    gas_net_demand.append(gas_load[i, 0:T])
gas_net_demand = np.array(gas_net_demand)
# 负荷节点
gas_net_load_info = np.array([[7], [8]])
# 负荷气需求
# gas_net_load = np.dot ( gas_net_demand , gas_net_load_info[1] )
# 读取网络数据

info_pipe = np.shape(gas_net_pipe)
Pipe_num_net = info_pipe[0]  # 网络中管道的个数
info_node = np.shape(gas_net_node)
Node_num_net = info_node[0]  # 网络中节点数目
info_load = np.shape(gas_net_load_info)
Load_num_net = info_load[0]  # 网络中负荷数目
info_well = np.shape(gas_holder)
Well_num_net = info_well[0]  # 网络中气源数目

Pressure_init = 4e+05
Lambda = 0.07 * 1
w_av = 2.55 * 1
dij = 0.5
Aij = dij * dij / 4 * 3.1415926
K1 = delta_T / Lij / Aij
K2 = Lambda * w_av * delta_T / 4 / Aij / dij
c2 = 367 * 367
K_p0 = Lambda * w_av * (gas_load[0, 0] + gas_load[1, 0]) / 2 / dij / Aij / c2
K_p1 = Lambda * w_av * gas_load[0, 0] / 2 / dij / Aij / c2
K_p2 = Lambda * w_av * gas_load[1, 0] / 2 / dij / Aij / c2
model = gurobi.Model()
flow = model.addVars(Pipe_num_net, Node, T, lb=0, ub=200, name='gas_flow_out')
node_pressure = model.addVars(Pipe_num_net, Node, T, lb=0, ub=9000000 / c2, name='node_pressure')
well_output = model.addVars(Well_num_net, T, name='well_output')
# model.addConstr(flow[0,0, 0] == gas_load[0])

# 边界条件
# 首端气压恒定 末端流量已知
for t in range(T):
    model.addConstr(c2 * node_pressure[0, 0, t] == Pressure_init)  #
    model.addConstr(flow[1, Node - 1, t] == gas_net_demand[0, t])  # 第1根管道末端流量 等于demand0
    model.addConstr(flow[2, Node - 1, t] == gas_net_demand[1, t])  # 第2根管道末端流量 等于demand1
# 初始条件
# 每根管道的流量为初始负荷  每根管道的初始气压为首节点气压-K * n
# Pre_down= Pressure_init / c2 - K * Node * Lij
Pre_down = K_p0 * (Node - 1) * Lij
# for p in range(Pipe_num_net-1): # 管道0 ，1的初始条件
#     for node in range(Node):
#         model.addConstr(flow[p,node, 0] == gas_load[0,0]) # 沿线流量初始条件
#         model.addConstr(node_pressure[p,node, 0] == Pressure_init / c2 -Pre_down * p - K * node * Lij)# 沿线气压初始条件 #分支的不能直接用
# 管道0的初始条件
for node in range(Node):
    model.addConstr(flow[0, node, 0] == gas_load[0, 0] + gas_load[1, 0])  # 沿线流量初始条件
    model.addConstr(node_pressure[0, node, 0] == Pressure_init / c2 - Pre_down * 0 - K_p0 * node * Lij)
# 管道1的初始条件
for node in range(Node):
    model.addConstr(flow[1, node, 0] == gas_load[0, 0])  # 沿线流量初始条件
    model.addConstr(node_pressure[1, node, 0] == Pressure_init / c2 - Pre_down * 1 - K_p1 * node * Lij)
# 管道2的初始条件
for node in range(Node):
    model.addConstr(flow[2, node, 0] == gas_load[1, 0])  # 沿线流量初始条件
    model.addConstr(node_pressure[2, node, 0] == Pressure_init / c2 - Pre_down * 1 - K_p2 * node * Lij)
# 差分方程约束
for p in range(Pipe_num_net):
    for n in range(Node - 1):
        for t in range(T - 1):
            model.addConstr(
                lhs=node_pressure[p, n + 1, t + 1] + node_pressure[p, n, t + 1] - node_pressure[p, n + 1, t] -
                    node_pressure[p, n, t],
                rhs=-1 * K1 * (flow[p, n + 1, t + 1] - flow[p, n, t + 1] + flow[p, n + 1, t] - flow[p, n, t]),
                sense=gurobi.GRB.EQUAL)
            model.addConstr(
                lhs=(flow[p, n + 1, t + 1] + flow[p, n, t + 1] - flow[p, n + 1, t] - flow[p, n, t]) / Aij +
                    (c2 * node_pressure[p, n + 1, t + 1] - c2 * node_pressure[p, n, t + 1] + c2 * node_pressure[
                        p, n + 1, t] -
                     c2 * node_pressure[p, n, t]) / Lij * delta_T,
                rhs=-1 * (flow[p, n + 1, t + 1] + flow[p, n, t + 1] + flow[p, n + 1, t] + flow[p, n, t]) * K2,
                sense=gurobi.GRB.EQUAL)

# 节点1 管道0 1
for t in range(T):
    model.addConstr(node_pressure[0, Node - 1, t] == node_pressure[1, 0, t])  # 每个管道出口和下个管道入口的气压
# 节点1 管道0 2
for t in range(T):
    model.addConstr(node_pressure[0, Node - 1, t] == node_pressure[2, 0, t])

model.update()


def find_f_pipeout(node):  # find all pipe out connected with node node  2 ==> 2,3
    a1 = np.where(gas_net_pipe[:, 0] == node)
    if a1[0].size == 0:
        return np.array([[0] * Time])
    fout = []
    for n in a1[0]:
        r = []
        for t in range(Time):
            r.append(flow[n, 0, t])
        fout.append(r)
    return fout


def find_f_pipein(node):  # find all pipe in connected with node node  2 ==> 1
    a1 = np.where(gas_net_pipe[:, 1] == node)
    if a1[0].size == 0:
        return np.array([[0] * Time])
    fin = []
    for n in (a1[0]):
        r = []
        for t in range(Time):
            r.append(flow[n, Node - 1, t])
        fin.append(r)
    return fin


def find_f_load(node):
    a1 = np.where(gas_net_load_info[:, 0] == node)
    if a1[0].size == 0:
        return np.array([[0] * Time])
    fload = []
    for n in (a1[0]):
        r = []
        for t in range(Time):
            r.append(gas_load[n, t])
        fload.append(r)
    return fload


def find_f_well(node):
    a1 = np.where(gas_holder[:, 0] == node)
    if a1[0].size == 0:
        return np.array([[0] * Time])
    fwell = []
    for n in (a1[0]):
        r = []
        for t in range(Time):
            r.append(flow[0, 0, t])
        fwell.append(r)
    return fwell


for node in range(Node_num_net):
    for t in range(Time):
        well = np.array(find_f_well(node))
        pipe_in = np.array(find_f_pipein(node))
        pipe_out = np.array(find_f_pipeout(node))
        load = np.array(find_f_load(node))
        model.addConstr((sum(well[:, t]) + sum(pipe_in[:, t])) == sum(load[:, t]) + sum(pipe_out[:, t]))

start2 = time.time()
model.setObjective(0)
model.optimize()

end2 = time.time()
# plt M
M1 = []
M22 = []
M23 = []
M21 = []
M4 = []
M3 = []
for t in range(T):
    M1.append(flow[0, 0, t].getAttr('X'))
    M22.append(flow[1, 0, t].getAttr('X'))
    M23.append(flow[2, 0, t].getAttr('X'))
    M4.append(flow[2, Node - 1, t].getAttr('X'))
    M3.append(flow[1, Node - 1, t].getAttr('X'))
    M21.append(flow[0, Node - 1, t].getAttr('X'))
plt.plot(M1, label='M1')
plt.plot(M22, label='M22')
plt.plot(M23, label='M23')
plt.plot(M21, label='M21')
plt.plot(M4, label='M4')
plt.plot(M3, label='M3')
plt.legend(fontsize='x-large')
plt.xlabel("time(s)")
plt.ylabel("kg/s")
plt.title('Massfolw')
plt.show()
# df = pd.DataFrame(M1)
# df.to_csv("D:\matlab eg\GF\常系数矩阵测试\8km\opt_gas_source_2626.txt",index=0)

# plt P
P1 = []
P2 = []
P3 = []
P4 = []
T1 = T
Pressure_source = [Pressure_init] * T
for t in range(T1):
    P2.append(node_pressure[0, Node - 1, t].getAttr('X'))
    P3.append(node_pressure[1, Node - 1, t].getAttr('X'))
    P4.append(node_pressure[2, Node - 1, t].getAttr('X'))
    P1.append(node_pressure[0, 0, t].getAttr('X'))
for t in range(T1):
    P1[t] = P1[t] * c2
    P2[t] = P2[t] * c2
    P3[t] = P3[t] * c2
    P4[t] = P4[t] * c2
plt.plot(P2, label='P2')
plt.plot(P3, label='P3')
plt.plot(P4, label='P4')
plt.plot(P1, label='P1')
plt.legend(fontsize='x-large')
plt.xlabel("time(s)")
plt.ylabel("Pressure(pa)")
plt.show()


# df = pd.DataFrame(b)
# df.to_csv("D:\matlab eg\GF\常系数矩阵测试\8km\opt_Pressure_load_2626.txt",index=0)

def get_pressure_distribution_of_t(t):
    a = []
    for node in range(Node):
        a.append(node_pressure[0, node, t].getAttr('X'))
    plt.title('pressure_distribution_of_time:' + str(t))
    plt.plot(a)
    plt.show()


end1 = time.time()
print('cal_time_of_opti: %s Seconds' % (end1 - start1))
print('time1: %s Seconds' % (end2 - start2))
# 数据保
uu = 0
if uu == 1:
    df = pd.DataFrame(M1)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\M1.txt", index=0)
    df = pd.DataFrame(M3)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\M3.txt", index=0)
    df = pd.DataFrame(M4)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\M4.txt", index=0)
    df = pd.DataFrame(M21)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\M21.txt", index=0)
    df = pd.DataFrame(M22)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\M22.txt", index=0)
    df = pd.DataFrame(M23)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\M23.txt", index=0)
    df = pd.DataFrame(M23)
    df = pd.DataFrame(P1)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\P1.txt", index=0)
    df = pd.DataFrame(P2)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\P2.txt", index=0)
    df = pd.DataFrame(P3)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\P3.txt", index=0)
    df = pd.DataFrame(P4)
    df.to_csv("D:\matlab eg\GF\优化差分\艾小猛Y网计算结果\P4.txt", index=0)
if uu == 2:
    df = pd.DataFrame(M1)
    df.to_csv("H:\艾小梦Y5\M1.txt", index=0)
    df = pd.DataFrame(M3)
    df.to_csv("H:\艾小梦Y5\M3.txt", index=0)
    df = pd.DataFrame(M4)
    df.to_csv("H:\艾小梦Y5\M4.txt", index=0)
    df = pd.DataFrame(M21)
    df.to_csv("H:\艾小梦Y5\M21.txt", index=0)
    df = pd.DataFrame(M22)
    df.to_csv("H:\艾小梦Y5\M22.txt", index=0)
    df = pd.DataFrame(M23)
    df.to_csv("H:\艾小梦Y5\M23.txt", index=0)
    df = pd.DataFrame(P1)
    df.to_csv("H:\艾小梦Y5\P1.txt", index=0)
    df = pd.DataFrame(P2)
    df.to_csv("H:\艾小梦Y5\P2.txt", index=0)
    df = pd.DataFrame(P3)
    df.to_csv("H:\艾小梦Y5\P3.txt", index=0)
    df = pd.DataFrame(P4)
    df.to_csv("H:\艾小梦Y5\P4.txt", index=0)

# 1117测试双管道时候用的
# c= []
# for p in range(Pipe_num_net):
#     for t in range(Node):
#        c.append(node_pressure[p, t,0].getAttr('X')) # 看各节点气压 初始时刻
# plt.plot(c)
# plt.show()
# plt.title('Pre(x),t=0')
#
# c= []
# for p in range(Pipe_num_net):
#     for node in range(Node):
#         c.append(Pressure_init / c2 -Pre_down * p - K * node * Lij)# 算初始时刻气压
# plt.plot(c)
# plt.show()
#
# c=[]
# a=[]
# for t in range(T):
#     c.append(c2*node_pressure[0,Node-1,t].getAttr('X'))
#     a.append(c2*node_pressure[1,0,t].getAttr('X'))
# plt.plot(c,label='c')
# plt.plot(a,label='a')
# plt.legend()
# plt.show()
# # 气压 管道0的末端=管道1的首端
# p=0
# a=Pressure_init / c2 -Pre_down * p - K * (Node-1) * Lij #  最后一个节点
# b=Pressure_init / c2 -Pre_down * p - K * Node * Lij
# p=1
# c=Pressure_init / c2 -Pre_down * p - K * 0 * Lij # 第一个节点
# d=Pressure_init / c2 -Pre_down * p - K * 1 * Lij
# #初始时刻 各节点流量分布
# c= []
# for p in range(Pipe_num_net):
#     for t in range(Node):
#        c.append(flow[p, t,0].getAttr('X'))
# plt.plot(c)
# plt.show()
# plt.title('f(x),t=0')
# #初始时刻 各节点气压分布
# c= []
# for p in range(Pipe_num_net):
#     for t in range(Node):
#        c.append(c2*node_pressure[p, t,0].getAttr('X')) # 发现c26 和c27不相等 ，理论上c26是p=0的end。c27是p=1的start，应该相等
# plt.plot(c)
# plt.show()
# plt.title('f(x),t=0')
