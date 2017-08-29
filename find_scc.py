from collections import defaultdict
def dfs(Graph, node, visited, group):
	if node in visited:
		return

	# do something to the node
	st = [node]
	while len(st)>0:
		node = st.pop()
		if node in visited:
			continue
		group.append(node)
		visited.add(node)
	
		for neighbor in Graph[node]:
			st.append(neighbor)
			
def get_reversed_graph_ordering(reversed_graph, largestNode):
	visited = set()
	group = []
	for node in xrange(largestNode, 0, -1):
		tmp = []
		dfs(reversed_graph, node, visited, tmp)
		group.append(tmp)
	group = [item for sublist in group[::-1] for item in sublist]
	return group

def main():
	fname = 'scc.txt'
	f = open(fname, 'r')
	G = defaultdict(list)
	G_reverse = defaultdict(list)
	largestNode = -1
	for line in f:
		edge = line.split()
		tail, head = int(edge[0]), int(edge[1])
		if tail > largestNode:
			largestNode = tail
		G[tail].append(head)
		G_reverse[head].append(tail)
	
	# doing dfs on reversed graph to get the correct ordering.
	group = get_reversed_graph_ordering(G_reverse, largestNode)	
	
	
	# using the group ranking to conduct dfs on the original graph.
	newvisited = set()
	scc_size = []
	for node in group:
		newgroup = []
		dfs(G, node, newvisited, newgroup)
		if len(newgroup) > 0:
			scc_size.append(len(newgroup))

	# get 5 largest connected component size
	print sorted(scc_size, reverse = True)[:5] 

if __name__ == "__main__":
	main()