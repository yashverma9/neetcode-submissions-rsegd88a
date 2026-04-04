class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Optimal - sliding window

        if len(s) == 1:
            return 1

        l = 0
        r = 0
        freq = {}
        maxFreq = 0
        maxLen = 0
        
        while (r != len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1 - maxFreq) > k:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1

        return maxLen


