def inversion(arr):
	count=0
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i]> arr[j]:
				count+=1
	return count

def merge(a, b):
	m = len(a)
	n = len(b)
	i, j = 0, 0
	c = []
	for k in range(m+n):
		if i == m:
			c.append(b[j])
			j+=1
		elif j == n:
			c.append(a[i])
			i+=1
		elif a[i] < b[j]:
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1
	return c

def msort(arr):
	N = len(arr)
	if len(arr) <= 1:
		return arr
	left = msort(arr[:N/2])
	right = msort(arr[N/2:])
	return merge(left, right)


def merge_count(a, b):
	m = len(a)
	n = len(b)
	i, j = 0, 0
	c = []
	count = 0
	for k in range(m+n):
		if i == m:
			c.append(b[j])
			j+=1
		elif j == n:
			c.append(a[i])
			i+=1
		elif a[i] < b[j]:
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			count += (m - i)
			j+=1
	return (c, count)

def inversionFast(arr):
	if len(arr) <= 1:
		return (arr, 0)
	else:
		N = len(arr)
		(left, lcount) = inversionFast(arr[:N/2])
		(right, rcount) = inversionFast(arr[N/2:])
		(merged_arr, splitcount) = merge_count(left, right)
		return (merged_arr, lcount + rcount + splitcount)


fname = "IntegerArray.txt"
f = open(fname, 'rb')
arr = []
for line in f:
	arr.append( int(line.strip()) )
#print arr
print inversionFast(arr)[1]
