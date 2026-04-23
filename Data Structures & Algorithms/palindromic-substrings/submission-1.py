class Solution:
    # Optimal - Exactly similar to longest palindrome substring (BRUTE SAME AS WELL)
    # Time - O(n^2)
    # Space - O(1)
    def countSubstrings(self, s: str) -> int:

        res = 0
        n = len(s)

        def checkP(l, r):
            nonlocal res
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
            
                l -= 1
                r += 1
    
        for mid in range(n):
            # odd
            l, r = mid, mid
            checkP(l,r)

            # even
            l, r = mid, mid+1
            checkP(l,r)
        
        return res