#!/usr/bin/env python3

import re
import itertools

lre = re.compile("(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.")

happiness = {}

with open("input13_1.txt") as f:
	for l in f.readlines():
		line = l.strip()
		m = lre.match(line)
		if m is None:
			break

		if m.group(1) not in happiness:
			happiness[m.group(1)] = {}

		gap = int(m.group(3))
		if m.group(2) == "lose":
			gap *= -1

		happiness[m.group(1)][m.group(4)] = gap

people = ["Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory"]


lenp = len(people)
maxp = -1
maxpp = []
for perm in itertools.permutations(people):
	s = 0
	for i, p in enumerate(perm):
		left = happiness[p][perm[i-1]]

		if i == len(people) - 1:
			right = happiness[p][perm[0]]
		else:
			right = happiness[p][perm[i+1]]

		s += left
		s += right

	if s > maxp:
		maxp = s
		maxpp = perm

print(maxp)
print(maxpp)