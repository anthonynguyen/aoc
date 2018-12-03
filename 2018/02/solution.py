#!/usr/bin/env python3

import itertools

lines = [l.strip() for l in open("input.txt")]

twocount = 0
threecount = 0

for line in lines:
    groups = [list(v) for k,v in itertools.groupby(sorted(line))]

    ftwo = False
    fthree = False

    for grp in groups:
        if len(grp) == 2:
            ftwo = True
        elif len(grp) == 3:
            fthree = True

    if ftwo:
        twocount += 1

    if fthree:
        threecount += 1

print(twocount * threecount)

def diff(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d

foundpair = ()
for i in range(len(lines)):
    found = False
    for j in range(i + 1, len(lines)):
        if diff(lines[i], lines[j]) == 1:
            foundpair = (lines[i], lines[j])
            found = True
            break

    if found:
        break

x, y = foundpair
print("".join(x[i] for i in range(len(x)) if x[i] == y[i]))
