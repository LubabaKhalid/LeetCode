from collections import defaultdict
l=defaultdict(int)
d=[]
n=int(input())
c=0
for _ in range(n):
    a=list(map(int,input().split()))
    d.append(a)
for i,j in d:
    key=tuple(sorted((i,j)))
    c+=l[key]
    l[key]+=1
print(c)
    