class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute - find every possible substring

        maxLen = 0
        for i in range(len(s)):
            count = {}
            maxFreq = 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j],0) + 1
                maxFreq = max(maxFreq, count[s[j]])
                if (j - i + 1 - maxFreq) <= k:
                    maxLen = max(j - i + 1, maxLen)
        
        return maxLen