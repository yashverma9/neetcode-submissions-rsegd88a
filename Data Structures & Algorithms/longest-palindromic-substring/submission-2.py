class Solution:
    # BRUTE
    def longestPalindrome(self, s: str) -> str:
        resMaxLen = 0
        res = None
        n = len(s)

        def isP(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        for i in range(n):
            for j in range(i, n):
                strLen = j - i + 1
                if strLen > resMaxLen and isP(i, j):
                    res = (i, j)
                    resMaxLen = strLen
        
        return s[res[0]: res[1]+1]