#!/usr/bin/env python3

f = open("input1.txt")
c = f.read()
f.close()

fl = 0

for i, b in enumerate(c):
	if (b == "("):
		fl += 1
	elif (b == ")"):
		fl -= 1
		if fl == -1:
			print(i + 1)
			exit()