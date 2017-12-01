#!/usr/bin/env python3

import re

table = {"b": 956}
ptable = {}

inst = re.compile("(.+?) -> (.+)")
sinst = re.compile("(.+) (.+) (.+)")

class Instruction:
	def __init__(self, operation, operand1, operand2 = None):
		self.operation = operation
		self.operand1 = operand1
		self.operand2 = operand2

def assign(target, value):
	global table
	table[target] = value
	print("ASSIGN {} = {}".format(target, table[target]))

def recalculate():
	global table
	global ptable

	todel = []

	for i in ptable:
		f = ptable[i]
		target = i

		try:
			o1 = int(f.operand1)
		except:
			try:
				o1 = table[f.operand1]
			except:
				continue

		if (f.operand1 == "e"):
			print("WE ARE e: {}".format(f.operand2))

		if f.operand2 is None:
			if f.operation == "NOT":
				assign(target, ~o1 % 65536)
			else:
				assign(target, o1)
			todel.append(target)
			continue

		try:
			o2 = int(f.operand2)
		except:
			try:
				o2 = table[f.operand2]
			except:
				continue

		if f.operation == "AND":
			assign(target, o1 & o2)
		elif f.operation == "OR":
			assign(target, o1 | o2)
		elif f.operation == "LSHIFT":
			assign(target, o1 << o2)
		elif f.operation == "RSHIFT":
			assign(target, o1 >> o2)
		todel.append(target)

	for i in todel:
		del ptable[i]

with open("input72.txt") as f:
	for l in f.readlines():
		m = inst.match(l)

		if m is None:
			break

		target = m.group(2)
		try:
			v = int(m.group(1))
			table[target] = v
			assign(target, v)
			continue
		except:
			pass

		if m.group(1)[:3] == "NOT":
			ptable[target] = Instruction("NOT", m.group(1)[4:])
			continue
		elif " " not in m.group(1):
			ptable[target] = Instruction("ASSIGN", m.group(1))
			continue

		n = sinst.match(m.group(1))
		if n is None:
			print("DEAD SHIT: " + l)
			continue

		ptable[target] = Instruction(n.group(2), n.group(1), n.group(3))

plen = len(ptable) + 1
while len(ptable) != plen:
	plen = len(ptable)
	recalculate()

print(table["a"])