fact =[1]*15
fact[0] = 1

for x in xrange(1,15):
	fact[x] = fact[x-1]*x

def result(s,n):
	if not s:
		return ''
	length = len(s)
	index =0
	while fact[length-1]<=n:
		n = n - fact[length-1]
		index+=1
	return s[index]+result(s[:index]+s[index+1:],n)



test = input()
while test:
	n = input()
	k = result(list("abcdefghijklm"),n-1)
	print k
	test = test-1