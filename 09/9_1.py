#!/usr/bin/env python3

import re
import itertools

routes = []
locations = set()

r = re.compile(r"(.+)? to (.+) = (\d+)")

with open("input9.txt") as f:
	for l in f.readlines():
		m = r.match(l)
		if m is None:
			break

		routes.append((m.group(1), m.group(2), int(m.group(3))))
		locations.add(m.group(1))
		locations.add(m.group(2))

def getdist(loc1, loc2):
	for r in routes:
		if (r[0] == loc1 and r[1] == loc2) or (r[1] == loc1 and r[0] == loc2):
			return r[2]

	return None

mindist = 10000000000
minr = []

for perm in itertools.permutations(list(locations)):
	dist = 0
	for i, l in enumerate(perm[:-1]):
		if getdist(l, perm[i + 1]) is not None:
			dist += getdist(l, perm[i + 1])
		else:
			break
	if dist < mindist:
		mindist = dist
		minr = perm


print(mindist)