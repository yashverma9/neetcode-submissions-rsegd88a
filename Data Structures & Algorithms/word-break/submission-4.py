class Solution:
    # Optimal - DP - Top-down
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        n = len(s)
        memo = {} # each memo[i] stores if check(i) was possible

        def check(i):
            if i == n:
                return True
            
            if i in memo:
                return memo[i]

            for j in range(i+1, n+1):
                if s[i:j] in wordSet and check(j):
                    memo[i] = True
                    return True
                
            memo[i] = False
            return False
        
        return check(0)
