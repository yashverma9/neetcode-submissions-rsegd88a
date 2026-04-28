class Solution:
    # Optimal - dp - bottom-up
    # Time - O(n^2)
    # Space - O(n) for dp
    '''
    On similar lines, just opposite iteration. Important thing to note is we initialize counts with
    1 in dp for each index. This is because each index includes itself atleast. This is same as 
    initialzing count = 1 in top-down. Then we follow similar approach..

    Space optimized not possible again.
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)            