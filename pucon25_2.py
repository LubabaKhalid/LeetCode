from collections import defaultdict
l=[1,2,3,2,2,2,3,1]
n=8
d=defaultdict(int)
for i in l:
    d[i]+=1
print(n-max(d.values()))
