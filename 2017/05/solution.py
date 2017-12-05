#!/usr/bin/env python3

f = open("input.txt")
lines = [int(x.strip()) for x in f.readlines()]

def run(instructions, part2):
	steps = 0
	cur = 0

	while cur >= 0 and cur < len(instructions):
		inst = instructions[cur]

		if part2 and inst >= 3:
			instructions[cur] -= 1
		else:
			instructions[cur] += 1

		cur += inst
		steps += 1

	return steps

print(run(lines[:], False))
print(run(lines[:], True))
