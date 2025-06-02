class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=len(nums1)
        y=len(nums2)
        i=0
        l=[]
        while i<x:
            ind=nums2.index(nums1[i])+1
            while ind<y:
                if nums2[ind]>nums1[i]:
                    l.append(nums2[ind])
                    break
                ind+=1
            else:
                l.append(-1)
            i+=1
        return l
