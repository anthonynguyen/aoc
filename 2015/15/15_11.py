#!/usr/bin/env python3

import re

ingr = {}
igrs = []

with open("input15_1.txt") as f:
	for l in f.readlines():
		line = l.strip()
		ingredient, _, capacity, _, durability, _, flavour, _, texture, _, calories = l.split(" ")
		ingr[ingredient[:-1]] = (int(capacity[:-1]), int(durability[:-1]), int(flavour[:-1]), int(texture[:-1]), int(calories))
		igrs.append((int(capacity[:-1]), int(durability[:-1]), int(flavour[:-1]), int(texture[:-1]), int(calories)))
maxscore = 0
for i in range(100):
	for j in range(100-i):
		if i + j != 100:
			continue

		capacity = 0
		capacity += igrs[0][0] * i
		capacity += igrs[1][0] * j

		durability = 0
		durability += igrs[0][1] * i
		durability += igrs[1][1] * j

		flavor = 0
		flavor += igrs[0][2] * i
		flavor += igrs[1][2] * j

		texture = 0
		texture += igrs[0][3] * i
		texture += igrs[1][3] * j

		if capacity < 0:
			capacity = 0

		if durability < 0:
			durability = 0

		if flavor < 0:
			flavor = 0

		if texture < 0:
			texture = 0

		prod = capacity * durability * flavor * texture

		if (i, j) == (44, 56) or (i, j) == (56, 44):
			print((capacity, durability, flavor, texture))
			print((i, j))
			print(prod)

		if prod > maxscore:
			maxscore = prod

print(ingr)
print(maxscore)