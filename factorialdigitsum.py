import math
test = input()
for x in xrange(test):
	n = input()
	sum1 = 0
	n1 = math.factorial(n)
	length = len(str(n1))
	n1 = str(n1)
	for y in xrange(0,length):
	    sum1+=int(n1[y]) 
	print sum1