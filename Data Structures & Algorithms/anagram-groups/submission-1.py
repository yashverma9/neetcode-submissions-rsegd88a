class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Sorting (not best)##

        sortedDict = {}

        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in sortedDict:
                sortedDict[sortedString].append(s)
            else:
                sortedDict[sortedString] = [s]
        
        output = []

        for anagramGroup in sortedDict.values():
            output.append(anagramGroup)
        return output