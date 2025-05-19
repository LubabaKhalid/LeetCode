from itertools import permutations
def perm(n,k):
    s=''
    for i in range(1,n+1):
        s=s+str(i)
    l=list(permutations(s))
    return ''.join(l[k-1])
        
n=int(input())
k=int(input())
print(perm(n,k))