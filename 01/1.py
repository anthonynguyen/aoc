#!/usr/bin/env python3

f = open("1.in")

raw = f.read()

parts = raw.split(", ")

current = [0, 0]

direction = 0 # 0 - n, 1 - e, 2 - s, 3 - w

for part in parts:
    d = part[0]
    num = int(part[1:])
    if d == "R":
        direction += 1
    else:
        direction -= 1
    
    direction %= 4
    
    if direction == 0:
        current[0] += num
    elif direction == 1:
        current[1] += num
    elif direction == 2:
        current[0] -= num
    else:
        current[1] -= num

print(abs(current[0]) + abs(current[1]))
