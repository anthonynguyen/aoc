#!/usr/bin/env python3

from collections import defaultdict

lines = [x.strip().split() for x in open("input.txt")]

indices = [0, 0]
lock = [0, 0]
sent = [0, 0]
queues = [[], []]

registers = [defaultdict(int), defaultdict(int)]
registers[0]['p'] = 0
registers[1]['p'] = 1

def reg(n, r):
	try:
		return(int(r))
	except:
		return registers[n][r]

def step(n):
	l = lines[indices[n]]
	if l[0] == "snd":
		queues[not n].append(reg(n, l[1]))
		sent[n] += 1
	elif l[0] == "set":
		registers[n][l[1]] = reg(n, l[2])
	elif l[0] == "add":
		registers[n][l[1]] += reg(n, l[2])
	elif l[0] == "mul":
		registers[n][l[1]] *= reg(n, l[2])
	elif l[0] == "mod":
		registers[n][l[1]] %= reg(n, l[2])
	elif l[0] == "jgz":
		if reg(n, l[1]) > 0:
			indices[n] += reg(n, l[2])
			return True
	elif l[0] == "rcv":
		if queues[n]:
			lock[n] = 0
			registers[n][l[1]] = queues[n].pop(0)
		else:
			if lock[not n]:
				return False
			else:
				lock[n] = 1
				return True

	indices[n] += 1
	return True

while step(0) and step(1):
	pass

print(sent[1])
