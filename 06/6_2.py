#!/usr/bin/env python3

import re

lights = []
for i in range(1000):
	lights.append([0] * 1000)

inst = re.compile("(.+?) (\d+),(\d+) through (\d+),(\d+)")
with open("input6.txt") as f:
	for line in f.readlines():
		m = inst.match(line)
		if m is None:
			break

		s = (int(m.group(2)), int(m.group(3)))
		e = (int(m.group(4)), int(m.group(5)))

		if m.group(1) == "turn on":
			for i in range(s[0], e[0] + 1):
				for j in range(s[1], e[1] + 1):
					lights[i][j] += 1
		elif m.group(1) == "turn off":
			for i in range(s[0], e[0] + 1):
				for j in range(s[1], e[1] + 1):
					lights[i][j] -= 1
					if lights[i][j] < 0:
						lights[i][j] = 0
		else:
			for i in range(s[0], e[0] + 1):
				for j in range(s[1], e[1] + 1):
					lights[i][j] += 2


on = 0
for i in lights:
	on += sum(i)

print(on)