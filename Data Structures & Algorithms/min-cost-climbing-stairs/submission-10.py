class Solution:
    # Optimal | DP | Bottom-up | Space optimal
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, second = 0, 0 # For n and n+1 step

        for i in range(n-1, -1, -1):
            one, second = cost[i] + min(one, second), one
        
        return min(one, second)