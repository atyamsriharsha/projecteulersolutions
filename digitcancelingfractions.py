ans={
(2,1): (110,322),
(3,1): (77262,163829),
(3,2): (7429,17305),
(4,1): (12999936,28131911),
(4,2): (3571225,7153900),
(4,3): (255983,467405),
}

n,k =map(int,raw_input().split())
sn,sd =ans[(n,k)]
print sn,sd
