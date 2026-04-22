class Solution:
    # Optimal - DP
    # Time - O(n) - as each subproblem (ways from step x) is solved only once
    # Space - O(n)
    def climbStairs(self, n: int) -> int:
        waysFromStep = [-1 for _ in range(n)]
        
        def climbTo(x):
            if x == n:
                return 1
            
            if x > n:
                return 0

            if waysFromStep[x] != -1:
                return waysFromStep[x]

            waysFromStep[x] = climbTo(x+1) + climbTo(x+2)
            return waysFromStep[x]
        
        return climbTo(0)
    