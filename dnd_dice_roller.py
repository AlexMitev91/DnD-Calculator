import random

print("number of rolls")
rolls = int(input())

adv_score = 0
adv_crit = 0
adv_fail = 0

dis_score = 0
dis_crit = 0
dis_fail = 0

norm_score = 0
norm_crit = 0
norm_fail = 0

for i in range(rolls):
    adv_roll1 = random.randint(1, 20)
    adv_roll2 = random.randint(1, 20)
    if adv_roll1 > adv_roll2:
        adv_score += adv_roll1
    else:
        adv_score += adv_roll2
    if adv_roll1 == 20 or adv_roll2 == 20:
        adv_crit += 1
    if adv_roll1 == adv_roll2 and adv_roll2 == 1:
        adv_fail += 1

for i in range(rolls):
    diss_roll1 = random.randint(1, 20)
    diss_roll2 = random.randint(1, 20)
    if diss_roll1 < diss_roll2:
        dis_score += diss_roll1
    else:
        dis_score += diss_roll2
    if diss_roll1 == diss_roll2 and diss_roll1 == 20:
        dis_crit += 1
    if diss_roll1 == 1 or diss_roll2 == 1:
        dis_fail += 1

for i in range(rolls):
    norm_roll = random.randint(1, 20)
    norm_score += norm_roll
    if norm_roll == 20:
        norm_crit += 1
    if norm_roll == 1:
        norm_fail += 1

percentage_adv_crit = (adv_crit / rolls) * 100
percentage_adv_fail = (adv_fail / rolls) * 100

percentage_dis_crit = (dis_crit / rolls) * 100
percentage_dis_fail = (dis_fail / rolls) * 100

percentage_norm_crit = (norm_crit / rolls) * 100
percentage_norm_fail = (norm_fail / rolls) * 100

avg_adv = adv_score / rolls
avg_diss = dis_score / rolls
avg_norm = norm_score / rolls

print(f"Out of {rolls} rolls with advantage:\nNatural 20s = {adv_crit} ({percentage_adv_crit:.2f}%)\nNatural 1s = {adv_fail} ({percentage_adv_fail:.2f}%)\nAverage roll was {avg_adv:.2f}\n\n")
print(f"Out of {rolls} rolls with disadvantage:\nNatural 20s = {dis_crit} ({percentage_dis_crit:.2f}%)\nNatural 1s = {dis_fail} ({percentage_dis_fail:.2f}%)\nAverage roll was {avg_diss:.2f}\n\n")
print(f"Out of  {rolls} normal rolls:\nNatural 20s = {norm_crit} ({percentage_norm_crit:.2f}%)\nNatural 1s = {norm_fail} ({percentage_norm_fail:.2f}%)\nAverage roll was {avg_norm:.2f}\n\n")
