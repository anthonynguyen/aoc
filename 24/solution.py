#!/usr/bin/env python3

import collections
import itertools

f = open("input.txt")
lines = [l.strip() for l in f.readlines()]

coords = {}

for y, l in enumerate(lines):
	for x, c in enumerate(l):
		if c.isdigit():
			coords[int(c)] = (x, y)

def wall(x, y):
	if lines[y][x] == "#":
		return True
	return False

numD = 8
dist = [[0 for i in range(numD)] for i in range(numD)]

def pathfrom(a, b):
	q = collections.deque()

	ax, ay = coords[a]
	q.append((ax, ay, 0))

	target = coords[b]
	visited = []

	while len(q):
		x, y, d = q.popleft()
		if wall(x, y):
			continue

		if (x, y) in visited:
			continue

		visited.append((x, y))

		if (x, y) == target:
			return d

		q.append((x, y + 1, d + 1))
		q.append((x, y - 1, d + 1))
		q.append((x + 1, y, d + 1))
		q.append((x - 1, y, d + 1))

for i in range(numD):
	for j in range(i + 1, numD):
		d = pathfrom(i, j)
		dist[i][j] = d
		dist[j][i] = d

def solve(part2):
	mind = 1000000
	for p in itertools.permutations(range(1, numD)):
		pp = [0] + list(p)
		if part2:
			pp += [0]
		d = sum([dist[n][pp[i+1]] for i, n in enumerate(pp[:-1])])
		mind = min(d, mind)

	return mind

print(solve(False))
print(solve(True))
