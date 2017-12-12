#!/usr/bin/env python3

lines = [x.strip().split() for x in open("input.txt")]

graph = {}
for l in lines:
	graph[int(l[0])] = [int(x.strip(",")) for x in l[2:]]

def bfs(start):
	seen = []
	queue = [start]
	while queue:
		node = queue.pop()
		for neighbour in graph[node]:
			if neighbour not in seen:
				seen.append(neighbour)
				queue.append(neighbour)

	return seen

groups = []
for i in graph:
	g = sorted(bfs(i))
	if g not in groups:
		groups.append(g)

print(len(bfs(0)))
print(len(groups))
