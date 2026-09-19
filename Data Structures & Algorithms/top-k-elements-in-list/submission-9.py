from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        freqList = []
        for num in freqMap.keys():
            freqList.append((num, freqMap[num]))

        freqList.sort(reverse = True, key = lambda tup: tup[1])

        res = []
        for i in range(k):
            res.append(freqList[i][0])
        return res