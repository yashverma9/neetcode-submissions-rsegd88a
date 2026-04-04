class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute

        maxLen = 0  
    
        for i in range(len(s)):
            cur = s[i]
            curLen = 1
            seen = {cur}
            for j in range(i+1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    curLen += 1
                else:
                    if curLen > maxLen:
                        maxLen = curLen
                    break
            if curLen > maxLen:
                maxLen = curLen
        return maxLen




