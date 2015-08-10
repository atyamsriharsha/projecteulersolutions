n = input()
list1 = ['']*n
list2 = ['']*n
for x in xrange(0,n):
	str1 = raw_input()
	list1[x] = str1
list1.sort()
for x in xrange(0,n):
	list2[x] = sum(bytearray(list1[x]))
	#print list2[x]
	leng = len(list1[x])
	#print leng
	list2[x] = list2[x] - leng*64
	#print list2[x]
	list2[x] = (x+1)*list2[x]
	#print list2[x]

q = input()
for x in xrange(1,q+1):
	str1 = raw_input()
	for y in xrange(0,n):
		if str1==list1[y]:
			print list2[y]

	