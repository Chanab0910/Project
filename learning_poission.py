from numpy import random

base = 0.0128125
Germany_attack = 72
Germany_defense = 46
Sweden_attack = 64
Sweden_defense = 40

def Calculate_Goals(attack, defense):
    changed_minute_base = base * attack / defense

    num_goals = random.poisson(changed_minute_base)
    return num_goals

for x in range(10):
    Gr_goals = 0
    Sw_goals = 0
    for i in range(90):
        Gr_goals += Calculate_Goals(Germany_attack, Sweden_defense)
        Sw_goals += Calculate_Goals(Sweden_attack, Germany_defense)

    print(Gr_goals, '-', Sw_goals)

import matplotlib

changed_minute_base = (base * Germany_attack / Sweden_defense) * 90
print(changed_minute_base)