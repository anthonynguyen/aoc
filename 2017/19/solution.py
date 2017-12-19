#!/usr/bin/env python3

maze = [x.rstrip() for x in open("input.txt")]
def sq(y, x):
	try:
		return maze[y][x]
	except:
		return " "

coord = (0, maze[0].index("|")) # y, x
direction = (1, 0) # (dy, dx)

seen = []
message = ""
steps = 0

while True:
	steps += 1

	y, x = coord
	dy, dx = direction

	if sq(y, x).isalpha():
		message += sq(y, x)

	if sq(y + dy, x + dx) != " ":
		coord = (y + dy, x + dx)
	elif dy and sq(y, x - 1) != " ":
		coord = (y, x - 1)
		direction = (0, -1)
	elif dy and sq(y, x + 1) != " ":
		coord = (y, x + 1)
		direction = (0, 1)
	elif dx and sq(y - 1, x) != " ":
		coord = (y - 1, x)
		direction = (-1, 0)
	elif dx and sq(y + 1, x) != " ":
		coord = (y + 1, x)
		direction = (1, 0)
	else:
		break

print(message)
print(steps)
