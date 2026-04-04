class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [] , []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:]) # We append a copy, otherwise it will point to reference of sol
                return
            # When we don't add the ith index sol
            backtrack(i+1)

            # When we add the ith index to sol
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res