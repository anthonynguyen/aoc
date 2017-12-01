#!/usr/bin/env python3

inp = 3014387
# inp = 5

elves = [1 for i in range(inp)]

while elves.count(0) < inp - 1:
	for i, e in enumerate(elves):
		if not e:
			continue

		fi = (i + 1) % inp
		while not elves[fi]:
			fi = (fi + 1) % inp

		elves[fi] = 0

for i, e in enumerate(elves):
	if e:
		print(i + 1)
