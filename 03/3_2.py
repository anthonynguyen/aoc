#!/usr/bin/env python3

h = 1
t = True
n = 8192
with open("input3.txt") as f:
	grid = []
	for i in range(n):
		grid.append([False] * n)
	row = [n/2, n/2]
	col = [n/2, n/2]

	grid[row[0]][col[0]] = True
	for c in f.read():
		ind = 1
		if t:
			ind = 0

		if c == "^":
			row[ind] -= 1
		elif c == "v":
			row[ind] += 1
		elif c == "<":
			col[ind] -= 1
		else:
			col[ind] += 1

		if not grid[row[ind]][col[ind]]:
			h += 1
			grid[row[ind]][col[ind]] = True

		t = not t

print(h)