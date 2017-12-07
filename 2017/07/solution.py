#!/usr/bin/env python3

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]

programs = {}
child = set()
everybody = set()

for l in lines:
	parts = l.split()
	me = parts[0]
	everybody.add(me)

	weight = int(parts[1][1:-1])

	children = [c.replace(",", "") for c in parts[3:]]

	while "" in children:
		children.remove("")

	for c in children:
		child.add(c)

	programs[me] = (weight, children[:])

root = list((everybody - child))[0]

def weightOf(program, allPrograms):
	prog = allPrograms[program]
	if len(prog[1]) == 0:
		return prog[0]
	else:
		return sum([weightOf(c, allPrograms) for c in prog[1]]) + prog[0]

weights = {}
for p in programs:
	weights[p] = weightOf(p, programs)

def nodeBalanced(program):
	global programs, weights

	children = programs[program][1]
	setLen = len(set([weights[c] for c in children]))

	if len(children) <= 1 and setLen == len(children):
		return True
	elif len(children) > 1 and setLen == 1:
		return True

	return False

def inspect(p):
	global programs, weights

	print("\n-----\n{} ({}) -- {}".format(p, programs[p][0], weights[p]))
	for c in programs[p][1]:
		print("{}: {}".format(c, weights[c]))
	print("-----\n")

def explore(node):
	global programs, weights

	balanced = nodeBalanced(node)
	if balanced:
		return True

	children = programs[node][1]
	childrenBalanced = True
	for child in children:
		if not explore(child):
			childrenBalanced = False

	if childrenBalanced:
		# we're unbalanced but our children are balanced
		# => one of our children is wrong
		for c in children:
			print("{} ({}) -> {}".format(c, programs[c][0], weights[c]))

print(root, "\n-------")
explore(root)
