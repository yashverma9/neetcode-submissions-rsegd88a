class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## brute ##
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False        


        ## optimal (using hashset) ##

        unique = set()
        for num in nums:
            unique.add(num)
        
        if len(unique) == len(nums):
            return False
        return True

