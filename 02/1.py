#!/usr/bin/env python3

f = open("1.in")
raw = f.readlines()

a = ["123", "456", "789"]

maxx = 2
maxy = 2

x = 1
y = 1

comb = []

for l in raw:
    for c in l.strip():
        if c == "R":
            if x < maxx:
                x += 1
        elif c == "L":
            if x > 0:
                x -= 1
        elif c == "D":
            if y < maxy:
                y += 1
        elif c == "U":
            if y > 0:
                y -= 1
    
    comb.append(a[y][x])

print(comb)