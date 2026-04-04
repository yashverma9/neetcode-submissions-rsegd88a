class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        ### Brute force ###
        count = 0
        maxCount = 0
        store = set(nums)
        for i in range(0, len(nums)):
            prev = nums[i]
            count = 0
            while prev in store:
                count += 1
                prev += 1
            maxCount = max(maxCount, count)
        return maxCount
            
        
        #### using sort (O(nlog(n))) ####
        
        # sortedNums = sorted(nums)
        # count = 1
        # maxCount = count
        # prevNum = sortedNums[0]
        # for i in range(1, len(nums)):
        #     if sortedNums[i] == prevNum:
        #         continue
        #     elif sortedNums[i] - prevNum == 1:
        #         count +=1
        #     else:
        #         maxCount = max(maxCount, count)
        #         count = 1
        #     prevNum = sortedNums[i]
        # maxCount = max(maxCount, count)
        # return maxCount

            