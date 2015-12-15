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

maxdist = 0
total = 2503
for r in rein:
	ttime = rein[r][1] + rein[r][2]
	groups = total / ttime
	diff = total - (ttime * groups)
	if diff > rein[r][1]:
		groups += 1
	print("{}: {} groups, {} remainder ({} traveled)".format(r, groups, diff, groups * rein[r][0] * rein[r][1]))