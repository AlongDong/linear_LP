import numpy as np
def economic_expansion_constraints(base_year,gdp_up_goal,limit):
    a_b=[]
    for year in gdp_up_goal.keys():
        while base_year<=year:
            a=gdp_up_goal[year]*(1-limit)
            b=gdp_up_goal[year]*(1+limit)
            a_b.append({"a":a,"b":b})
            base_year+=1
    return a_b

gdp_up_goal={2025:0.06,2030:0.05,2035:0.04}
a_b=economic_expansion_constraints(2021,gdp_up_goal,0.5)
print(a_b)
