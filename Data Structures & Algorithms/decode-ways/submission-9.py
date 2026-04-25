class Solution:
    # Optimal - DP - bottom-up, space optimal
    def numDecodings(self, s: str) -> int:
        n = len(s)

        one, two = 1, 0 # two is none as n+1 makes no sense in this problem initially

        # We will use a curr variable to maintain current which is upto dp[i+1] + dp[i+2]
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                curr = 0
            
            else:
                curr = one
                if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                    curr += two
                 
            two = one
            one = curr

        return one  
        