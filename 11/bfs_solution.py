#!/usr/bin/env python3

import collections
import itertools
import re

f = open("input_large.txt")
raw = f.readlines()

elements = set()

state = {
	"current": 0,
	"floors": [ # generator first, then chip
		[[], []],
		[[], []],
		[[], []],
		[[], []]
	]
}

i = 0

for l in raw:
	line = l.strip()
	gs = re.findall(" ([A-Za-z]+?) generator", line)
	for g in gs:
		state["floors"][i][0].append(g)
		elements.add(g)

	ms = re.findall(" ([A-Za-z]+?)\-compatible microchip", line)
	for m in ms:
		state["floors"][i][1].append(m)
		elements.add(m)

	i += 1

print(state)

numElements = len(elements)

steps = 0

def checkvalid(state):
	for floor in state["floors"]:
		if len(floor[0]): # if there are any generators on this floor
			for m in floor[1]:
				if m not in floor[0]:
					return False
	return True

def checkwin(state):
	global numElements
	if len(state["floors"][3][0]) == numElements and len(state["floors"][3][1]) == numElements:
		return True
	return False

def copystate(state):
	return {
		"current": state["current"],
		"floors": [
			[state["floors"][0][0][:], state["floors"][0][1][:]],
			[state["floors"][1][0][:], state["floors"][1][1][:]],
			[state["floors"][2][0][:], state["floors"][2][1][:]],
			[state["floors"][3][0][:], state["floors"][3][1][:]],
		]
	}

def genericstate(state):
	return {
		"current": state["current"],
		"floors": [
			[len(state["floors"][0][0]), len(state["floors"][0][1])],
			[len(state["floors"][1][0]), len(state["floors"][1][1])],
			[len(state["floors"][2][0]), len(state["floors"][2][1])],
			[len(state["floors"][3][0]), len(state["floors"][3][1])],
		]
	}

def checkseen(state, steps):
	cs = genericstate(state)
	if cs in steps:
		return None
	return cs

def updown(state, elems, d):
	ns = copystate(state)
	ns["current"] += d
	c = ns["current"]

	for e in elems:
		ee = e[1:]
		if e[0] == "G":
			ns["floors"][c-d][0].remove(ee)
			ns["floors"][c][0].append(ee)
		else:
			ns["floors"][c-d][1].remove(ee)
			ns["floors"][c][1].append(ee)

	return ns

def up(state, elems):
	return updown(state, elems, 1)

def down(state, elems):
	return updown(state, elems, -1)

# --------------------------------------

def nextmoves(state, steps, gnmoves):
	current = state["current"]

	allElems = ["G"+g for g in state["floors"][current][0]] + ["M"+m for m in state["floors"][current][1]]
	pairings = itertools.combinations(allElems, 2)

	lowest = 0
	for i in range(3):
		if len(state["floors"][i][0]) + len(state["floors"][i][1]):
			lowest = i
			break

	moves = []

	twoUp = 0

	if current < 3:
		for p in pairings:
			# TWO UP
			ns = up(state, p)
			g = genericstate(ns)
			if checkvalid(ns) and g not in gnmoves:
				moves.append((ns, steps))
				gnmoves.append(g)

	twoUp = len(moves)

	if current > 0 and current > lowest:
		for e in allElems:
			# ONE DOWN
			ns = down(state, [e])
			g = genericstate(ns)
			if checkvalid(ns) and g not in gnmoves:
				moves.append((ns, steps))
				gnmoves.append(g)

	oneDown = len(moves) - twoUp

	if not twoUp and current < 3:
		for e in allElems:
			#ONE UP
			ns = up(state, [e])
			g = genericstate(ns)
			if checkvalid(ns) and g not in gnmoves:
				moves.append((ns, steps))
				gnmoves.append(g)

	if not oneDown and current > 0 and current > lowest:
		for p in pairings:
			# TWO DOWN
			ns = down(state, p)
			g = genericstate(ns)
			if checkvalid(ns) and g not in gnmoves:
				moves.append((ns, steps))
				gnmoves.append(g)

	return moves

queue = collections.deque()
queue.append((state, []))

# store new moves generated at a given move #
nqueue = collections.deque()

# store move "hashes" at a given move # so that equivalent states are not explored
gnmoves = []

n = 0

moves = 0
maxsteps = 100
win = False

while len(queue) or len(nqueue):
	if not len(queue):
		# gnmoves = []
		moves += 1
		print(moves, len(nqueue))
		queue += nqueue
		nqueue.clear()

	cur = queue.popleft()
	state, steps = cur

	# we're checking validity when we generate moves so this is not necessary
	# if not checkvalid(state):
	# 	continue

	if len(steps) > maxsteps:
		continue

	cs = checkseen(state, steps)
	if cs is None:
		continue

	if checkwin(state):
		win = True
		break

	nqueue += nextmoves(state, steps + [cs], gnmoves)

if win:
	print(moves)
else:
	print("Didn't solve in {} steps".format(maxsteps))
