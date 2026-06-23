from collections import defaultdict
class Solution:
    # Find substringds of t in s
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        tFreq = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            tFreq[c] += 1
        
        have, need = 0, len(tFreq)
        
        minRes, minLen = [-1,-1], float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minRes = [l, r]    
                if s[l] in tFreq and window[s[l]] == tFreq[s[l]]:
                    have -= 1
      
                window[s[l]] -= 1
                if not window[s[l]]:
                    del window[s[l]]
                    
                l += 1

        if minLen == float('inf'):
            return ''
        
        return s[minRes[0]: minRes[1] + 1]

