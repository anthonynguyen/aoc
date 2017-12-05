#!/usr/bin/env python3

raw = open("input.txt").read().strip()

full = len(raw)
half = len(raw) // 2

answer1 = 0
answer2 = 0

for i in range(full):
	if raw[i] == raw[(i+1) % full]:
		answer1 += int(raw[i])

	if raw[i] == raw[(i+(half)) % full]:
		answer2 += int(raw[i])

print(answer1)
print(answer2)
