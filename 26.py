class Solution:
    def removeDuplicates(self,nums) :
        c=1
        i=1
        while i <len(nums):
            if nums[i]!=nums[i-1]:  
                c=c+1
                i=i+1
            else:
                del nums[i]
                
        
        
        return c
    
s=Solution()
nums=[1,1,2,2,2,3,4,5,5,6]
print(s.removeDuplicates(nums))

print(nums)
        
