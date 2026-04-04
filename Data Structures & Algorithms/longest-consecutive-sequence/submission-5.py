class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute - using sort
        if len(nums) == 0:
            return 0
        sortedNums = sorted(nums)
        count = 1
        maxCount = count
        prevNum = sortedNums[0]
        for i in range(1, len(nums)):
            if sortedNums[i] == prevNum:
                continue
            elif sortedNums[i] - prevNum == 1:
                count +=1
            else:
                maxCount = max(maxCount, count)
                count = 1
            prevNum = sortedNums[i]
        maxCount = max(maxCount, count)
        return maxCount