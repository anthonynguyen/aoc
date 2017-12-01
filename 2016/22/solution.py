#!/usr/bin/env python3

import collections

f = open("input.txt")
lines = [l.strip().split() for l in f.readlines()][2:]

vp = 0

for i in range(len(lines) - 1):
	a = lines[i]
	for j in range(i+1, len(lines)):
		b = lines[j]
		a_used = int(a[2][:-1])
		b_used = int(b[2][:-1])

		a_avail = int(a[3][:-1])
		b_avail = int(b[3][:-1])

		if a_used != 0 and a_used <= b_avail or b_used != 0 and b_used <= a_avail:
			vp += 1

print(vp)

# ------------------------------------------------

maxx = 34
maxy = 30

board = [[(0, 0) for i in range(maxx)] for j in range(maxy)]

avg = []
for p in lines:
	avg.append(int(p[1][:-1]))
	f = p[0].split("-")
	x = int(f[-2][1:])
	y = int(f[-1][1:])

	# used / size
	board[y][x] = (int(p[2][:-1]), int(p[1][:-1]))

avg = sum(avg) / len(avg)

def copy_board(b):
	return [a[:] for a in b]

def print_board(b):
	for y, r in enumerate(b):
		print(str(y) + "\t", end = "")
		for x, e in enumerate(r):
			if x == 0 and y == 0:
				print("!", end = "")
			elif x == 33 and y == 0:
				print("s", end = "")
			elif e[0] == 0:
				print("_", end = "")
			elif e[1] > avg*2:
				print("#", end = "")
			else:
				print(".", end = "")

			print(" ", end = "")

		print("")


def movable(board, x, y, nx, ny):
	if nx >= maxx or ny >= maxy or nx < 0 or ny < 0:
		return False

	# assume we're called on the empty square
	our_avail = board[y][x][1]
	their_used = board[ny][nx][0]

	return their_used < our_avail

visited = []
q = collections.deque()
q.append((4, 25, 0, board[:]))

target = (32, 0)

moves = 0

while len(q):
	x, y, d, b = q.popleft()

	if (x, y) in visited:
		continue

	visited.append((x, y))

	if (x, y) == target:
		moves = d
		break

	# up
	if movable(b, x, y, x, y - 1):
		nb = copy_board(b)
		nb[y][x] = (nb[y-1][x][0], nb[y][x][1])
		nb[y-1][x] = (0, nb[y-1][x][1])
		q.append((x, y - 1, d + 1, nb[:]))

	# down
	if movable(b, x, y, x, y + 1):
		nb = copy_board(b)
		nb[y][x] = (nb[y+1][x][0], nb[y][x][1])
		nb[y+1][x] = (0, nb[y+1][x][1])
		q.append((x, y + 1, d + 1, nb[:]))

	# left
	if movable(b, x, y, x - 1, y):
		nb = copy_board(b)
		nb[y][x] = (nb[y][x-1][0], nb[y][x][1])
		nb[y][x-1] = (0, nb[y][x-1][1])
		q.append((x - 1, y, d + 1, nb[:]))

	# right
	if movable(b, x, y, x + 1, y):
		nb = copy_board(b)
		nb[y][x] = (nb[y][x+1][0], nb[y][x][1])
		nb[y][x+1] = (0, nb[y][x+1][1])
		q.append((x + 1, y, d + 1, nb[:]))

# our blank space is to the left of the source at (32, 0)
# it takes 5 moves to move the blank space left with its payload
# + 1 move to move the payload into the final blank

print(moves + 32 * 5 + 1)
