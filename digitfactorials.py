import math
import os
list1 = [0]*100001
#list1.append(0)
for x in xrange(19,100001):
	length = len(str(x))
	#print length
	sum1=0
	ref = x
	while ref:
		sum1 = sum1 + math.factorial(ref%10)
		ref = ref/10
		#print sum1
	if sum1%x==0:
		#print sum1
		list1[x]=x
	list1[x]=list1[x]+list1[x-1]
	#print length
n = input()
print list1[n]
