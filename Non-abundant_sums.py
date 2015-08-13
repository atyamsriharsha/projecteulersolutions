max1 = 28123+7
list1=[0]*max1
list2 =[]

def sum_of_proper_divisors(n):
	sum1 =1
	for x in xrange(2,n+1):
		if x*x==n:
	#		print sum1
			sum1 = sum1 +x
			break
		elif x*x>n:
			break
		elif n%x==0:
	#		print x,n/x
			sum1 = sum1+x+n/x
	return sum1

#print sum_of_proper_divisors(6)

for y in xrange(1,max1+1):
	if sum_of_proper_divisors(y)>y:
		list2.append(y)
		list1[y]=1

#print "idhar bee aaya"

print len(list2)
#print list1[6]

test = input()
while test:
	n = input()
	if n>max1:
		print "YES\n"
	else:
		rem =0
		for z in xrange(1,len(list2)):
			if list2[z]>n:
				break
			print list2[z]
			print list1[z],list1[n-list2[z]]
			if list1[n-list2[z]]!=0:
				rem =1
				break
		if rem:
			print "YES\n"
		else:
			print "NO\n"
	test = test-1
#'''