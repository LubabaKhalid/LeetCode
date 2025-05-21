from itertools import combinations
n=list(map(int,input().split()))
m=list(map(int,input().split()))
com=list(combinations(n,3))

count=0
for c in com:
    
    x=m.index(c[0])
    y=m.index(c[1])
    z=m.index(c[2])
    if x<y and y<z:
        count+=1
print(count)
    
