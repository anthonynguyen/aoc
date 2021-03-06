#!/usr/bin/env python3

total = 0

with open("input2.txt") as f:
	for line in f.readlines():
		p = line.strip().split("x")
		if len(p) != 3:
			print(p)
			break
		s1 = int(p[0])
		s2 = int(p[1])
		s3 = int(p[2])
		total += 2 * s1 * s2 + 2 * s2 * s3 + 2 * s1 * s3 + min(s1 * s2, s2 * s3, s1 * s3)
	f.close()

print(total)