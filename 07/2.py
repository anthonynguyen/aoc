#!/usr/bin/env python3

import re

f = open("1.in")
raw = f.readlines()

ips = 0

for l in raw:
	line = l.strip()
	valid = None
	brackets = "[]"

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
		ips += 1

print(ips)
