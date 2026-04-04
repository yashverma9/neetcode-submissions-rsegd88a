class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Brute
        '''
            num1 -> [1,2], num2 -> [3] 
            Just merge and find median 
        '''

        i = 0
        j = 0

        nums = []

        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        if i < len(nums1):
            nums = nums + nums1[i:]
        if j < len(nums2):
            nums = nums + nums2[j:]

        if len(nums)%2 == 0:
            return (nums[int(len(nums)/2) - 1] + nums[int(len(nums)/2)])/2
        else:
            return nums[len(nums)//2]
