class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countDict = {}

        for char in s:
            if char in countDict:
                countDict[char] += 1
            else:
                countDict[char] = 1
        
        for char in t:
            if char in countDict:
                countDict[char] -= 1
            else:
                return False
        
        for count in countDict.values():
            if count != 0:
                return False
        
        return True