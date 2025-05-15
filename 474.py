s=list(map(str,input().split()))
n=int(input())
m=int(input())
dp=[[0]*(n+1) for i in range(m+1)]
for x in s:
    zero=x.count('0')
    one=x.count('1')
    for i in range(m,zero-1,-1):
        for j in range(n,one-1,-1):
            dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)
            print(i,j,dp[i][j])
print(dp[m][n])
        