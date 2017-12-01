#!/usr/bin/env python3

inp = 3014387

def series(inp):
	elves = [True for i in range(inp)]
	pres = inp

	nexti = 0

	lastdeletion = 0

	while pres > 1:
		if not elves[nexti]:
			nexti = (nexti + 1) % inp
			continue
		across = pres // 2
		c = nexti
		while across:
			c = (c + 1) % inp
			if elves[c]:
				across -= 1

		elves[c] = False
		nexti = (nexti + 1) % inp
		pres -= 1

	# print("elf #", nexti + 1, end = "\n\n")
	print(inp, nexti if nexti != 0 else inp)

for i in range(1, 82):
	series(i)
