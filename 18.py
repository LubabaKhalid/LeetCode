nums=[1,0,-1,0,-2,2]
target=0
n=len(nums)
        
l=[]
nums.sort()
for i in range(n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        left=j+1
        right=n-1
        while left<right:
            t=nums[i]+nums[j]+nums[left]+nums[right]
            if t==target:
                l.append([nums[i],nums[j],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1] :
                    left+=1
                while left<right and nums[right]==nums[right-1] :
                    right-=1
                            
                left+=1
                right-=1
            elif t>target:
                right-=1
            else:
                left+=1

print(l)

