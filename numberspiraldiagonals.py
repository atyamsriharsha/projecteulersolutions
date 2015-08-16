def sum_of_nintegers(n):
	return (n*(n+1))/2

def sum_of_squares_of_nintegers(n):
	return (n*(n+1)*(2*n+1))/6


test = input()
while test:
	ans=0
	N = long(raw_input())
	n = (N+1)/2
	top_right = 4*sum_of_squares_of_nintegers(n) -4*sum_of_nintegers(n)+n
	#print top_right
	top_left = top_right - 2*sum_of_nintegers(n) + 2*n
	#print top_left
	bottom_left = top_left - 2*sum_of_nintegers(n) + 2*n
	#print bottom_left
	bottom_right = bottom_left -2*sum_of_nintegers(n)+2*n
	#print bottom_right
	ans = (top_right+top_left+bottom_left+bottom_right-3)%(10**9+7)
	print ans
	test = test-1