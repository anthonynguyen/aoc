#!/usr/bin/env python3

f = open("input.txt")
lines = [l.strip() for l in f.readlines()]

discs = []

def pos(n, t):
	return (discs[n][1] + t) % discs[n][0]

for l in lines:
	p = l.split()
	discs.append((int(p[3]), int(p[11][:-1])))

def solve():
	global discs
	i = 0
	while True:
		valid = True
		for j in range(len(discs)):
			if pos(j, i + j + 1):
				valid = False
				break

		if not valid:
			i += 1
			continue

		print(i)
		break

solve()
discs.append((11, 0))
solve()
