#!/usr/bin/env python3

f = open("input.txt")
phrases = [x.strip().split() for x in f.readlines()]

answer1 = 0
answer2 = 0

for phrase in phrases:
	if len(phrase) == len(set(phrase)):
		answer1 += 1

	if len(phrase) == len(set([str(sorted(x)) for x in phrase])):
		answer2 += 1

print(answer1)
print(answer2)
