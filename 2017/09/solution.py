#!/usr/bin/env python3

content = open("input.txt").read().strip()

score = 0
level = 0
garbage = 0

inGarbage = False
ignore = False

for char in content:
	if inGarbage:
		if ignore:
			ignore = False
		elif char == '!':
			ignore = True
		elif char == '>':
			inGarbage = False
		else:
			garbage += 1

		continue

	if char == '{':
		level += 1
	elif char == '}':
		score += level
		level = max(level - 1, 0)
	elif char == '<':
		inGarbage = True

print(score)
print(garbage)
