#!/usr/bin/env python3

h = 1
n = 8192
with open("input3.txt") as f:
	grid = []
	for i in range(n):
		grid.append([False] * n)
	row = n/2
	col = n/2
	grid[row][col] = True
	for c in f.read():
		if c == "^":
			row -= 1
		elif c == "v":
			row += 1
		elif c == "<":
			col -= 1
		else:
			col += 1

		if not grid[row][col]:
			h += 1
			grid[row][col] = True

print(h)