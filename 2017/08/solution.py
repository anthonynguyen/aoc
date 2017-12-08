#!/usr/bin/env python3

from collections import defaultdict

lines = [x.strip().split() for x in open("input.txt").readlines()]
registers = defaultdict(lambda: 0)
lifetimeLargest = -999999

# a dec -511 if x >= -4
# 0 1   2    3  4 5  6
for l in lines:
	if eval("{} {} {}".format(registers[l[4]], l[5], l[6])):
		amount = int(l[2])
		if l[1] == "dec":
			amount = -amount

		registers[l[0]] += int(amount)
		lifetimeLargest = max(lifetimeLargest, registers[l[0]])

print(max(registers.values()))
print(lifetimeLargest)
