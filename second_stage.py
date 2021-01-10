from config2 import K
from utility import *


class SecondLayer:
    def __init__(self, empirical_distribution, confidence_level):
        self.model = gurobi.Model()
        self.distribution = None
        self.distribution_tuple_list = None
        self.empirical_distribution = empirical_distribution
        self.confidence_level = confidence_level

    def bulid_base_model(self):
        self.distribution_tuple_list = self.model.addVars(K, lb=0, ub=1, name='distribution')
        self.distribution = tonp(self.distribution_tuple_list)
        for k in range(K):
            self.model.addConstr(self.distribution[k] - self.empirical_distribution[k] >= -1 * self.confidence_level)
            self.model.addConstr(self.distribution[k] - self.empirical_distribution[k] <= self.confidence_level)
        self.model.addConstr(gurobi.quicksum(self.distribution_tuple_list) == 1)

    def optimize(self, obj_k):
        self.model.update()
        self.model.setObjective((self.distribution.reshape((1, -1)).dot(np.array(obj_k).reshape((-1, 1))))[0][0])
        self.model.optimize()
        return to_value(self.distribution_tuple_list)
