#!/usr/bin/env python3

f = open("input.txt")

lines = [x.strip().split() for x in f]
pairs = [(int(l[0][:-1]), int(l[1])) for l in lines]

def calculate(delay):
	punished = False
	punishment = 0

	for layer, depth in pairs:
		if not (delay + layer) % (depth * 2 - 2):
			punished = True
			punishment += layer * depth

	return (punished, punishment)

print(calculate(0)[1])

delay = 0
while calculate(delay)[0]:
	delay += 1

print(delay)
