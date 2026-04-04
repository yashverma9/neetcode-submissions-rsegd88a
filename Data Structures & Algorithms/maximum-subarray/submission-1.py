class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute - try all subarrays O(n2)
        
        maxSum = float('-inf')
        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum > maxSum:
                    maxSum = curSum
        
        return maxSum