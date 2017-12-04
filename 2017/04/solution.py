#!/usr/bin/env python3

f = open("input.txt")
raw = f.readlines()

answer_1 = 0
answer_2 = 0

for l in raw:
	words = l.strip().split()
	if len(words) == len(set(words)):
		answer_1 += 1

	anaSet = set([str(sorted(x)) for x in words])
	if len(words) == len(anaSet):
		answer_2 += 1

print(answer_1)
print(answer_2)
