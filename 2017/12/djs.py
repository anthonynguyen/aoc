#!/usr/bin/env python3

lines = [x.strip().split() for x in open("input.txt")]

graph = {}
for l in lines:
	graph[int(l[0])] = [int(x.strip(",")) for x in l[2:]]

sets = set([frozenset([g]) for g in graph])

def find(x):
	for subset in sets:
		if x in subset:
			return subset

for g in graph:
	for c in graph[g]:
		sg = find(g)
		sc = find(c)
		if sg != sc:
			sets.add(frozenset.union(sg, sc))
			sets.remove(sg)
			sets.remove(sc)

print(len(find(0)))
print(len(sets))
