class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #BRUTE
        i = 0
        j = 0
        combined = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
            
        if i < len(nums1):
            combined += nums1[i:]
        
        if j < len(nums2):
            combined += nums2[j:]
        
        length = len(combined)
        if length % 2 == 0:
            return (combined[length//2] + combined[(length//2)-1])/2
        else:
            return combined[length//2]