#!/usr/bin/env python3

f = open("input.txt")
lines = [l.strip().split() for l in f.readlines()]

def get(arg):
	if arg in "abcd":
		return registers[arg]
	return int(arg)

def solve(registers):
	i = 0

	while i < len(lines):
		line = lines[i]

		if line[0] == "cpy":
			registers[line[2]] = get(line[1])
		elif line[0] == "inc":
			registers[line[1]] += 1
		elif line[0] == "dec":
			registers[line[1]] -= 1
		elif line[0] == "jnz":
			if get(line[1]) != 0:
				i += int(line[2])
				continue

		i += 1

registers = {
	"a": 0,
	"b": 0,
	"c": 0,
	"d": 0
}
solve(registers)
print(registers["a"])

registers = {
	"a": 0,
	"b": 0,
	"c": 1,
	"d": 0
}
solve(registers)
print(registers["a"])
