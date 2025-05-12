nums=list(map(int,input().split()))
m1=float('inf')
m2=float('inf')
for n in nums:
    if n<=m1:
        m1=n
    elif n<=m2:
        m2=n
    else:
        print(True)
        break
else:
    print(False)
    