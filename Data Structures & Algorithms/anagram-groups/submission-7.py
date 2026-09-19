from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute
        
        groups = defaultdict(list)
        
        for string in strs:
            groups["".join(sorted(string))].append(string)
        
        res = []

        for key in groups.keys():
            res.append(groups[key])
        
        return res