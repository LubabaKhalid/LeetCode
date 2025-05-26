import math
n=int(input())
if n<=0:
    print(False)
else:
    print((n&(n-1))==0)

