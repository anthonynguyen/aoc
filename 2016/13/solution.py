#!/usr/bin/env python3

import collections

def wall(x, y):
	if x < 0 or y < 0:
		return True
	b = bin((x * x) + (3 * x) + (2 * x * y) + y + (y * y) + 1350)
	return b.count("1") % 2 != 0

target = (31, 39)
queue = collections.deque([(1, 1, 0)])
visited = []

while len(queue):
	x, y, dist = queue.popleft()

	if wall(x, y) or (x, y) in visited:
		continue

	if (x, y) == target:
		print(dist)
		break

	visited.append((x, y))

	queue.append((x - 1, y, dist + 1))
	queue.append((x + 1, y, dist + 1))
	queue.append((x, y - 1, dist + 1))
	queue.append((x, y + 1, dist + 1))

# ---------------------------------

queue = collections.deque([(1, 1, 0)])
visited = []

while len(queue):
	x, y, dist = queue.popleft()

	if wall(x, y) or (x, y) in visited or dist > 50:
		continue

	visited.append((x, y))

	queue.append((x - 1, y, dist + 1))
	queue.append((x + 1, y, dist + 1))
	queue.append((x, y - 1, dist + 1))
	queue.append((x, y + 1, dist + 1))

print(len(visited))
