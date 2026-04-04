class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''' Optimal'''

        numSet = set(nums)
        possibleStarts = []

        for num in nums:
            if num-1 not in numSet:
                possibleStarts.append(num)
            
        maxCount = 0
        curCount = 1
        for start in possibleStarts:
            curNum = start
            while(curNum+1 in numSet):
                curCount += 1
                curNum += 1
            if curCount > maxCount:
                maxCount = curCount
            curCount = 1

        return maxCount
