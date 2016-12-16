#!/usr/bin/env python3

def dragon(a):
	b = a[::-1]
	b = b.replace("0", "2").replace("1", "0").replace("2", "1")
	return a + "0" + b

def checksum(s):
	c = ""
	for i in range(0, len(s), 2):
		if s[i] == s[i+1]:
			c += "1"
		else:
			c += "0"
	return c

def solve(s, length):
	while len(s) < length:
		s = dragon(s)

	s = s[:length]

	c = checksum(s)
	while len(c) % 2 == 0:
		c = checksum(c)

	print(c)

inp = "00101000101111010"
solve(inp, 272)
solve(inp, 35651584)
