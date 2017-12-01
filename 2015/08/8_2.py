#!/usr/bin/env python3

import re

litsum = 0
realsum = 0

hx = re.compile(r"\\x..")

with open("input8.txt") as f:
	for l in f.readlines():
		line = l.strip()
		litsum += len(line)

		line = line.replace("\\\"", ".")
		line = line.replace("\\\\", ".")
		line = re.sub(r"\\x..", ".", line)

		realsum += len(line)

print(litsum - realsum)
print(litsum)
print(realsum)