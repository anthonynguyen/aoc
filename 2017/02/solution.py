#!/usr/bin/env python3

raw = open("input.txt").readlines()
nums = [[int(x) for x in l.strip().split()] for l in raw]

answer1 = 0
answer2 = 0

for line in nums:
	answer1 += max(line) - min(line)

	for i in line:
		for j in line:
			if i != j and i % j == 0:
				answer2 += (i// j)
				break

print(answer1)
print(answer2)
