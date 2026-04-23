# THIS IS A DIFFERENT KIND OF 2-POINTER QUESTION, NOT WORTH DP
class Solution:
    # Optimal - 2pointer
    # Time - O(n^2)
    # Space - O(1) extra space
    '''
    This is a tricky 2 pointer problem. We think about palindromes having a middle index.
    In case of odd sized strings, the middle is an index and left and right of it keep matching.
    For even, the middle is between left and right index in the middle of the string. And they
    keep matching till the ends. 

    So, we consider all possible middle indexes for an input string and start expanding in both
    directions to make a longer substring. Each step we check if the new left and right are equal
    and within string bounds. If they are bigger than existing stored results, we update.
    '''
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