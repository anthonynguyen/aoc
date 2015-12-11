#!/usr/bin/env python3

import re

litsum = 0
encsum = 0

with open("input8.txt") as f:
	for l in f.readlines():
		line = l.strip()
		litsum += len(line)

		line = line.replace("\\", "\\\\")
		line = line.replace("\"", "\\\"")

		encsum += len(line) + 2

print(encsum - litsum)
print(encsum)
print(litsum)