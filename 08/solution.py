#!/usr/bin/env python3

f = open("input.txt")
raw = f.readlines()

screen = []

for i in range(6):
	h = []
	for j in range(50):
		h.append(False)
	screen.append(h)

for l in raw:
	line = l.strip()

	parts = line.split()
	cmd = parts[0]

	if cmd == "rect":
		dim = parts[1].split("x")
		dim[0] = int(dim[0])
		dim[1] = int(dim[1])
		for i in range(dim[0]):
			for j in range(dim[1]):
				screen[j][i] = True
	elif cmd == "rotate":
		if parts[1] == "row":
			y = parts[2].split("=")
			y = int(y[1])

			n = int(parts[4])

			screen[y] = screen[y][-n:] + screen[y][:-n]
		if parts[1] == "column":
			x = parts[2].split("=")
			x = int(x[1])

			n = int(parts[4])

			c = [row[x] for row in screen]
			c = c[-n:] + c[:-n]

			for i in range(len(screen)):
				screen[i][x] = c[i]

l = 0
for r in screen:
	for c in r:
		if c:
			l += 1

print(l)

for i in range(len(screen)):
	for j in range(len(screen[i])):
		if screen[i][j]:
			print("+", end=" ")
		else:
			print(" ", end=" ")

		if j % 5 == 4:
			print(" ", end = "")

	print("")
