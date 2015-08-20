import math
test  = input()
while test:
    n = input()
    ans =(-1+math.sqrt(1+8*n))/2
    if ans==int(ans):
        print int(ans)
    else:
        print -1
    test = test-1