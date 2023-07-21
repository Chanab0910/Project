from numpy import random

base = 0.0128125
Germany_attack = 92
Germany_defense = 86
Sweden_attack = 80
Sweden_defense = 78
Gr_wins_num = 0
Sw_wins_num= 0
draws = 0
def Calculate_Goals(attack, defense):
    changed_minute_base = base * attack / defense

    num_goals = random.poisson(changed_minute_base)
    return num_goals

for x in range(1000):
    Gr_goals = 0
    Sw_goals = 0
    for i in range(90):
        Gr_goals += Calculate_Goals(Germany_attack, Sweden_defense)
        Sw_goals += Calculate_Goals(Sweden_attack, Germany_defense)

    print(Gr_goals, '-', Sw_goals)

    if Gr_goals > Sw_goals:
        Gr_wins_num += 1
    elif Gr_goals < Sw_goals:
        Sw_wins_num +=1
    else:
        draws += 1
print(f'Gr won: {Gr_wins_num} | Sw won: {Sw_wins_num}, | Draws: {draws}')