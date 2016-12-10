#!/usr/bin/env python3

import collections

f = open("input.txt")
raw = f.readlines()

bots = collections.defaultdict(list)
output = collections.defaultdict(list)

new = []

for l in raw:
	line = l.strip()
	parts = line.split()

	if parts[0] == "value":
		v = int(parts[1])
		t = int(parts[5])

		bots[t].append(v)
	else:
		new.append(line)

changed = True
while changed:
	changed = False
	nn = []
	for line in new:
		parts = line.split()
		s = int(parts[1])

		if len(bots[s]) == 2:
			l = parts[5]
			ln = int(parts[6])

			h = parts[10]
			hn = int(parts[11])

			if l == "output":
				output[ln].append(min(bots[s]))
			else:
				bots[ln].append(min(bots[s]))

			if h == "output":
				output[hn].append(max(bots[s]))
			else:
				bots[hn].append(max(bots[s]))
			changed = True
		else:
			nn.append(line)

	new = nn

for b in bots:
	if 61 in bots[b] and 17 in bots[b]:
		print(b)
		break

print(output[0][0] * output[1][0] * output[2][0])
