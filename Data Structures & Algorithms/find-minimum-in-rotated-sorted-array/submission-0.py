class Solution:
    def findMin(self, nums: List[int]) -> int:
        ### Reverse-rotate first, then binary search ###

        n = 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        
        return nums[0]