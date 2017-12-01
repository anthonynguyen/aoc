#!/usr/bin/env python3

f = open("input.txt")
raw = f.read().strip()
f.close()

full = len(raw)
half = len(raw) // 2

answer_1 = 0
answer_2 = 0

for i in range(full):
	if raw[i] == raw[(i+1) % full]:
		answer_1 += int(raw[i])

for i in range(full):
	if raw[i] == raw[(i+(half)) % full]:
		answer_2 += int(raw[i])

print(answer_1)
print(answer_2)
