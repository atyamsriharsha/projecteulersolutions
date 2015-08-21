ans={3:lambda n:(n*(n+1))/2,5:lambda n:(n*(3*n-1))/2,6:lambda n:n*(2*n-1)}
N,a,b=map(long,raw_input().split())
gena,genb=ans[a],ans[b]
na,nb=1,1
while True:
	va=gena(na)
	vb=genb(nb)
	if va>=N or vb>=N:
		break
	if va==vb:
		print va
		na+=1
		nb+=1
	elif va>vb:
		nb+=1
	elif va<vb:
		na+=1