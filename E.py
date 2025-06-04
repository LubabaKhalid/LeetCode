def count_ways(n, k, s):
    MOD = 998244353
    
    # Initialize the DP table
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case

    for i in range(1, n + 1):
        for j in range(0, k + 1):
            # Carry forward the previous counts
            dp[i][j] = dp[i - 1][j]
            if j > 0 and s[i - 1] == '0':
                # If we can perform an operation at this index
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    # The answer is the number of ways to perform exactly k operations on the full string
    return dp[n][k]

def main():
    
    
    t = int(input())
    
    index = 1
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        
        print(count_ways(n, k, s))
        
    


if __name__ == "__main__":
    main()
