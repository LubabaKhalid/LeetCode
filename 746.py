def minCostClimbingStairs(cost) -> int:
    p1=0
    p2=0
    for i in range(2,len(cost)+1):
        c=min(p1+cost[i-1],p2+cost[i-2])
        p2,p1=p1,c
    return p1
cost=list(map(int,input().split()))
print(minCostClimbingStairs(cost))