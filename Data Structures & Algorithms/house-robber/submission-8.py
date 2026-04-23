class Solution:
    # Optimal - DP - Bottom-up
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] stores max money you can rob from starting from house i
        dp = [0 for _ in range(n+2)]
        # dp[n] = 0 # End of house
        # dp[n+1] = 0 # End of house + 1 to manage i+2 jump safely
        
        for i in range(n-1, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]