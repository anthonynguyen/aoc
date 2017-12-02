#!/usr/bin/env python3

f = open("input.txt")
raw = f.readlines()

nums = [[int(x) for x in l.strip().split()] for l in raw]

answer_1 = 0
answer_2 = 0

for line in nums:
	answer_1 += max(line) - min(line)

for line in nums:
	lts = sorted(line, reverse = True)
	for i in range(len(lts)):
		breakNow = False
		for j in range(i+1, len(lts)):
			if lts[i] % lts[j] == 0:
				answer_2 += (lts[i] // lts[j])
				breakNow = True
				break

print(answer_1)
print(answer_2)
