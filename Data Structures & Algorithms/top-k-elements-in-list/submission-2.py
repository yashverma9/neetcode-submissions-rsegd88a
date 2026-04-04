class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Optimal ##
        ''' Using bucket sort -
        We make an array of the length of nums + 1 (to avoid 0 index)
        We store array of nums which are of same freq in the same array at that freq index in the bucket
        Later return the most frequent one from the end of bucket array
        '''

        freqDict = {}

        for num in nums:
            freqDict[num] = 1 + freqDict.get(num, 0)

        freqBucket = [[] for _ in range(len(nums)+1)]

        for num, freq in freqDict.items():
            freqBucket[freq].append(num)

        output = []
        for i in range(len(freqBucket)-1, -1, -1):
            if len(output) < k:
                output += freqBucket[i]

        return output[:k+1]