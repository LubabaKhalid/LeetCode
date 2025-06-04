def fun(l,n):
    
    for i in range(n-1):
        if l[i]==0 and l[i+1]==0:
            return "YES"
    return "NO"
            

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    if len(s)==1:
        print("YES")
    else:
        print(fun(l,n))
            