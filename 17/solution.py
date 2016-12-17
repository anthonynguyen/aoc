#!/usr/bin/env python3

import collections
import hashlib

# up down left right
def walls(path):
	inp = "udskfozm"
	d = hashlib.md5((inp + path).encode("utf-8")).hexdigest()
	return (d[0] in "bcdef", d[1] in "bcdef", d[2] in "bcdef", d[3] in "bcdef")

# bfs without remembering visited nodes
q = collections.deque([(0, 0, "")])
found = []

while len(q):
	x, y, p = q.popleft()
	w = walls(p)

	if (x, y) == (3, 3):
		if not len(found):
			# this is the first one we find
			# since this is a bfs, it should be the shortest path
			print(p)
		found.append(len(p))
		continue

	if y > 0 and w[0]:
		q.append((x, y - 1, p + "U"))
	if y < 3 and w[1]:
		q.append((x, y + 1, p + "D"))
	if x > 0 and w[2]:
		q.append((x - 1, y, p + "L"))
	if x < 3 and w[3]:
		q.append((x + 1, y, p + "R"))

# the last one should be the longest path cause bfs
print(found[-1])
