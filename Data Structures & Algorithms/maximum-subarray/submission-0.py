class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute - try all subarrays
        
        maxSum = float('-inf')
        for i in range(len(nums)):
            curSum = nums[i]
            if curSum > maxSum:
                maxSum = curSum
            for j in range(i+1, len(nums)):
                curSum += nums[j]
                if curSum > maxSum:
                    maxSum = curSum
        
        return maxSum