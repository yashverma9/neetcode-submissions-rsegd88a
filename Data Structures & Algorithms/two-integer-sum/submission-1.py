class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## Brute ##
        # for i in range(len(nums)):
        #     num1 = nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == target - num1:
        #             return [i, j]

        ## Optimal ##

        numbersVisited = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in numbersVisited:
                return [numbersVisited[target - nums[i]], i]
            numbersVisited[nums[i]] = i
        