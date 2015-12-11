#!/usr/bin/env python3

inp = "3113322113"

def looksay(ipp, m):
	new = ""
	curchar = ipp[0]
	n = 1
	i = 1
	while i < len(ipp):
		if ipp[i] == curchar:
			n += 1
			i += 1
		else:
			new += str(n) + curchar
			curchar = ipp[i]
			n = 1
			i += 1

	new += str(n) + curchar

	if m > 1:
		return looksay(new, m - 1)

	return new


print(len(looksay(inp, 40)))
print(len(looksay(inp, 50)))