from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute


        l = 0
        freqMap = defaultdict(int)
        freqMap[s[l]] = 1
        maxLen = 1
        
        for r in range(l+1, len(s)):
            freqMap[s[r]] += 1

            while (r - l + 1 - max(freqMap.values())) > k:
                freqMap[s[l]] -= 1
                l += 1
                
            maxLen = max(r - l + 1, maxLen)
        
        return maxLen