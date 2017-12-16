#!/usr/bin/env python3

f = open("input.txt")

inst = []
# parse the instructions so execution is faster
# probably not needed, but I did it when I was trying to brute force part 2 :(
for i in f.read().strip().split(","):
	if i[0] == 's':
		inst.append((0, int(i[1:]), 0))
	elif i[0] == 'x':
		a, b = [int(x) for x in i[1:].split('/')]
		inst.append((1, a, b))
	elif i[0] == 'p':
		a, b = i[1:].split('/')
		inst.append((2, a, b))

programs = list("abcdefghijklmnop")
seen = [programs[:]]

while True:
	if programs in seen:
		index = seen.index(programs)
		if len(seen) > index + 1:
			programs = seen[index + 1]
			break

	for i, a, b in inst:
		if i == 0:
			programs = programs[-a:] + programs[:-a]
		elif i == 1:
			programs[a], programs[b] = programs[b], programs[a]
		elif i == 2:
			a, b = programs.index(a), programs.index(b)
			programs[a], programs[b] = programs[b], programs[a]

	if programs not in seen:
		seen.append(programs[:])

print("".join(seen[1]))
print("".join(seen[(1000000000) % len(seen)]))
