#!/usr/bin/env python3

import re

f = open("input.txt")
raw = f.read()
string = raw

n = 0

while len(string):
	m = re.match("\((\d+)x(\d+)\)(.+)", string)
	if m is not None:
		f = int(m.group(1))
		s = int(m.group(2))
		string = m.group(3)
		string = string[f:]
		n += f * s
	else:
		m = re.match("([A-Z]+)(\(.+)", string)
		p = m.group(1)
		string = m.group(2)
		n += len(p)

print(n)

r = re.compile(r"(.*?)\((\d+)x(\d+)\)(.+)")

def findn(s):
	if "(" not in s:
		return len(s)

	m = r.match(s)
	prev = m.group(1)
	f = int(m.group(2))
	s = int(m.group(3))
	rest = m.group(4)

	return findn(prev) + findn(rest[:f]) * s + findn(rest[f:])

print(findn(raw))
