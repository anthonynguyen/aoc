#!/usr/bin/env python3

import json

def recsum(r):
	s = 0

	if isinstance(r, list):
		d = r
	elif isinstance(r, dict):
		if "red" in r.values():
			return 0
		else:
			d = r.values()
	else:
		return 0

	for v in d:
		try:
			s += v
		except:
			s += recsum(v)

	return s

with open("input12.txt") as f:
	d = json.loads(f.read())
	print(recsum(d))
