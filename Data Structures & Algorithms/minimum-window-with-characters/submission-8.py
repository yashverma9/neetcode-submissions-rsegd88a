class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Optimal

        '''
            
        '''
        if len(s) < len(t):
            return ""

        tCounts = {}
        window = {}

        for c in t:
            tCounts[c] = tCounts.get(c, 0) + 1
            window[c] = 0
        l = 0
        minRes, minLen = [-1, -1], float('inf')
        have, need = 0, len(tCounts) # Gives unique number of matches we want
        for r in range(len(s)):
            c = s[r]
            if c in tCounts:
                window[c] += 1
                if window[c] == tCounts[c]:
                    have += 1
                
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    minRes = [l, r]

                c = s[l]
                if c in window and window[c] - 1 < tCounts[c]:
                    have -= 1
                
                if c in window:
                    window[c] -= 1
                l += 1
        
        if minLen == float('inf'):
            return ""
        return s[minRes[0]: minRes[1] + 1] 
        
            
            


