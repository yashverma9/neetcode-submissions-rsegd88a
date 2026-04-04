class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimal - sliding window
        '''
            We maintain a seen map for storing which index we saw a char at last
            We just keep moving a window (between l and r) based on the logic,
            if we see no repeat in char (using map) we keep moving r ahead
            Once we see a repeat then we move the l to a position ahead of one where
            we last saw that char. r keeps moving forward, this way we keep avoiding the repeats
        '''
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
