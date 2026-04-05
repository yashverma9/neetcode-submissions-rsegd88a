class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)

        def backtrack(i, subset):
            if i == n:
                res.append(subset[:])
                return
            
            # When nums[i] is included
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # When nums[i] is not included
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res