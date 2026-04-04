class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute - find every possible substring 
        '''
            At every substring start we find freq of the most frequent char till an index
            and replace with others with k, if all replacement are possible we compare the 
            length of the substring with max we have seen and update our max accordingly

            O(n2) , O(m) space where m is unique char in the string
        '''

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