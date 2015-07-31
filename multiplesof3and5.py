def func(n):
	return n*(n+1)/2 ;
test = int(raw_input())
for x in xrange(test):
	n = int(raw_input())
	n-=1
	print func(n/3)*3 + func(n/5)*5 - func(n/15)*15