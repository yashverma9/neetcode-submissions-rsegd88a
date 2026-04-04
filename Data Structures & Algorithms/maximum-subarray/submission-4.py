class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Optimal - O(n) - Kadane's algo, O(1) space        
        # maxSum = float('-inf')
        # cur = 0
        # for num in nums:
        #     cur += num
        #     if cur > maxSum:
        #         maxSum = cur
        
        #     if cur < 0:
        #         cur = 0

        # return maxSum

        ## OR ##
        # Both work same

        maxSum = float('-inf')
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            maxSum = max(cur, maxSum)
            

        return maxSum