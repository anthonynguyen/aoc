#!/usr/bin/env python3

import hashlib

# d = hashlib.md5((inp + str(i)).encode("utf-8")).hexdigest()

inp = "ngcjuoqr"
i = 0

keys = []
check = []

while len(keys) < 64:
	d = hashlib.md5((inp + str(i)).encode("utf-8")).hexdigest()

	for j in range(len(d) - 2):
		if d[j] == d[j+1] == d[j+2]:
			check.append((d[j], i + 1000))
			break

	remove = []

	for ic, c in enumerate(check[:-1]):
		if i > c[1]:
			remove.append(ic)
		else:
			for j in range(len(d) - 4):
				if c[0] == d[j] == d[j+1] == d[j+2] == d[j+3] == d[j+4]:
					remove.append(ic)
					keys.append(c[1] - 1000)
					break

	for r in remove[::-1]:
		del check[r]

	i += 1

print(sorted(keys))
