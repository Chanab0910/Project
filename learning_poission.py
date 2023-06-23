from numpy import random

base = 0.0128125
Germany_attack = 72
Germany_defense = 46
Sweden_attack = 64
Sweden_defense = 40


def Calculate_Goals(attack, defense):
    changed_minute_base = base * attack / defense
    ninety_min = changed_minute_base * 90
    num_goals = random.poisson(ninety_min)
    return num_goals


Gr_goals = Calculate_Goals(Germany_attack, Sweden_defense)
Sw_goals = Calculate_Goals(Sweden_attack, Germany_defense)

print(Gr_goals, '-', Sw_goals)
