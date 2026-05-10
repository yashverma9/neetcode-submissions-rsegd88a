from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)

        for str in strs:
            charFreq = [0 for _ in range(26)]
            for c in str:
                charFreq[ord(c) - ord('a')] += 1
            freqMap[tuple(charFreq)].append(str)
        
        res = []

        for group in freqMap.values():
            res.append(group)
        
        return res

        