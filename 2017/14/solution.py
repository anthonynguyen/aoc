#!/usr/bin/env python3

def bits(hexc):
	return bin(int(hexc, 16))[2:].zfill(4)

def run(lengths):
	position = 0
	skip = 0
	
	sequence = list(range(256))

	for _ in range(64):
		for l in lengths:
			for i in range(l // 2):
				now = (position + i) % len(sequence)
				later = (position + l - 1 - i) % len(sequence)
				sequence[now], sequence[later] = sequence[later], sequence[now]
			
			position += l + skip
			skip += 1
	
	return sequence

def hash(string):
	lengths = [ord(x) for x in string] + [17, 31, 73, 47, 23]
	seq = run(lengths)
	
	hashstr = ""
	for i in range(len(seq) // 16):
		num = 0
		for j in range(16):
			num ^= seq[i * 16 + j]
		hashstr += hex(num)[2:].zfill(2)
		
	return hashstr

key = "hwlqcszp"

grid = []
for i in range(128):
	has = hash(key + "-" + str(i))
	row = list(int(x) for x in "".join([bits(x) for x in has]))
	grid.append(row)

filled = [(x, y) for x in range(128) for y in range(128) if grid[y][x]]
print(len(filled))

regions = 0
seen = []

for f in filled:
	if f in seen:
		continue

	q = [f]
	
	while q:
		sq = q.pop()
		if sq in seen or sq not in filled:
			continue

		seen.append(sq)

		x, y = sq
		q += [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]
	
	regions += 1

print(regions)
