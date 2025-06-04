t=int(input())
for _ in range(t):
    n,m,a,b=map(int,input().split())
    turns = min(n - 1, m - 1) + max(a - 1, n - a) + max(b - 1, m - b)
    print(turns)