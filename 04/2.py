#!/usr/bin/env python3

import functools

# aczupnetwp-dnlgpyrpc-sfye-dstaatyr-561[patyc]
# jsehsyafy-vqw-ljsafafy-866[nymla]
# tyepcyletzylw-ncjzrpytn-prr-opawzjxpye-743[cnrdl]
# foadouwbu-qvcqczohs-obozmgwg-662[lamjh]
# ckgvutofkj-pkrrehkgt-zkinturume-436[krtue]

f = open("1.in")
raw = f.readlines()

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
		valid.append(l.strip())

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
	
	print(sid, realName)
