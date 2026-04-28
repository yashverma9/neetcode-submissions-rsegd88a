class Solution:
    # Optimal - DP - top-down
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {} # memo[i] stores max count i onwards

        def findNext(i):
            if i in memo:
                return memo[i]

            count = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    count = max(count, 1 + findNext(j))
            
            memo[i] = count
            return count
        
        res = 0
        for i in range(n):
            res = max(res, findNext(i))
        
        return res