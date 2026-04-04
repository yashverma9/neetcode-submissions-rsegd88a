class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Optimal - O(n)
        
        # maxSum = float('-inf')
        # cur = 0
        # for num in nums:
        #     cur += num
        #     if cur > maxSum:
        #         maxSum = cur
        
        #     if cur < 0:
        #         cur = 0

        # return maxSum

        maxSum = float('-inf')
        cur = 0
        for num in nums:
            cur = max(num, num + cur)
            maxSum = max(cur, maxSum)
            

        return maxSum