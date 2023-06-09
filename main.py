"""import modules"""
import json

# Player info
LEVEL = int(input("My Adventure Rank is: "))
CUR_EXP = int(input("Input your current EXP: "))
DAILY = input("Do daily mission every day? (Y/N): ")
DAILY_EXP = 0
if DAILY.upper() == "Y" or DAILY.upper() == "YES":
    DAILY_EXP = 500 + (4 * 250)
    DO_DAILY = "doing daily"
else:
    DAILY_EXP = 0
    DO_DAILY = "not doing daily"

REFILL_RESIN = int(input("How many times you refill resin? (0-6) times: "))
EXPECT_LVL = int(input("AR that you want to reach: "))

# Code
with open('artable.json', 'r', encoding='utf-8') as file:
    ARTABLE = json.load(file)

RESIN_PD = 180
EXP_RESIN = 100

RESIN_PD = RESIN_PD / 20 * EXP_RESIN
REFILL_EXP = max(min(REFILL_RESIN, 6), 0) * (3 * EXP_RESIN)

EGPD = DAILY_EXP + RESIN_PD + REFILL_EXP
TOTAL = ARTABLE[str(EXPECT_LVL)] - ARTABLE[str(LEVEL)] - CUR_EXP
M = TOTAL//(EGPD*30)
D = TOTAL//EGPD
print("Current AR:", LEVEL, "\nExp:", CUR_EXP)
print("Total Exp required:", TOTAL)
print("If you are", DO_DAILY, "and refill resin", REFILL_RESIN, "times, then")
print("Est. time until AR", str(EXPECT_LVL), "is", "≈", M, "months or", "≈", D, "days")
