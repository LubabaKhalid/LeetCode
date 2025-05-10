nums=[10,20,30,40,50,60,70,80,90]
nums.sort()
target=1
n=len(nums)
t=0
l=[]
for i in range(n):
    left=i+1
    right=n-1
    while left<right:
        t=nums[i]+nums[left]+nums[right]
        l.append(t)
        if t==target:
            print(t)
            break
        elif t<target:
            left+=1
        else:
            right-=1
l.sort()
l=list(set(l))
m=l[0]
print(l)
for i in range(1,len(l)):
    if abs(target-m)>abs(target-l[i]):
        m=l[i]
print(m)
