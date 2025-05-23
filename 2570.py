class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        j=0
        i=0
        nums3=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i][0]==nums2[j][0]:
                nums3.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0]<nums2[j][0]:
                nums3.append([nums1[i][0],nums1[i][1]])
                i+=1
            else:
                nums3.append([nums2[j][0],nums2[j][1]])
                j+=1
        while i<len(nums1):
            nums3.append([nums1[i][0],nums1[i][1]])
            i+=1
        while j<len(nums2):
            nums3.append([nums2[j][0],nums2[j][1]])
            j+=1
        return nums3

