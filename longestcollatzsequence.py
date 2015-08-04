result = 0 
def calculate(n):
	if n==1:
		return 0
	if n&01:
		result = calculate(n/2) +1
	elif n&01:
	    result = calculate(3*n +1)+1
    #return result



	



T = int(raw_input())
for x in xrange(T):
	N = int(raw_input())
	calculate(N)
	print result
