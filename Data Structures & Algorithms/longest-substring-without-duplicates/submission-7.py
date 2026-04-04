class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimal - sliding window
        if len(s) < 2:
            return len(s)
        maxLen = 0
        seen = {s[0]: 0}
        l = 0 
        r = 1
        while (l < len(s) and r < len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                currLen = r - l
                if currLen > maxLen:
                    maxLen = currLen
                l = seen[s[r]] + 1
                seen[s[r]] = r
            else:
                seen[s[r]] = r
            r += 1
        
        currLen = r - l 
        if maxLen < currLen:
            maxLen = currLen
        
        return maxLen
