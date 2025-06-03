import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operation=0
        while nums[0]<k:
            num1=heapq.heappop(nums)
            num2=heapq.heappop(nums)
            n=2*min(num1,num2)+max(num1,num2)
            heapq.heappush(nums,n)
            operation+=1
        return operation
            
            