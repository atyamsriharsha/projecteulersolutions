def number_base(n,k):
	s=''
	while n:
		s = s+str(n%k)
		#print s
		n=n/k
	return s[::-1]

def is_palindrome(s):
	length = len(str(s))
	for x in xrange(0,length):
		if str(s)[x]!=str(s)[length-1-x]:
			return 0
	return 1
sum1 =0
n,k=map(int,raw_input().split())
for x in xrange(1,n+1):
	ans1 = is_palindrome(x)
	ans2 = is_palindrome(number_base(x,k))
	if ans1==1 and ans2==1:
		sum1 = sum1+x
print sum1



