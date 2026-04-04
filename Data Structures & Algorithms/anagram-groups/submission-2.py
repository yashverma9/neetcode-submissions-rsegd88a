class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqDict = {}

        for s in strs:
            charFreq = [0]*26
            for t in s:
                charFreq[ord(t.lower())- ord('a')] += 1
            if tuple(charFreq) in freqDict:
                freqDict[tuple(charFreq)].append(s)
            else:
                freqDict[tuple(charFreq)] = [s]
        
        output = []

        for anagrams in freqDict.values():
            output.append(anagrams)

        return output