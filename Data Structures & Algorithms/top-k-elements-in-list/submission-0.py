class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Brute force ##
        freqDict = {}

        for num in nums:
            if num in freqDict:
                freqDict[num] += 1
            else:
                freqDict[num] = 1

        sortedFreq = sorted(freqDict.items(), key = lambda item: item[1], reverse=True)

        output = []
        for i in range(k):
            output.append(sortedFreq[i][0])

        return output

        