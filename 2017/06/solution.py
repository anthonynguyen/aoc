#!/usr/bin/env python3

f = open("input.txt")
nums = [int(x) for x in f.read().strip().split()]

seen = []
steps = 0

while True:
	m = max(nums)
	pos = nums.index(m)
	nums[pos] = 0

	for i in range(m):
		nums[(pos + 1 + i) % len(nums)] += 1

	steps += 1
	if nums in seen:
		break

	seen.append(nums[:])

print(steps)
print(len(seen) - seen.index(nums))
