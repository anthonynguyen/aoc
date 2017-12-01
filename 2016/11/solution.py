#!/usr/bin/env python3

import copy
import itertools
import re

f = open("input_small.txt")
raw = f.readlines()

elements = set()

lowestwin = 100

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

def moves(state, steps):
	global lowestwin

	if not checkvalid(state):
		return

	if len(steps) > lowestwin:
		return

	cs = checkseen(state, steps)
	if cs is not None:
		steps = steps + [cs]
	else:
		return

	if checkwin(state):
		l = len(steps)
		if l < lowestwin:
			lowestwin = l
		return

	current = state["current"]

	allElems = ["G"+g for g in state["floors"][current][0]] + ["M"+m for m in state["floors"][current][1]]
	pairings = itertools.combinations(allElems, 2)

	lowest = 0
	for i in range(3):
		if len(state["floors"][i][0]) + len(state["floors"][i][1]):
			lowest = i
			break

	for p in pairings:
		if current < 3:
			upState = copystate(state)
			upState["current"] += 1

			f = p[0][1:]
			s = p[1][1:]

			if p[0][0] == "G":
				upState["floors"][current][0].remove(f)
				upState["floors"][current + 1][0].append(f)
			else:
				upState["floors"][current][1].remove(f)
				upState["floors"][current + 1][1].append(f)

			if p[1][0] == "G":
				upState["floors"][current][0].remove(s)
				upState["floors"][current + 1][0].append(s)
			else:
				upState["floors"][current][1].remove(s)
				upState["floors"][current + 1][1].append(s)

			moves(upState, steps)

		# if current > 0:
		# 	downState = copystate(state)
		# 	downState["current"] -= 1
		
		# 	f = p[0][1:]
		# 	s = p[1][1:]

		# 	if p[0][0] == "G":
		# 		downState["floors"][current][0].remove(f)
		# 		downState["floors"][current - 1][0].append(f)
		# 	else:
		# 		downState["floors"][current][1].remove(f)
		# 		downState["floors"][current - 1][1].append(f)

		# 	if p[1][0] == "G":
		# 		downState["floors"][current][0].remove(s)
		# 		downState["floors"][current - 1][0].append(s)
		# 	else:
		# 		downState["floors"][current][1].remove(s)
		# 		downState["floors"][current - 1][1].append(s)

		# 	if downState not in steps:
		# 		try:
		# 			r = moves(downState, steps + [downState])
		# 		except RecursionError:
		# 			pass


	for e in allElems:
		if current < 3:
			upState = copystate(state)
			upState["current"] += 1
		
			ee = e[1:]
			if e[0] == "G":
				upState["floors"][current][0].remove(ee)
				upState["floors"][current + 1][0].append(ee)
			else:
				upState["floors"][current][1].remove(ee)
				upState["floors"][current + 1][1].append(ee)

			moves(upState, steps)

		if current > 0 and current > lowest:
			downState = copystate(state)
			downState["current"] -= 1
		
			ee = e[1:]
			if e[0] == "G":
				downState["floors"][current][0].remove(ee)
				downState["floors"][current - 1][0].append(ee)
			else:
				downState["floors"][current][1].remove(ee)
				downState["floors"][current - 1][1].append(ee)

			moves(downState, steps)

moves(state, [])

print(lowestwin - 1)
