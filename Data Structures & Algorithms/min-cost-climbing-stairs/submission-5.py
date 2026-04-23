class Solution:
    # Optimal | Dp | Top-down
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        
        def climbTo(i):
            # Base case
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(climbTo(i+1), climbTo(i+2))
            return memo[i]

        return min(climbTo(0), climbTo(1))
            
