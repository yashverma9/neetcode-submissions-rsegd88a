class Solution:
    # Optimal - DP - Bottom-up
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = [-1 for _ in range(n+1)]

        ways[1] = 1
        ways[2] = 2

        for x in range(3, n+1):
            ways[x] = ways[x-1] + ways[x-2]
        
        return ways[n]