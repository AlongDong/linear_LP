import numpy as np
import random

# random.seed(1)
def down_GDP(base_energy, energy_down_goal: dict, down_type, base_year):
    """
    :param base_energy: 2020年基准值
    :param energy_down_goal: 下降到的值
    :param down_type: 分散到每年的数值的分散形式线性/非线性
    :param base_year: 基准年
    :return: 返回给定年份每一年的下降值
    """
    def down_linear(energy_down_goal, base_energy_temp, base_year, energy_):
        """
        :param base_energy: 2020年基准值
        :param energy_down_goal: 下降到的值
        :param base_energy_temp: 中间变量
        :param base_year: 中间变量基准年
        :param energy_: 存储每一年下降的值
        :return:
        """
        end_energy = energy_down_goal[year]
        down_rate = (base_energy_temp - end_energy) / (year - base_year)
        energy_ = energy_ + [round(x, 3) for x in
                             np.arange(base_energy_temp - down_rate, end_energy - down_rate, -down_rate)]
        base_energy_temp = end_energy
        base_year = year
        return energy_, base_energy_temp, base_year

    base_energy_temp = base_energy
    base_year = base_year
    energy_ = list()

    if down_type == "线性":
        for year in energy_down_goal.keys():
            while base_year<year:
                energy_, base_energy_temp, base_year = down_linear(energy_down_goal, base_energy_temp,
                                                                   base_year, energy_)
        return energy_

    elif down_type == "非线性":
        pass

        return energy_

if __name__ == "__main__":
    energy_down_goal = {2025: 800, 2030: 750, 2050: 600}
    print(energy_down_goal.values())
    a = down_GDP(900, energy_down_goal, "线性", 2020)
    b = down_GDP(900, energy_down_goal, "非线性", 2020)
    print(a)
    print(b)
