a=int(input())
coins=list(map(int,input().split()))
dp=[0]*(a+1)
dp[0]=1
for coin in coins:
    for i in range(coin,a+1):
        dp[i]+=dp[i-coin]
print(dp[a])