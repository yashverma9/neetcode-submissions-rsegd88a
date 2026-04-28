class Solution:
    # DP - Bottom-up
    # O(n^2), O(n)
    # Reverse logic, iterative. dp[i] means can substring from to end be segmented
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[n] = True # As end of string means nothing to check and valid segment

        for i in range(n-1, -1, -1):
            # The second loop is the catch
            for j in range(i+1, n+1):
                if s[i:j] in wordSet and dp[j]: 
                    dp[i] = True
                    break
        
        return dp[0]

        