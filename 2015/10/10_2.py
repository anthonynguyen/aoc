#!/usr/bin/env python3

inp = "3113322113"

def firstn(s, n):
	i = 0
	for c in s:
		if c == n:
			i += 1
		else:
			break

	return i


def looksay(ipp):
	newn = ""
	s = ipp[:]

	while True:
		c = s[0]
		n = firstn(s, c)
		newn += str(n) + str(c)
		s = s[n:]
		if s == "":
			break

	return newn



d = 50
for i in range(d):
	print("{}: {}".format(i, len(inp)))
	inp = looksay(inp)

#print(inp)
print(len(inp))