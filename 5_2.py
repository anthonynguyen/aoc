#!/usr/bin/env python3

nice = 0
with open("input5.txt") as f:
	for l in f.readlines():
		line = l.strip()
		pair = False
		for i, c in enumerate(line):
			if i == len(line) - 1:
				break
			search = c + line[i + 1]
			if search in line[i+2:]:
				pair = True
				break

		mid = False
		for i, c in enumerate(line):
			if i == len(line) - 2:
				break

			if c == line[i+2]:
				mid = True
				break

		if pair and mid:
			print(line.strip())
			nice += 1

print(nice)