#!/usr/bin/env python3

from collections import defaultdict

lines = [x.strip().split() for x in open("input.txt")]
registers = defaultdict(int)
lfreq = 0

def reg(r):
	try:
		return(int(r))
	except:
		return registers[r]

i = 0
while True:
	l = lines[i]

	if l[0] == "snd":
		lfreq = reg(l[1])
	elif l[0] == "set":
		registers[l[1]] = reg(l[2])
	elif l[0] == "add":
		registers[l[1]] += reg(l[2])
	elif l[0] == "mul":
		registers[l[1]] *= reg(l[2])
	elif l[0] == "mod":
		registers[l[1]] %= reg(l[2])
	elif l[0] == "jgz":
		if reg(l[1]) > 0:
			i += reg(l[2])
			continue
	elif l[0] == "rcv" and lfreq:
		break

	i += 1

print(lfreq)
