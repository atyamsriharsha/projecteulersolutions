import math

test = int(raw_input())
for x in xrange(test):
	n = int(raw_input())
	m = int(raw_input())
	f = math.factorial
	print ((f(m+n))/(f(m)*f(n)))%(1000000007)
