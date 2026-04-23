class Solution:
    # Optimal | Dp | Top-down
    # Time - O(n) - as each step from 1 -> n will be calculated for once and stored
    # Space - O(n) - recursion stack + memo cache
    '''
    The intuition for top-down is basically using the same recursion approach and storing each
    step's cost into a memo (dict/hash-map). So, we end up calculating cost for each i step only
    once and use cache (memo) if required again.
    '''
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
            
