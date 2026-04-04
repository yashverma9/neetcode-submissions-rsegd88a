class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Brute force: Sorting, then if the next element is exactly 1 keep adding to current
        subsequence. If not, count the current length of subseq and store, Later make more and compare
        
        '''
        if len(nums) == 0:
            return 0

        nums.sort()

        maxCount = 0
        prevNum = nums[0]
        curSeq = [prevNum]
        curCount = 1

        for i in range(1, len(nums)):
            curNum = nums[i]
            if curNum == prevNum:
                continue
            if curNum - prevNum == 1:
                curSeq.append(curNum)
                curCount += 1
            else:
                if curCount > maxCount:
                    maxCount = curCount
                curSeq = [curNum]
                curCount = 1
            prevNum = curNum

        if curCount > maxCount:
            maxCount = curCount
            
        return maxCount

