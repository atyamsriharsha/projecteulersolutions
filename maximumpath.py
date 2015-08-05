import math
import sys
go_left = 0
go_right = 0
test = input()
for x in xrange(test):
	ans = 0
	n = input()
	count1 = 0
	matrix = [[0 for x in xrange(n)]for x in xrange(n)]
	for r in xrange(1,n+1):
	    temp = list(raw_input().split())
	    length = len(temp)
	    for e in xrange(1,length+1):
	    	matrix[r-1][e-1] = int(temp[e-1])
	for a in xrange(1,n):
		for b in xrange(0,a+1):
			if b==0:
				go_left = 0
			else :
				go_left = matrix[a-1][b-1]
			if b==a:
				go_right =0
			else :
				go_right = matrix[a-1][b]
			matrix[a][b] = matrix[a][b] + max(go_left,go_right)
	for s in xrange(0,n):
		ans = max(ans,matrix[n-1][s])
	print ans