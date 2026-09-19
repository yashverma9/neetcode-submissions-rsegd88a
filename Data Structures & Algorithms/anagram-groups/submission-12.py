from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute
        
        groups = defaultdict(list)
        
        for string in strs:
            counts = [0 for _ in range(26)]
            for c in string:
                counts[ord(c) - ord('a')] += 1
            groups[tuple(counts)].append(string)
        
        res = []

        for group in groups.keys():
            res.append(groups[group])
            
        return res
