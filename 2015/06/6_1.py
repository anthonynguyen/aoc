#!/usr/bin/env python3

import re

lights = []
for i in range(1000):
	lights.append([False] * 1000)

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
					lights[i][j] = True
		elif m.group(1) == "turn off":
			for i in range(s[0], e[0] + 1):
				for j in range(s[1], e[1] + 1):
					lights[i][j] = False
		else:
			for i in range(s[0], e[0] + 1):
				for j in range(s[1], e[1] + 1):
					lights[i][j] = not lights[i][j]


on = 0
for i in lights:
	on += i.count(True)

print(on)