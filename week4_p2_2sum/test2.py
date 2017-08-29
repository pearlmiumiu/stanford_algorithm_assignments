def getsum(a, b, c, d):
	sum=0
	low=max(a,c)
	high=min(b,d)
	for i in range(low,high+1):
		sum+=i
	return sum

def printnum(n, factors):
	divisible_one=False
	divisible_all=True
	for i in range(1,n+1):
		
		for j in factors:
			if i%j != 0:
				divisible_all = False

			else:
			    divisible_one=True
		#print i, j , divisible_all, divisible_one
		if divisible_all:
			print str(i) + "all"

		elif divisible_one:
			print str(i)+" one"
		else:
			print str(i)
def main():
	printnum(15, [2,3])

if __name__ == '__main__':
	main()




