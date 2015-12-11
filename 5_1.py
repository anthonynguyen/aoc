#!/usr/bin/env python3

nice = 0
with open("input5.txt") as f:
	for line in f.readlines():
		v = 0
		for c in line:
			if c in "aeiou":
				v += 1

		d = False
		for l in "abcdefghijklmnopqrstuvwxyz":
			if (l + l) in line:
				d = True
				break

		good = True
		for p in ["ab", "cd", "pq", "xy"]:
			if p in line:
				good = False
				break

		if v >= 3 and d and good:
			nice += 1
print(nice)