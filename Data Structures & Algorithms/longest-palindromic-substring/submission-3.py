# THIS IS A DIFFERENT KIND OF 2-POINTER QUESTION, NOT WORTH DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resLen = 0
        res = ()

        def checkP(start, end):
            nonlocal resLen, res
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 > resLen:
                    res = (start, end)
                    resLen = end - start + 1
                
                start -= 1
                end += 1
            

        
        for mid in range(n):
            # Odd len substr
            i, j = mid, mid
            checkP(i, j)

            # Even len substr
            i, j = mid, mid+1
            checkP(i, j)
        
        return s[res[0] : res[1]+1]