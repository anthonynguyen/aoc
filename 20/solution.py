#!/usr/bin/env python3

f = open("input.txt")
lines = [l.strip().split("-") for l in f.readlines()]
ps = sorted([(int(x[0]), int(x[1])) for x in lines])

for i in range(len(ps) - 1):
	if ps[i][1] + 1 < ps[i+1][0]:
		print(ps[i][1] + 1)
		break

h,t = 0, 0
for a, b in ps:
	if h < a - 1:
		t += a - h - 1
	h = max(h, b)

print(t + (4294967295 - h))
