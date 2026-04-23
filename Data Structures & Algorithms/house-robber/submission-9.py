class Solution:
    # Optimal - DP - Bottom-up
    # Time - O(n)
    # Space - O(n)
    '''
    On similar lines as any bottom up, we reverse the logic and use iteration. As we know
    the last houses are calculated first at the end of recursion, we start iteration from end
    to the first house. 

    We create a dp list of size n+2 for safely handling dp[n] and dp[n+1] for the 2nd last house jumps

    Now the dp[i] stores max at any house onwards. So, thats assigned with max (rob, skip)
    In the end we return dp[0] to start from beginning.
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] stores max money you can rob from starting from house i
        dp = [0 for _ in range(n+2)]
        # dp[n] = 0 # End of house
        # dp[n+1] = 0 # End of house + 1 to manage i+2 jump safely
        
        for i in range(n-1, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]