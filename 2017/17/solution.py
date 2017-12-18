#!/usr/bin/env python3

inp = 363

buf = [0]
ind = 0

for v in range(2017):
	ind = (ind + inp) % len(buf) + 1
	buf.insert(ind, v + 1)

print(buf[ind + 1])

ind = 0
ans = 0
for v in range(50000000):
	ind = (ind + inp) % (v + 1) + 1
	if ind == 1:
		ans = v + 1

print(ans)
