import random
import copy
def pickRandomEdge(G):
	i = random.choice(G.keys())
	j = random.choice(G[i])
	return i, j

def karger(G):
	while len(G) > 2:
		i, j = pickRandomEdge(G)
		G[i].extend(G[j])
		for x in G[j]:
			G[x].remove(j)
			G[x].append(i)
			
		#remove self-loop:
		while i in G[i]:
			G[i].remove(i)

		del G[j]
	return len(G.values()[0])

fname = 'kargerMinCut.txt'
f = open(fname, 'r')
Graph = {}
for line in f:
	arr = line.split()
	Graph[arr[0]] = arr[1:]

minimumcut=2**32

for i in range(200):
	cuts = karger(copy.deepcopy(Graph))
	print cuts
	if cuts<minimumcut:
		minimumcut=cuts
print minimumcut