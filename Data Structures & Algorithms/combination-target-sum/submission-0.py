class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combination = [], []
        
        def calSum(i, sum):
            if sum == target:
                res.append(combination[:])
                return 
            
            if i == len(nums) or sum > target:
                return
            
            for ind in range(i, len(nums)):
                num = nums[ind]
                sum += num
                combination.append(num)
                calSum(ind, sum)
                sum -= num
                combination.pop()
        calSum(0, 0)
        return res
            