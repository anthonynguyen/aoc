#!/usr/bin/env python3

import itertools

f = open("input.txt")
lines = [l.strip().split() for l in f.readlines()]

def solve(inp):
	global lines
	inp = list(inp)
	for l in lines:
		cmd = l[0]

		if cmd == "swap" and l[1] == "position":
			a = int(l[2])
			b = int(l[5])
			inp[a], inp[b] = inp[b], inp[a]
		elif cmd == "swap" and l[1] == "letter":
			a = inp.index(l[2])
			b = inp.index(l[5])
			inp[a], inp[b] = inp[b], inp[a]
		elif cmd == "rotate":
			if l[1] == "based":
				s = inp.index(l[6])
				inp = inp[-1:] + inp[:-1]
				inp = inp[-s:] + inp[:-s]
				if s >= 4:
					inp = inp[-1:] + inp[:-1]
			else:
				d = l[1]
				s = int(l[2])
				if d == "right":
					inp = inp[-s:] + inp[:-s]
				else:
					inp = inp[s:] + inp[:s]
		elif cmd == "reverse":
			a = int(l[2])
			b = int(l[4])
			s = inp[a:b+1][::-1]
			inp = inp[:a] + s[:] + inp[b+1:]
		elif cmd == "move":
			a = int(l[2])
			b = int(l[5])
			v = inp[a]
			del inp[a]
			inp.insert(b, v)

	return "".join(inp)

print(solve("abcdefgh"))

for p in itertools.permutations("abcdefgh"):
	if solve(p) == "fbgdceah":
		print("".join(p))
		break
