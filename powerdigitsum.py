test = input()
for x in xrange(test):
	sum1 =0
	n  = input()
	ans = pow(2,n)
	leng = len(str(ans))
	ans = str(ans)
	for x in xrange(leng):
		sum1+=int(ans[x])
	#ans=sum((str(ans)))
	print sum1