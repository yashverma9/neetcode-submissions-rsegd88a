from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimal
        if len(s) < 2:
            return len(s)
        maxLen = 1
        freqMap = defaultdict(int)
        l = 0
        freqMap[s[l]] += 1
        for r in range(1, len(s)):
            freqMap[s[r]] += 1
            
            # while invalid
            while freqMap[s[r]] > 1:
                freqMap[s[l]] -= 1
                l += 1
        
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen