from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = defaultdict(int)
        subFreq = defaultdict(int)
        
        n = len(s1)

        for c in s1:
            s1Freq[c] += 1
        
        l = 0

        for r in range(len(s2)):
            subFreq[s2[r]] += 1
            
            while r - l + 1 > n:
                subFreq[s2[l]] -= 1
                if subFreq[s2[l]] == 0:
                    del subFreq[s2[l]]
                l += 1
                
            if s1Freq == subFreq:
                return True
            
        return False
            