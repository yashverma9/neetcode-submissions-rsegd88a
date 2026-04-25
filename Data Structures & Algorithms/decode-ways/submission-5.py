class Solution:
    # Optimal - DP - Top-down
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def decode(i):
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            # 1 digit at a time
            ways = decode(i+1)

            # 2 digit combined at a time
            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += decode(i+2)
            
            memo[i] = ways
            return memo[i]

        return decode(0)        