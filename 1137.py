def tribonacci(n):
        memo={}
        def tri(k):
            if k==0:
                return 0
            elif k==1:
                return 1
            elif k==2:
                return 1
            if k not in memo:
                memo[k]=tri(k-1)+tri(k-2)+tri(k-3)

            return memo[k]
        print(tri(n))
        
x=int(input())
tribonacci(x)