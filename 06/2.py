#!/usr/bin/env python3

f = open("1.in")
raw = f.readlines()

answer = [[],[],[],[],[],[],[],[]]

for l in raw:
	line = l.strip()
	for i, c in enumerate(line):
		answer[i].append(c)

for pos in answer:
	freq = []
	for c in set(pos):
		freq.append((pos.count(c), c))
	print(sorted(freq)[0][1], end = "")

print("")

