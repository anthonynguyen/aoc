#!/usr/bin/env python3

def do(instructions):
	here = (0, 0)
	visited = set([here])
	go = lambda (x, y), direction: {
		"^": (x, y - 1),
		"v": (x, y + 1),
		"<": (x - 1, y),
		">": (x + 1, y)
	}[direction]

	for inst in instructions:
		here = go(here, inst)
		visited.add(here)

	return visited

m = open("input3.txt").read()

print(len(do(m)))
print(len(do(m[::2]) | do(m[1::2])))