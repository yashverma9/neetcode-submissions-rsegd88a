class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
        
        for char in sDict.keys():
            if char in sDict and char in tDict:
                if sDict[char] != tDict[char]:
                    return False
            else:
                return False

        return True