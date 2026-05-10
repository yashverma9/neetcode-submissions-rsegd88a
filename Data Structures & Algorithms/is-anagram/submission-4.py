from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freqMap = defaultdict(int)

        n = len(s)

        for i in range(n):
            freqMap[s[i]] += 1
            freqMap[t[i]] -= 1
        
        for char in freqMap.keys():
            if freqMap[char] != 0:
                return False

        
        return True

        