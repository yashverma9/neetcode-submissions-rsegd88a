class Solution:
    # Optimal - DP - bottom-up
    # Time - O(n), space - O(n)
    '''
    Very similar logic as any other bottom up, it depends on next 2 states conditionally.
    Looks tricky at first. But, use same logic. nth index means valid way, hence thats 1 way.

    And then we reverse iterate to 0th index. Just checking if the index digit is 0, then
    no. of ways at dp[i] is 0. And otherwise its dp[i+1] and additional + dp[i+2] if i+2 is 
    possible based on digit being between 10 and 26.
    '''
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1 for _ in range(n+1)] # dp[i] is the no. of ways to decode from ith index
        dp[n] = 1 # end is 1 valid way

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
        
        return dp[0]



