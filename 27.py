class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]==val and nums[j]==val:
                j=j-1
            elif nums[j]!=val and nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j-=1
            elif nums[j]!=val and nums[i]!=val:
                i+=1
            else:
                i+=1
                j-=1
        return len(nums)-nums.count(val)
