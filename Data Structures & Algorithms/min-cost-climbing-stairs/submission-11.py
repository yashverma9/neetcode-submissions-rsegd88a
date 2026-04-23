class Solution:
    # Optimal | DP | Bottom-up | Space optimal
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        next1, next2 = 0, 0 # For n and n+1 step

        for i in range(n-1, -1, -1):
            temp = next1
            next1 = cost[i] + min(next1, next2)
            next2 = temp
        
        
        return min(next1, next2)