class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # BRUTE

        if len(s1) > len(s2):
            return False

        k = len(s1)
        
        windowFreq = defaultdict(int)
        s1Freq = defaultdict(int)
        
        for i in range(k):
            s1Freq[s1[i]] += 1
            windowFreq[s2[i]] += 1
        
        l = 0

        for r in range(k, len(s2)):

            if s1Freq == windowFreq:
                return True

            windowFreq[s2[r]] += 1
            windowFreq[s2[l]] -= 1
            if windowFreq[s2[l]] == 0:
                del windowFreq[s2[l]]
            l += 1
        
        return windowFreq == s1Freq