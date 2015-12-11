#!/usr/bin/env python3

import re

alpha = "abcdefghijklmnopqrstuvwxyz"
inp = "hxbxwxba"

def nextl(c):
	if c == "z":
		return "a"

	return alpha[alpha.index(c) + 1]

def increment(s):
	news = list(s)
	ind = -1
	carry = True
	
	while True:
		news[ind] = nextl(news[ind])
		if news[ind] == "a":
			ind -= 1
		else:
			break

		if ind == 0:
			break

	return "".join(news)


def isvalid(s):
	trip = False
	for i, c in enumerate(s[:-2]):
		if nextl(c) == s[i+1] and nextl(nextl(c)) == s[i+2] and c != "y" and c != "z":
			trip = True

	if not trip:
		return False

	if "i" in s or "o" in s or "l" in s:
		return False

	doubles = 0
	for l in alpha:
		if l + l in s:
			doubles += 1

	if doubles < 2:
		return False

	return True

while not isvalid(inp):
	inp = increment(inp)

inp = increment(inp)
while not isvalid(inp):
	inp = increment(inp)

print(inp)