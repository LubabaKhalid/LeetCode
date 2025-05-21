banned=list(map(int,input().split()))
n=int(input())
maxSum=int(input())
c=0
count=0
for i in range(1,n+1):
    if i in banned:
        continue
    if count+i>maxSum:
        break
    c=c+1
    count+=i
print(c)

        