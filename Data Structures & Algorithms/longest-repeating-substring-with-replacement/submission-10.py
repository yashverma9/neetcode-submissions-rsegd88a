class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Optimal - sliding window
        '''
          We keep increasing the window if the replacements (window_size - maxFreq) are valid (<k)
          Else till they are not valid we keep shrinking the window by moving left ahead till
          its valid again.
          We further optimize by storing a maxFreq variable instead of finding max freq every iteration
          This is an optimization bias as it doesnt effect our solution
          O(26*n) reduced to O(n) -> Understand why it doesnt effect next time
        '''
        l = 0
        r = 0
        freq = {}
        maxFreq = 0
        maxLen = 0
        
        while (r != len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]]) # Using this makes our algo O(n) from O(26*n)

            # Replace with maxFreq here instead of revaluating, as it never alters our answer
            while (r - l + 1 - max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen


