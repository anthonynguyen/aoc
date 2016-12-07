#!/usr/bin/env python3

import re

f = open("1.in")
raw = f.readlines()

ips = 0
b = 0

for l in raw:
	line = l.strip()
	valid = None
	brackets = "[]"

	parts = re.split("[\[\]]", line)

	for i, p in enumerate(parts):
		if i % 2: # inside brackets
			for j in range(len(p) - 3):
				if p[j] == p[j+3] and p[j+1] == p[j+2] and p[j] != p[j+1]:
					valid = False
					break
		else:
			for j in range(len(p) - 3):
				if p[j] == p[j+3] and p[j+1] == p[j+2] and p[j] != p[j+1]:
					valid = True
					break

		if valid == False: 
			b += 1
			break

	if valid == True:
		ips += 1

print(ips)