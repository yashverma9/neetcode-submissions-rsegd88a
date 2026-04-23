class Solution:
    # Optimal | DP | Bottom-up | Space optimal
    # Time - O(n)
    # Space - O(1) # As only 2 variables

    '''
    This is exactly one lines of bottom-up but only using 2 variables. As, at every step i we only
    need the cost at i+1 and i+2, we store those 2 variables and keep updating them as we go down
    from step n to 0.
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        next1, next2 = 0, 0 # For n and n+1 step

        for i in range(n-1, -1, -1):
            temp = next1
            next1 = cost[i] + min(next1, next2)
            next2 = temp
        
        return min(next1, next2)