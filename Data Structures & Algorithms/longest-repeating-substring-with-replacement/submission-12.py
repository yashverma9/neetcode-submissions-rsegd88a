from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute

        'XYYX'
        'AAABABB'

        # Optimal
        n = len(s)
        longest = 0
        freq = defaultdict(int)

        l = 0

        for r in range(n):
            # Expand window
            freq[s[r]] += 1
            # while invalid
            while freq.values() and (sum(freq.values()) - max(freq.values()) > k):
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest


        # n = len(s)
        # longest = 0

        # for i in range(n):
        #     freq = defaultdict(int)
        #     curLen = 0
        #     for j in range(i, n):
        #         freq[s[j]] += 1
        #         total = sum(freq.values())
        #         maxFreq = max(freq.values())
        #         if total - maxFreq <= k:
        #             longest = max(longest, j - i + 1)
        #         else:
        #             break
        
        # return longest

