#!/usr/bin/env python3

raw = open("input.txt").read().strip()

def solve(rows):
	global raw
	row = [True if x == "." else False for x in raw]
	new = row[:]
	l = len(row)

	safe = row.count(True)

	for _ in range(rows - 1):
		for i in range(l):
			a = not i or (row[i-1])
			c = (i == (l - 1)) or (row[i+1])

			if a == c:
				new[i] = True
				safe += 1
			else:
				new[i] = False

		row, new = new, row

	print(safe)

solve(40)
solve(400000)
