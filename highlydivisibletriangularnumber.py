def triangular(n):
	return n*(n+1)/2

ans =[
(1,1),
(2,2),
(3,4),
(7,6),
(8,9),
(15,16),
(24,18),
(32,20),
(35,24),
(63,36),
(80,40),
(104,48),
(224,90),
(384,112),
(560,128),
(935,144),
(1224,162),
(1664,168),
(1728,192),
(2015,240),
(2079,320),
(5984,480),
(12375,576),
(14399,648),
(21735,768),
(41040,1024)]

test = int(raw_input())
for x in xrange(test):
	N = int(raw_input())
	for (a,b) in ans:
		if b>N:
			print triangular(a)
			break ;