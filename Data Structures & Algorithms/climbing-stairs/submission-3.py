class Solution:
    # Optimal - DP - Top-down - memoization
    # Time - O(n) - as each subproblem (ways from step x) is solved only once
    # Space - O(n)
    '''
    We store a cache for the sub-problems already solved. In our case ways to reach top from
    each step is stored in the cache array. No. of ways from each step is sum of no. of ways
    from step+1 and step+2.
    '''
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
    