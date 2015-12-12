#!/usr/bin/env python3

import re

with open("input12.txt") as f:
	print(sum(map(int, re.findall(r"[\"\[,:](-?\d+)\b", f.read()))))