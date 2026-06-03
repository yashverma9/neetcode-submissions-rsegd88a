from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute

        'XYYX'
        'AAABABB'

        n = len(s)
        longest = 0

        for i in range(n):
            freq = defaultdict(int)
            curLen = 0
            for j in range(i, n):
                freq[s[j]] += 1
                total = sum(freq.values())
                maxFreq = max(freq.values())
                if total - maxFreq <= k:
                    longest = max(longest, j - i + 1)
                else:
                    break
        
        return longest