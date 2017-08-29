import collections
import heapq

def dikstra(d, dist_map, start, end):
	# find shortest distance between two nodes, 'start' and 'end'.
	
	shortest = {start:0}
	prev = {}
	q = []
	for node in d:
		if node != start:
			shortest[node] = 2**32
			prev[node] = None
		heapq.heappush(q, (shortest[node], node))

	while q:
		(dist, node) = heapq.heappop(q)
		for neighbor in d[node]:
			score = dist + dist_map[(node, neighbor)]
			#print score
			if score < shortest[neighbor]:
				shortest[neighbor] = score
				prev[neighbor] = node
				heapq.heappush(q, (score, neighbor))


#	print shortest
#	print prev
	path = [end]
	v = end
	while v != start:
		
		v = prev[v]
		path.append(v)
	#print '->'.join(path[::-1]), shortest[end]
	return shortest[end]

def main():
	fname = 'dikstraData.txt'
	f = open(fname, 'r')

	node_dist_map = {}
	d = collections.defaultdict(set)
	for line in f:
		tmp = line.split()
		node = tmp[0]
		for neighbor in tmp[1:]:
			n, dist = neighbor.split(',')
			d[node].add(n)
			node_dist_map[(node, n)] = int(dist)

	request_nodes = [7,37,59,82,99,115,133,165,188,197]
	answer = []
	start = '1'
	for target in request_nodes:
		answer.append(dikstra(d, node_dist_map, start, str(target)))
	print answer

if __name__ == "__main__":
	main()
	
