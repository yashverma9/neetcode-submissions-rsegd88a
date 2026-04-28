class Solution:
    # Optimal - DP - Top-down
    # Time - O(n^2) - As for upto n index we run a loop for i+1 to n+1. pracitically O(n^3) if slicing included
    # Space - O(n) - Memo and recursion stack
    '''
    Similar logic to brute, just store memo[i] to avoid recalculation of check(i) everytime
    '''
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
