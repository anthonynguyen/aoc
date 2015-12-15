#!/usr/bin/env python3

import re

rr = re.compile("(.+) can fly (.+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

rein = {}

states = {}

with open("input14.txt") as f:
	for l in f.readlines():
		line = l.strip()
		m = rr.match(line)
		if m is None:
			break

		rein[m.group(1)] = (int(m.group(2)), int(m.group(3)), int(m.group(4)))

points = {}
for r in rein:
	points[r] = 0
for total in range(1, 2504):
	maxdist = ([], -1)
	for r in rein:
		ttime = rein[r][1] + rein[r][2]
		full = total / ttime
		bleed = total % ttime

		if bleed >= rein[r][1]:
			dist = (full + 1) * rein[r][0] * rein[r][1]
		else:
			dist = full * rein[r][0] * rein[r][1] + bleed * rein[r][0]

		if dist > maxdist[1]:
			maxdist = ([r], dist)
		elif dist == maxdist[1]:
			maxdist = (maxdist[0] + [r], dist)

	for r in maxdist[0]:
		points[r] += 1

print(points)
print(max(points.values()))
print(sum(points.values()))