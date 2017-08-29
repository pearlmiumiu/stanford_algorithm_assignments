import heapq
class TreeNode():
	def __init__(self, val):
		self.val = val
		
		self.left = None
		self.right = None


def huff(arr):
	print len(arr)
	newarr = [ (x, TreeNode(str(i))) for i, x in enumerate(arr) ]
	heapq.heapify(newarr)
	
	
	while len(newarr)>=2:
		#print len(newarr)
		(w1, n1) = heapq.heappop(newarr)

		(w2, n2) = heapq.heappop(newarr)
		# merge n1, n2

		node = TreeNode(n1.val +" "+ n2.val)
		node.left = n1
		node.right = n2
		heapq.heappush(newarr, (w1+w2, node))
	root = newarr[0][1]
	dfs(root)
	#return root

def dfs(root):
	st = [(root, "")]
	maxl = 0
	minl = 2**32
	while st:
		(v,c) = st.pop()
		if not v.left and not v.right:
			print v.val, c
			if len(c) > maxl:
				maxl = len(c)
			if len(c) < minl:
				minl = len(c)
			
		if v.right:
			st.append((v.right, c + "1") )
		if v.left:
			st.append((v.left, c + "0"))

	print 'max, min len = ', maxl, minl
	print 0.28*2 + 0.27*2 + 0.4 + 0.45 + 0.3




def main():
	fname = "huffman_test.txt"
	f = open(fname, 'r')
	line = f.next()
	N = int(line)
	arr = []
	for line in f:
		arr.append(int(line.strip()))
	
	huff(arr)
	


if __name__ == "__main__":
	main()