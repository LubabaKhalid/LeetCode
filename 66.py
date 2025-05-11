digits=list(map(int,input().split()))
n=len(digits)
x=digits[n-1]+1
if x>9:
    digits[n-1]=x%10
    x=x//10
    
    
    for i in range(n-2,-1,-1):
        x=digits[i]+x
        if x>9:
            digits[i]=x%10
            x=x//10
        else:
            digits[i]=x
            x=0
            break
    if x!=0:
        digits.insert(0,x)
else:
    digits[n-1]=x
print(digits)
    