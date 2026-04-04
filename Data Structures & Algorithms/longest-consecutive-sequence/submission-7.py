class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        ### Brute force (O(n2))###
        # count = 0
        # maxCount = 0
        # store = set(nums)
        # for i in range(0, len(nums)):
        #     prev = nums[i]
        #     count = 0
        #     while prev in store:
        #         count += 1
        #         prev += 1
        #     maxCount = max(maxCount, count)
        # return maxCount
            
        ### Optimized above approach ( O(n))
        # Above we were considering every number is starting of a sequence
        # Can't we just check if for a starting n, does n-1 exist
        # If it exists that means n will be considered when n-1 is start, so
        # no need to consider n as start
        # we consider a start n only if n-1 is not available

        count = 0
        maxCount = 0
        store = set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in store:
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

            