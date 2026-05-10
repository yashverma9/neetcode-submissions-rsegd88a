from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqList = [[] for _ in range(n+1)]
        freq = defaultdict(int)
        res = []

        for num in nums:   
            freq[num] += 1
        
        for num, count in freq.items():
            freqList[count].append(num)

        for i in range(n, -1, -1):
            if k == 0:
                return res
            if len(freqList[i]) > k:
                res.extend(freqList[:k])
                return res
            else:
                res.extend(freqList[i])
            k -= len(freqList[i])
        
        return res
            
            