#!/usr/bin/env python3

import re

f = open("input.txt")
raw = f.readlines()

tls = 0

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
			break

	if valid == True:
		tls += 1

print(tls)

ssl = 0

for l in raw:
	line = l.strip()
	parts = re.split("[\[\]]", line)

	target = set()
	found = set()

	for i, p in enumerate(parts):
		if i % 2 == 0:
			for j in range(len(p) - 2):
				if p[j] == p[j+2] and p[j] != p[j+1]:
					target.add(p[j+1] + p[j] + p[j+1])

	for i, p in enumerate(parts):
		if i % 2: # inside brackets
			for t in target:
				if t in p:
					found.add(t)

	if len(found) > 0 and len(target) > 0:
		ssl += 1

print(ssl)
