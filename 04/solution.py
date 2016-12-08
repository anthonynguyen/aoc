#!/usr/bin/env python3

import functools

f = open("input.txt")
raw = f.readlines()

s = 0
valid = []
alphabet = "abcdefghijklmnopqrstuvwxyz"

# frequency is sorted descending, but letters are sorted ascending
def comp(x, y):
	if x[1] < y[1]:
		return -1
	elif x[1] > y[1]:
		return 1
	else:
		if x[0] > y[0]:
			return -1
		elif x[0] < y[0]:
			return 1
		else:
			return 0

for l in raw:
	parts = l.strip().split("-")
	name = "".join(parts[:-1])
	freq = []
	for letter in set(name):
		freq.append((letter, name.count(letter)))
	freq.sort(key = functools.cmp_to_key(comp), reverse = True)
	if len(freq) < 5:
		continue
	chksum = freq[0][0] + freq[1][0] + freq[2][0] + freq[3][0] + freq[4][0]
	parts = parts[-1].split("[")
	sid = int(parts[0])
	if chksum == parts[-1][:-1]:
		s += sid
		valid.append(l.strip())

print(s)

for v in valid:
	parts = v.split("-")
	name = " ".join(parts[:-1])
	parts = parts[-1].split("[")
	sid = int(parts[0])
	
	realName = ""
	for c in name:
		if c == " ":
			realName += " "
			continue
		i = alphabet.index(c)
		i = (i + sid) % 26
		realName += alphabet[i]
	
	if "north" in realName:
		print(sid, realName)
