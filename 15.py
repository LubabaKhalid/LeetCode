nums=[-1,0,1,2,-1,-4]
nums.sort()
n=len(nums)
l=[]
for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        t=nums[i]+nums[left]+nums[right]
        if t==0:
            l.append([nums[i],nums[left],nums[right]])
            while left<right and nums[left]==nums[left+1]:
                 left+=1
            while left<right and nums[right]==nums[right -1]:
                right -=1
            left+=1
            right-=1
        elif t<0:
            left+=1
        else:
            right-=1
print(l)
    