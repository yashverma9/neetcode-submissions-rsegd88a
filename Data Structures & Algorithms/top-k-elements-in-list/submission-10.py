from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num in freqMap:
            buckets[freqMap[num]].append(num)
        
        res = []

        for i in range(len(buckets) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) == k:
                return res
