import math
import sys
import os
max1 = 100004
def sum_of_proper_divisors(n):
	sum1 = 0
	for x in xrange(1,max1):
		if x*x>n:
			break
		if n%x==0:
			sum1 = sum1 + x + n//x
		if x*x==n:
			sum1=sum1-x
	return sum1-n

is_amicable = [-1]*max1
is_amicable[0] = 0

for x in xrange(1,max1):
	if is_amicable[x]!=-1:
		continue
	p =sum_of_proper_divisors(x)
	#print p
	if x!=p and sum_of_proper_divisors(p)==x:
		is_amicable[x] = 1
		is_amicable[p] = 1
	else:
		is_amicable[x] = 0

#print 'hello3'

for x in xrange(1,max1):
	if is_amicable[x]==1:
		is_amicable[x] = is_amicable[x-1] + x
	else:
		is_amicable[x] = is_amicable[x-1]
#print 'hello4'

	 	

test = input()
while test:
	n = input()
	#print 'chandrakala'
	print is_amicable[n]
	test = test-1