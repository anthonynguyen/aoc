#!/usr/bin/env python3

f = open("1.in")
raw = f.readlines()

valid = 0

for l in raw:
	sides = sorted(list(map(int, l.split())))
	if sides[0] + sides[1] > sides[2]:
		valid += 1

print(valid)
