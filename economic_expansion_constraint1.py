import numpy as np


class EconomicExpansionConstraints():
    def __init__(self, gdp_up_goals):
        self.gdp_up_goals = gdp_up_goals

    @staticmethod
    def economic_expansion_constraints(base_year, gdp_up_goal, limit):
        a_b = []
        for year in gdp_up_goal.keys():
            temp=0
            while base_year < year:
                a = (gdp_up_goal[year]-temp) * (1 - limit)
                b = (gdp_up_goal[year]-temp) * (1 + limit)
                temp+=0.01/5
                a_b.append({"a": round(a, 8), "b": round(b, 8)})
                base_year += 1
        return a_b

    def constraints(self):
        ret = []
        for goal in self.gdp_up_goals:
            ret.append(self.economic_expansion_constraints(goal['base_year'], goal['gdp_up_goal'], goal['limit']))
        return ret


if __name__ == "__main__":
    # gdp_up_goal = {2025: 0.06, 2030: 0.05, 2035: 0.04}
    # a_b = economic_expansion_constraints(2020, gdp_up_goal, 0.5)
    # print(a_b)
    gdp_up_goals = [
        {
            "base_year": 2020,
            "limit": 0.5,
            "gdp_up_goal": {2025: 0.06, 2030: 0.05, 2035: 0.04}
        },        {
            "base_year": 2020,
            "limit": 0.2,
            "gdp_up_goal": {2025: 0.05, 2030: 0.04, 2035: 0.03}
        },        {
            "base_year": 2020,
            "limit": 0.3,
            "gdp_up_goal": {2025: 0.07, 2030: 0.06, 2035: 0.05}
        },        {
            "base_year": 2020,
            "limit": 0.1,
            "gdp_up_goal": {2025: 0.0612, 2030: 0.0533, 2035: 0.0444}
        },        {
            "base_year": 2020,
            "limit": 0.6,
            "gdp_up_goal": {2025: 0.10, 2030: 0.07, 2035: 0.04}
        },        {
            "base_year": 2020,
            "limit": 0.4,
            "gdp_up_goal": {2025: 0.0345, 2030: 0.0234, 2035: 0.0123}
        }
    ]
    x = EconomicExpansionConstraints(gdp_up_goals=gdp_up_goals).constraints()
    # print(x)
    for i in np.array(x).T:
        print(i.tolist())