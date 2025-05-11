n=list(map(int,input().split()))
t=int(input())
i=0
j=len(n)-1
while i<j:
    if n[i]+n[j]==t:
        print(i+1,j+1)
        break
    elif n[i]+n[j]>t:
        j-=1
    else:
        i+=1