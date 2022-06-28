import numpy as np
from scipy.optimize import linprog
import warnings
warnings.filterwarnings("ignore")
class Lp(object):
    def __init__(self, x_low: list, x_up: list,P: float, T: float, fun_var_num: int, A, B, C):
        """
        :param x_low: gdp约束下限
        :param x_up: gdp约束下限
        :param P: 能耗强度控制约束
        :param T: 能耗总量控制约束
        :param fun_var_num: 部门数量
        :param A: 第一种能源矩阵
        :param B: 第二种能源矩阵
        :param C: 第三种能源矩阵
        """
        self.x_low = x_low
        self.x_up = x_up
        self.P = P
        self.T = T
        self.A = A
        self.B = B
        self.C = C
        self.fun_var_num = fun_var_num

    def lp_solve(self):
        # 目标函数系数
        c = [-1 for _ in range(self.fun_var_num)]

        energy_matrix = np.array([[0.08319041, 0. ,        0.   ,      0.     ,    0.    ,     0.        ],
         [0.  ,       0.63955646 ,0.  ,       0.   ,      0.   ,      0. ,       ],
         [0. ,        0. ,        0.05482305, 0. ,        0. ,        0.        ],
         [0. ,        0.,         0. ,        0.39606769, 0.  ,       0.        ],
         [0. ,        0. ,        0. ,        0.,         0.12190175, 0.        ],
         [0.   ,      0.  ,       0.   ,      0.  ,       0. ,        0.22984435]])
        print(energy_matrix)
        cons_matrix=energy_matrix-np.eye((self.fun_var_num),dtype=object)*self.P
        # 不等式1的各变量的系数
        A_neq1 = [var[i] for i, var in enumerate(cons_matrix)]
        # 不等式2的各变量的系数
        A_neq2 = [var[i] for i, var in enumerate(energy_matrix)]

        A = np.vstack((A_neq1, A_neq2))
        b = [0, self.T]

        # 单个变量的上下限
        bound = list(zip(self.x_low, self.x_up))

        ans = linprog(c, A_ub=A, b_ub=b, A_eq=None, b_eq=None, bounds=bound, method="interior-point")
        return -ans.fun, ans.x


if __name__ == '__main__':
    x_low =[1805108.5137399998, 15278735.831199998 ,  1327793.731145,705201.540797276,   3396817.187208,    11927887.4553188]
    # x_low = [198.87, 1825.60, 193.34, 68.28, 311.36, 1275.80]
    x_up =[1952464.3107800002, 16218002.3782  ,      1465388.936445,770429.965469996 ,  3672981.1861680006, 12223495.070922801]
    # x_up = [239.31, 2037.50, 215.78, 85.54, 390.02, 1598.12]
    P=0.26
    # P = 0.3767
    # T = 2157.779084
    T=600
    fun_var_num = len(x_low)
    A = np.array([[0.023781067, 0, 0, 0, 0, 0],
                  [0, 0.182141056, 0, 0, 0, 0],
                  [0, 0, 0.015667108, 0, 0, 0],
                  [0, 0, 0, 0.113238913, 0, 0],
                  [0, 0, 0, 0, 0.034858309, 0],
                  [0, 0, 0, 0, 0, 0.065570256]],dtype=object)
    B = np.array([[0.045672679, 0, 0, 0, 0, 0],
                  [0, 0.349810631, 0, 0, 0, 0],
                  [0, 0, 0.030089433, 0, 0, 0],
                  [0, 0, 0, 0.217480761, 0, 0],
                  [0, 0, 0, 0, 0.066947055, 0],
                  [0, 0, 0, 0, 0, 0.125930821]],dtype=object)
    C = np.array([[0.013682258, 0, 0, 0, 0, 0],
                  [0, 0.104793484, 0, 0, 0, 0],
                  [0, 0, 0.009013953, 0, 0, 0],
                  [0, 0, 0, 0.065151155, 0, 0],
                  [0, 0, 0, 0, 0.020055466, 0],
                  [0, 0, 0, 0, 0, 0.037725353]],dtype=object)

    # alpha=[0.092306472,0.054850062,0.054850062,0.112155209,0.112155209,0.112155209,0.094064862]
    a = Lp(x_low, x_up,P, T, fun_var_num, A, B, C)
    GDP, x = a.lp_solve()
    print(GDP)
    print(x)
    # import matplotlib.pyplot as plt
    # plt.plot(x)
    # plt.show()

    # cons_Matrix = np.array([[-0.318919227, 0, 0, 0, 0, 0],
    #                         [0, 0.234689941, 0, 0, 0, 0],
    #                         [0, 0, -0.347284737, 0, 0, 0],
    #                         [0, 0, 0, -0.006184402, 0, 0],
    #                         [0, 0, 0, 0, -0.280194401, 0],
    #                         [0, 0, 0, 0, 0, -0.172828801]])
