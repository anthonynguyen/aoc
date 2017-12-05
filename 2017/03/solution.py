#!/usr/bin/env python3

import math

inp = 312051

def part1():
	i = 1
	while i * i < inp:
		i += 2

	corners = [i * i - n * (i - 1) for n in range(4)]
	smallest_diff = min([abs(inp - corner) for corner in corners])

	return i - 1 - smallest_diff

def sumAdjacent(grid, coords):
	return \
		grid[coords[0] - 1][coords[1] - 1] + \
		grid[coords[0] - 1][coords[1]] + \
		grid[coords[0] - 1][coords[1] + 1] + \
		grid[coords[0]][coords[1] - 1] + \
		grid[coords[0]][coords[1] + 1] + \
		grid[coords[0] + 1][coords[1] - 1] + \
		grid[coords[0] + 1][coords[1]] + \
		grid[coords[0] + 1][coords[1] + 1]

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
def part2():
	n = 11
	grid = [[0 for _ in range(n)] for _ in range(n)]

	# y, x
	cur = [n // 2, n // 2]

	grid[cur[0]][cur[1]] = 1
	gr = 1

	cur[1] += 1

	direction = 0
	while gr < inp:
		grid[cur[0]][cur[1]] = gr

		if direction == 0: # up
			# something on left -> write number then go up
			# nothing on left -> write number then go left
			if grid[cur[0]][cur[1] - 1]:
				cur[0] -= 1
			else:
				direction = 1
		elif direction == 1: # left
			# something underneath -> write number then go left
			# nothing underneath -> write number then go down
			if grid[cur[0] + 1][cur[1]]:
				cur[1] -= 1
			else:
				direction = 2
		elif direction == 2: # down
			# something on right -> write number then go down
			# nothing on right -> write number then go right
			if grid[cur[0]][cur[1] + 1]:
				cur[0] += 1
			else:
				direction = 3
		elif direction == 3: # right
			# something on top -> write number then go right
			# nothing on top -> write number then go up
			if grid[cur[0] - 1][cur[1]]:
				cur[1] += 1
			else:
				direction = 0

		gr = sumAdjacent(grid, cur)

	return gr

print(part1())
print(part2())
