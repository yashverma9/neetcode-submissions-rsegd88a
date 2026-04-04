class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Optimal - sliding window
        '''
          We keep increasing the window if the replacements (window_size - maxFreq) are valid (<k)
          Else till they are not valid we keep shrinking the window by moving left ahead till
          its valid again    
    
        '''
        l = 0
        r = 0
        freq = {}
        maxFreq = 0
        maxLen = 0
        
        while (r != len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1 - max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen


