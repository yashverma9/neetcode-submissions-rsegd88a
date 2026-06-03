class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # BETTER OPTIMAL
        # Easier better OPTIMAL using set instead of map
        seen = set()
        n = len(s)

        l = 0
        r = 0 

        longest = 0

        for r in range(n):

            # Window is invalid, basically duplicates after r is included in subs
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            w = r - l + 1 # new substring width
            longest = max(longest, w)
            seen.add(s[r])

        return longest