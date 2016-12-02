#!/usr/bin/env python3

f = open("1.in")
raw = f.readlines()

a = [
    "--1--",
    "-234-",
    "56789",
    "-ABC-",
    "--D--"
]

maxx = 4
maxy = 4

x = 0
y = 2

comb = []

for l in raw:
    for c in l.strip():
        if c == "R":
            if x < maxx and a[y][x+1] != "-":
                x += 1
        elif c == "L":
            if x > 0 and a[y][x-1] != "-":
                x -= 1
        elif c == "D":
            if y < maxy and a[y+1][x] != "-":
                y += 1
        elif c == "U":
            if y > 0 and a[y-1][x] != "-":
                y -= 1
    
    comb.append(a[y][x])

print(comb)