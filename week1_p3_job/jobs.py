import heapq
def getjob(arr, N):
	print N
	print arr
	h = []
	for (w, l) in arr:
		heapq.heappush(h, (-1.0*(w-l), -w, l))

	t = 0
	res = 0
	while h:
		score, neg_w, l = heapq.heappop(h)
		t+=l
		res += -neg_w*t
	print res

def main():
	fname = "jobs.txt"
	f = open(fname, 'r')
	line = f.next()
	N = int(line)
	arr = []
	for line in f:
		arr.append(map(int, line.strip().split()))
	getjob(arr, N)
	


if __name__ == "__main__":
	main()