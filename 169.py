from collections import defaultdict
nums=[2,2,1,1,1,1,1,1,2,2]
n=set(nums)
d=defaultdict(int)
for i in nums:
    d[i]+=1
    
sorted_items=sorted(d.items(),key=lambda x:x[1])
print(sorted_items[-1][0])