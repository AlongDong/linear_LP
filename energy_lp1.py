import numpy as np
from scipy.optimize import linprog


class Lp(object):
    def __init__(self, x_low: list, x_up: list, F_low: list, F_up: list, P: float, T: float, fun_var_num: int):
        # def __init__(self,T):
        self.x_low = x_low
        self.x_up = x_up
        self.F_low = F_low
        self.F_up = F_up
        self.P = P
        self.T = T
        self.fun_var_num = fun_var_num

    def lp_solve(self):
        # 目标函数系数
        c_x = [-1 for _ in range(self.fun_var_num)]
        c_F = [0 for _ in range(self.fun_var_num)]
        c = np.r_[c_x, c_F]

        # 不等式1的各变量的系数
        A_x_neq1 = [-self.P for __ in range(self.fun_var_num)]
        A_F_neq1 = [1 for _ in range(self.fun_var_num)]
        A_neq1 = np.r_[A_x_neq1, A_F_neq1]
        # 不等式2的各变量的系数
        A_x_neq2 = [0 for x in range(self.fun_var_num)]
        A_F_neq2 = [1 for x_ in range(self.fun_var_num)]
        A_neq2 = np.r_[A_x_neq2, A_F_neq2]
        # 合并不等式系数至一个数组中
        A = np.vstack((A_neq1, A_neq2))
        b = [0, self.T]

        # 单个变量的上下限
        lows = np.r_[self.x_low, self.F_low]
        ups = np.r_[self.x_up, self.F_up]
        bound = list(zip(lows, ups))

        ans = linprog(c, A_ub=A, b_ub=b, A_eq=None, b_eq=None, bounds=bound, method="interior-point")
        return -ans.fun,ans.x

if __name__=='__main__':
    x_low = [198.87, 1825.60, 193.34, 68.28, 311.36, 1275.80]
    x_up = [239.31, 2037.50, 215.78, 85.54, 390.02, 1598.12]
    F_low = [16.53297238, 1162.444763, 10.58932028, 27.03170025, 37.94237952, 292.446495]
    F_up = [19.89556186, 1297.36551, 11.81838427, 33.86115066, 47.5283692, 366.3319265]
    P = 0.402055231
    T = 2157.779084
    fun_var_num = len(x_low)
    a = Lp(x_low, x_up, F_low, F_up, P, T, fun_var_num)
    GDP,x= a.lp_solve()
    print(GDP)
