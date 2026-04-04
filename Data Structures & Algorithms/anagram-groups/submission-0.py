class Solution:

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        countDict = {}

        for i in range(len(s)):
            if s[i] in countDict:
                countDict[s[i]] += 1
            else:
                countDict[s[i]] = 1
            if t[i] in countDict:
                countDict[t[i]] -= 1
            else:
                countDict[t[i]] = -1
        
        for count in countDict.values():
            if count != 0:
                return False

        return True


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        seen = set()
        for i in range(len(strs)):
            if i not in seen:
                s = strs[i]
                anagrams = [s]
                seen.add(i)
                for j in range(i+1, len(strs)):
                    t = strs[j]
                    if self.isAnagram(s,t) and j not in seen:
                        anagrams.append(t)
                        seen.add(j)
                output.append(anagrams)
        
        return output

            