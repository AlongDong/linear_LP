import numpy as np
import random

# random.seed(1)
def down_gdp(base_energy, energy_down_goal: dict, down_type, base_year):
    """
    :param base_energy: 2020年基准值
    :param energy_down_goal: 下降百分比
    :param down_type: 分散到每年的数值的分散形式线性/非线性
    :param base_year: 基准年
    :return: 返回给定年份每一年的下降值
    """

    def down_linear(base_energy, energy_down_goal, base_energy_temp, base_year, energy_):
        """
        :param base_energy: 2020年基准值
        :param energy_down_goal: 下降百分比
        :param base_energy_temp: 中间变量
        :param base_year: 中间变量基准年
        :param energy_: 存储每一年下降的值
        :return:
        """
        end_energy = base_energy * (1 - energy_down_goal[year])
        down_rate = (base_energy_temp - end_energy) / (year - base_year)
        energy_ = energy_ + [round(x, 3) for x in
                             np.arange(base_energy_temp - down_rate, end_energy - down_rate, -down_rate)]
        base_energy_temp = end_energy
        base_year = year
        return energy_, base_energy_temp, base_year

    def down_nonlinear(base_energy, energy_down_goal, base_energy_temp, base_year, energy_):
        end_energy = round(base_energy * (1 - energy_down_goal[year]), 3)
        down_rate = (base_energy_temp - end_energy) / (year - base_year)
        energy_ = energy_ + [round(random.uniform(x + down_rate, x), 3) for x in
                             np.arange(base_energy_temp - down_rate, end_energy, -down_rate)]
        energy_.append(end_energy)
        base_energy_temp = end_energy
        base_year = year
        return energy_, base_energy_temp, base_year

    base_energy_temp = base_energy
    base_year = base_year
    energy_ = list()

    if down_type == "线性":
        for year in energy_down_goal.keys():
            if year == 2025:
                energy_, base_energy_temp, base_year = down_linear(base_energy, energy_down_goal, base_energy_temp,
                                                                   base_year, energy_)
            elif year == 2030:
                energy_, base_energy_temp, base_year = down_linear(base_energy, energy_down_goal, base_energy_temp,
                                                                   base_year, energy_)
            else:
                energy_, base_energy_temp, base_year = down_linear(base_energy, energy_down_goal, base_energy_temp,
                                                                   base_year, energy_)
        return energy_

    elif down_type == "非线性":
        for year in energy_down_goal.keys():
            if year == 2025:
                energy_, base_energy_temp, base_year = down_nonlinear(base_energy, energy_down_goal, base_energy_temp,
                                                                      base_year, energy_)
            elif year == 2030:
                energy_, base_energy_temp, base_year = down_nonlinear(base_energy, energy_down_goal, base_energy_temp,
                                                                      base_year, energy_)
            else:
                energy_, base_energy_temp, base_year = down_nonlinear(base_energy, energy_down_goal, base_energy_temp,
                                                                      base_year, energy_)
        return energy_
if __name__ == "__main__":
    energy_down_goal = {2025: 0.15, 2030: 0.25, 2050: 0.35}
    print(energy_down_goal.values())
    a = down_gdp(0.4, energy_down_goal, "线性", 2020)
    b = down_gdp(0.4, energy_down_goal, "非线性", 2020)
    print(a)
    print(b)
