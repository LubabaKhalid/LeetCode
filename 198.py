class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        p2=nums[0]
        p1=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            c=max(p2+nums[i],p1)
            
            p2=p1
            
            p1=c
        return p1