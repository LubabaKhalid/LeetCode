class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:

            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
                i+=2
            else:
                i=i+1 
        i=0
        j=1
        while i<len(nums) and j<len(nums):
            if nums[i]!=0 and nums[j]!=0:
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j=j+1
            else:
                i+=1
                j+=1
        return nums