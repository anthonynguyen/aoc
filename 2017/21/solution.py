#!/usr/bin/env python3

lines = [x.strip().split() for x in open("input.txt")]

rules = {}
for line in lines:
	rules[line[0]] = line[2]

def flipH(pattern):
	return "/".join(x[::-1] for x in pattern.split("/"))

def flipV(pattern):
	return "/".join(pattern.split("/")[::-1])

def rotateCW(pattern):
	grid = pattern.split("/")
	return "/".join(["".join(x)[::-1] for x in zip(*grid)])

def findMatch(pattern):
	# try v. flip, h.flip
	# also try 3 rotations
	t = pattern
	for i in range(4):
		if t in rules:
			return rules[t]
		elif flipH(t) in rules:
			return rules[flipH(t)]
		elif flipV(t) in rules:
			return rules[flipV(t)]

		t = rotateCW(t)

	return None

def splitt(large, n, size):
	subg = []

	for row in range(n):
		rr = []

		for col in range(n):
			cursq = []
			for j in range(size):
				cursq.append(large[row*size+j][col*size:(col+1)*size])
			rr.append("/".join(cursq))

		subg.append(rr)

	return subg

def run(iters):
	grid = ".#./..#/###"

	for _ in range(iters):
		ss = grid.split("/")
		subg = []

		if len(ss) % 2 == 0:
			size = 2
			target = len(ss) // 2
		elif len(ss) % 3 == 0:
			size = 3
			target = len(ss) // 3

		subg = splitt(ss, target, size)

		for i in range(len(subg)):
			for j in range(len(subg[i])):
				subg[j][i] = findMatch(subg[j][i]).split("/")

		grid = ""
		for row in subg:
			for i in range(size + 1):
				for j in range(len(row)):
					grid += row[j][i]
				grid += "/"

		grid = grid.strip("/")

	return grid.count("#")

print(run(5))
print(run(18))
