from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        res = []
        i = 0
        for num, count in sorted(freq.items(), key = lambda x: x[1], reverse = True):
            if i == k:
                return res
            res.append(num)
            i += 1
    
        return res
            
            
            