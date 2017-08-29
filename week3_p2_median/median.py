import heapq
def getMedian(arr):
	medians = []

	maxh = []
	minh = []

	maxh_to_minh = True 
	for num in arr:
		if maxh_to_minh:
			heapq.heappush(maxh, -num)
			val = -heapq.heappop(maxh)
			heapq.heappush(minh, val)
		else:
			heapq.heappush(minh, num)
			val = heapq.heappop(minh)
			heapq.heappush(maxh, -val)
		maxh_to_minh = not maxh_to_minh
		if len(minh) > len(maxh):
			medians.append(minh[0])
		else:
			medians.append(min(minh[0], -maxh[0]))

		#print maxh, minh


	print sum(medians) % 10000


def main():
	fname = "Median.txt"
	f = open(fname, 'r')
	arr = []
	for line in f:
		arr.append(int(line.strip()))
	getMedian(arr)
	


if __name__ == "__main__":
	main()