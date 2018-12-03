#!/usr/bin/env python3

from collections import defaultdict
import re

lines = [l.strip() for l in open("input.txt")]

claimre = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

claims = []
cells = defaultdict(int)

for line in lines:
    matches = claimre.search(line)
    c = int(matches.group(1))
    x = int(matches.group(2))
    y = int(matches.group(3))
    w = int(matches.group(4))
    h = int(matches.group(5))
    claims.append((c, x, y, w, h))

    for i in range(w):
        for j in range(h):
            cells[(x + i, y + j)] += 1

answer1 = 0
for c in cells:
    if cells[c] >= 2:
        answer1 += 1

print(answer1)

def intersects(c1, c2):
    n1, x1, y1, w1, h1 = c1
    n2, x2, y2, w2, h2 = c2
    return not ((x1 + w1) < x2 or x1 > (x2 + w2) or (y1 + h1) < y2 or y1 > (y2 + h2))

overlaps = [0] * len(claims)

for i in range(len(claims)):
    for j in range(i + 1, len(claims)):
        if intersects(claims[i], claims[j]):
            overlaps[i] += 1
            overlaps[j] += 1

for i in range(len(overlaps)):
    if overlaps[i] == 0:
        print(claims[i][0])
