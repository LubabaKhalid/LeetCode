def is_valid(m,l,maxOp):
    op=0
    for n in l:
        op+=(n-1)//m
    return op<=maxOp

maxOp=int(input())
l=list(map(int,input().split()))
left=1
right=max(l)
while left<right:
    mid=(left+right)//2
    if is_valid(mid,l,maxOp):
        right=mid
    else:
        left=mid+1
print(left)