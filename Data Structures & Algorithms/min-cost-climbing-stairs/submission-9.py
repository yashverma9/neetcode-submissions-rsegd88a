class Solution:
    # Optimal | DP | Bottom-up (iteration)
    # Time - O(n) - Each dp[i] is calculated once upto n steps
    # Space - O(n) - for dp

    '''
    So, in earlier approaches using recursion we ask future and go till the end and return
    the solved steps. In bottom-up using iteration we start opposite from the future already
    computed and use it to find earier steps. 

    So, we know cost to reach last step or last step + 1 (if the jump is from n-1 step) is 0.
    We use that to find cost to reach top from n-1 step. And so on from n-2, n-3,....,2,1
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = [-1 for _ in range(n+2)]

        dp[n] = 0
        dp[n+1] = 0

        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0], dp[1])