from collections import defaultdict
nums1=list(map(int,input().split()))  
nums2=list(map(int,input().split()))  
nums3=list(map(int,input().split()))  
nums4=list(map(int,input().split()))  
n=len(nums1)
nums1.sort()
nums2.sort()
nums3.sort()
nums4.sort()
count=0
s=defaultdict(int)
for a in nums1:
    for b in nums2:
        s[a+b]+=1

for c in range(n):
    for d in range(n):
        
        
        target=-(nums3[c]+nums4[d])
        print(target)
        if target in s.keys():
            count=count+s[target]
print(count)