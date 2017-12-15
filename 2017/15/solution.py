#!/usr/bin/env pypy3

def next(ca, cb, part2):
	a = 16807
	b = 48271
	div = 2147483647

	nextA = (ca * a) % div
	while part2 and nextA % 4:
		nextA = (nextA * a) % div

	nextB = (cb * b) % div
	while part2 and nextB % 8:
		nextB = (nextB * b) % div

	return (nextA, nextB)

def run(iters, part2):
	curA = 873
	curB = 583

	matches = 0

	for i in range(iters):
		if (curA & 0xFFFF) == (curB & 0xFFFF):
			matches += 1

		curA, curB = next(curA, curB, part2)

	return matches

print(run(40000000, False))
print(run(5000000, True))
