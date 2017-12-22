#!/usr/bin/env python3

from collections import defaultdict

lines = [x.strip() for x in open("input.txt")]

def run(bursts, part2 = False):
	grid = defaultdict(lambda: ".")

	for i in range(len(lines)):
		for j in range(len(lines[i])):
			grid[j, i] = lines[i][j]

	pos = (len(lines) // 2, len(lines) // 2)

	direction = 0 # up right down left
	infections = 0

	for _ in range(bursts):
		if part2:
			if grid[pos] == ".":
				grid[pos] = "W"
				direction = (direction + 3) % 4
			elif grid[pos] == "W":
				grid[pos] = "#"
				infections += 1
			elif grid[pos] == "#":
				grid[pos] = "F"
				direction = (direction + 1) % 4
			elif grid[pos] == "F":
				grid[pos] = "."
				direction = (direction + 2) % 4
		else:
			if grid[pos] == ".":
				grid[pos] = "#"
				direction = (direction + 3) % 4
				infections += 1
			elif grid[pos] == "#":
				grid[pos] = "."
				direction = (direction + 1) % 4

		x, y = pos
		if direction == 0:
			y -= 1
		elif direction == 1:
			x += 1
		elif direction == 2:
			y += 1
		elif direction == 3:
			x -= 1
		pos = (x, y)

	return infections

print(run(10000))
print(run(10000000, True))
