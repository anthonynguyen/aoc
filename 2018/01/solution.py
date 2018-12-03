#!/usr/bin/env python3

lines = open("input.txt").readlines()
numbers = [int(x.strip()) for x in lines]

answer1 = sum(numbers)
answer2 = 0

freq = 0
seen = {}
num = 0

while True:
    freq += numbers[num]

    if freq in seen:
        answer2 = freq
        break
    else:
        seen[freq] = 1

    num = (num + 1) % len(numbers)

print(answer1)
print(answer2)
