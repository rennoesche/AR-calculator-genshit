#!/usr/bin/env python3
import json

# Player info
LEVEL = input("My Adventure Rank is:\n")
LEVEL = int(LEVEL)

CUR_EXP = input("Input your current EXP:\n")
CUR_EXP = int(CUR_EXP)

DAILY = input("Do daily mission every day?:\n Y(yes)/N(no)")
DAILY_EXP = 0
if DAILY.upper() == "Y" or "YES":
    DAILY_EXP = 500 + (4 * 250)
    DO_DAILY = "doing daily"
else:
    DAILY_EXP = 0
    DO_DAILY = "not do daily"

REFILL_RESIN = input("How many times u refill resin? (0-6)times:\n")

EXPECT_LVL = input("AR that you wanna reach:\n")
EXPECT_LVL = int(EXPECT_LVL)

# Code
with open('artable.json', 'r', encoding='utf-8') as file:
    ARTABLE = json.load(file)

RESIN_PD = 180
EXP_RESIN = 100

RESIN_PD = RESIN_PD / 20 * EXP_RESIN
REFILL_EXP = max(min(REFILL_RESIN, 6), 0) * (3 * EXP_RESIN)

EGPD = DAILY_EXP + RESIN_PD + REFILL_EXP
TOTAL = ARTABLE[EXPECT_LVL] - ARTABLE[LEVEL] - CUR_EXP

print("Current AR:", LEVEL, "Exp:", CUR_EXP)
print("Total Exp required:", TOTAL)
print("if you", DO_DAILY, "and REFILL RESIN", REFILL_RESIN, "times, then")
print("Est. days until AR", str(EXPECT_LVL) + ",", TOTAL / EGPD)