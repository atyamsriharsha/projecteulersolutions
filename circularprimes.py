import math
import os

list1=[0]*1000001
list1[1]=0
def is_prime(n):
	if (n and 01)==0:
		return 0
	for x in xrange(2,n):
		if x*x>n:
			break
		if n%x==0:
			return 0
	return 1

#print  is_prime(16)

for x in xrange(1,1000001):
	if is_prime(x):
		length = len(str(x))
		ref1=x
		ref2 =''
		for s in xrange(1,length+1):
			ref =str(x)[length-1]
			#ref2[s] = ref1[s-1]
			#str(ref1)[0]=ref
			ref2 = ref2+ref
			for j in xrange(1,length):
				ref2[x]=ref1[x-1]
				

			
