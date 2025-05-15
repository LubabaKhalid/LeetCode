l=list(map(int,input().split()))
k=int(input())
r=0
for i in range(len(l)):
    r=r*10+l[i]
r=r+k
s=[]
while r>0:
    d=r%10
    r=r//10
    print(s)
    s.insert(0,d)
print(s)