#!/usr/bin/env python3

import collections
import hashlib
import re

f = open("input.txt")
lines = [l.strip().split() for l in f.readlines()]

def get(arg):
	if arg in "abcd":
		return registers[arg]
	return int(arg)

def solve(registers):
	i = 0

	a = registers["a"]

	outt = []
	# let's hope this is long enough
	target = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

	while i < len(lines) and len(outt) < len(target):
		line = lines[i]

		if line[0] == "cpy":
			if line[2] in "abcd":
				registers[line[2]] = get(line[1])
		elif line[0] == "inc":
			registers[line[1]] += 1
		elif line[0] == "dec":
			registers[line[1]] -= 1
		elif line[0] == "jnz":
			if get(line[1]) != 0:
				i += get(line[2])
				continue
		elif line[0] == "tgl":
			x = get(line[1])
			t = i + x
			if t < len(lines):
				if lines[t][0] == "inc":
					lines[t][0] = "dec"
				elif lines[t][0] == "dec":
					lines[t][0] = "inc"
				elif lines[t][0] == "tgl":
					lines[t][0] = "inc"
				elif lines[t][0] == "cpy":
					lines[t][0] = "jnz"
				elif lines[t][0] == "jnz":
					lines[t][0] = "cpy"
		elif line[0] == "out":
			outt.append(get(line[1]))

		i += 1

	if outt == target:
		print("yay", a)
		return True
	return False

nn = 0
while True:
	registers = {
		"a": nn,
		"b": 0,
		"c": 0,
		"d": 0
	}
	r = solve(registers)
	if r:
		break
	nn += 1
