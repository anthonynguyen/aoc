#!/usr/bin/env python3

f = open("input.txt")
raw = f.readlines()

valid = 0

for l in raw:
	sides = sorted(list(map(int, l.split())))
	if sides[0] + sides[1] > sides[2]:
		valid += 1

print(valid)

# ------------------------------

valid = 0

for i in range(len(raw) // 3):
	start = i * 3
	nums = []
	for j in range(3):
		nums.append(list(map(int, raw[start+j].split())))

	for j in range(3):
		sides = sorted([nums[0][j], nums[1][j], nums[2][j]])
		if sides[0] + sides[1] > sides[2]:
			valid += 1

print(valid)
