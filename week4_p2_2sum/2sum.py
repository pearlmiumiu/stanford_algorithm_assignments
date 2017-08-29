
def get2sum(arr):
	# in the interval [-10000, 10000]
	#print len(arr)
	N = 10000
	count = 0
	# target i would be at location i + N
	targets = set(range(-N, N+1))
	visited = set()
	S = {}
	for i, val in enumerate(arr):
		for target in (targets-visited):
			if val - target in S and i != S[val-target]:
				visited.add(target)

				
		S[-val] = i
		if (i%100==0):
			print i, len(visited)
	#print visited
	print len(visited)





def main():
	fname = "2sum.txt"
	f = open(fname, 'r')
	arr = []
	for line in f:
		arr.append(int(line.strip()))
	#print arr
	get2sum(set(arr))
	


if __name__ == "__main__":
	main()