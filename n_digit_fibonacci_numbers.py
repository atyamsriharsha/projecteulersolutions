test = input()
ans =[]
while test:
	n = input()
	a=1
	b=1
	c=0
	index1=0
	while 1:
		c=a+b
		a=b
		b=c
		index1=index1+1
		#print n,b,len(str(b))
		if n<=len(str(b)):
			#print b
			break
	print index1+2
	test = test -1
	