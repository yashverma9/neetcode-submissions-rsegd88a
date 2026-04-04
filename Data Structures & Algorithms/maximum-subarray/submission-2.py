class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Optimal
        
        maxSum = float('-inf')
        cur = 0
        for num in nums:
            cur += num
            if cur > maxSum:
                maxSum = cur
        
            if cur < 0:
                cur = 0

        return maxSum