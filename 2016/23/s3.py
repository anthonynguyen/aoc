#!/usr/bin/env python3

import collections
import hashlib
import re

f = open("input2.txt")
lines = [l.strip().split() for l in f.readlines()]

def get(arg):
	if arg in "abcd":
		return registers[arg]
	return int(arg)

def solve(registers):
	i = 0
	n = 0

	while i < len(lines):
		line = lines[i]
		n += 1

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
			print(x)
			break
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
		elif line[0] == "spec":
			print(registers)
			registers["a"] += registers["b"] * registers["d"]
			registers["c"] = 0
			registers["d"] = 0
			print(registers)

		i += 1
		if n % 100000 == 0:
			n = 0
			print(registers["a"])

registers = {
	"a": 12,
	"b": 0,
	"c": 0,
	"d": 0
}
solve(registers)
print(registers["a"])

