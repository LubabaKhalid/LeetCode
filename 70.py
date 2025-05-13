def climbStairs( n):
    memo={}
    def dp(k):
        if k==1:
            return 1
        elif k==2:
            return 2
        elif k==3:
            return 3
        if k not in memo:
            memo[k]=dp(k-1)+dp(k-2)
        return memo[k]
    return dp(n)