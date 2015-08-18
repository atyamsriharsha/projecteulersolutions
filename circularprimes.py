import math
import os

list1=[0]*1000001
list1[1]=0

def memoize(f):
    """Cache the results of calls to f."""
    def func(*args):
        if args not in func.cache:
            func.cache[args] = f(*args)
        return func.cache[args]
    func.cache = {}
    return func

def is_prime(n):
	if (int(n) and 01)==0:
		return 0
	for x in xrange(2,int(n)):
		if x*x>int(n):
			break
		if int(n)%x==0:
			return 0
	return 1

for x in xrange(2,1000001):
	if is_prime(x):
		length = len(str(x))
		ref1=x
		ref2 =''
		flag1 =1
		for s in xrange(1,length+1):
			ref =str(ref1)[length-1]
			#print ref
			ref2 =''
			ref2 = ref2+ref
			#print ref2
			for j in xrange(1,length):
				p=str(ref1)[j-1]
				ref2 = ref2 +p
			ref1 = ref2
			if is_prime(ref2)==0:
				list1[x]=0
				flag1=0
				break
			#print ref2
		#list1[x] =x
		if flag1:
			list1[x]=x
	list1[x] = list1[x]+list1[x-1]

n1 = input()
print list1[n1]