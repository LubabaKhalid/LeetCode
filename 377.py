nums=list(map(int,input().split()))
target=int(input())
dp=[0]*(target+1)
dp[0]=1
for i in range(1,target+1):
    for num in nums:
        if i>=num:
            dp[i]+=dp[i-num]
print(dp[target])