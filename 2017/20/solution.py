#!/usr/bin/env python3

import re

particles = []
pre = re.compile(r"p=\<(-?\d+),(-?\d+),(-?\d+)\>, v=\<(-?\d+),(-?\d+),(-?\d+)\>, a=\<(-?\d+),(-?\d+),(-?\d+)\>")

for line in open("input.txt"):
	m = pre.match(line)

	pos = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
	vel = (int(m.group(4)), int(m.group(5)), int(m.group(6)))
	acc = (int(m.group(7)), int(m.group(8)), int(m.group(9)))

	particles.append([pos, vel, acc, True])

def add3t(a, b):
	return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def run(particles, part2):
	for _ in range(500):
		seen = {}
		for i, p in enumerate(particles):
			if part2 and not p[3]:
				continue

			newacc = p[2]
			newvel = add3t(p[1], newacc)
			newpos = add3t(p[0], newvel)

			valid = True
			if newpos in seen:
				particles[seen[newpos]][3] = False
				valid = False
			else:
				seen[newpos] = i

			particles[i] = [newpos, newvel, newacc, valid]

	if part2:
		particles = [p for p in particles if p[3]]

	closest = 0
	cdist = 10000000

	for i, p in enumerate(particles):
		dist = sum(abs(x) for x in p[0])

		if dist < cdist:
			cdist = dist
			closest = i

	return (particles, closest)

print(run(particles[:], False)[1])
print(len(run(particles[:], True)[0]))
