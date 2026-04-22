class Solution:
    def climbStairs(self, n: int) -> int:
        waysFromStep = [-1 for _ in range(n+2)]
        
        def climbTo(x):
            if x == n:
                return 1
            
            if x > n:
                return 0
            
            climb1 = waysFromStep[x+1] if waysFromStep[x+1] != -1 else climbTo(x+1)
            climb2 = waysFromStep[x+2] if waysFromStep[x+2] != -1 else climbTo(x+2)
            ways = climb1 + climb2
            
            waysFromStep[x] = ways
            return ways
        
        return climbTo(0)
    