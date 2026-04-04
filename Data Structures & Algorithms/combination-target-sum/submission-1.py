class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Optimal 
        # Time- O(n^(T/m)), we process upto n nodes per level and the max depth possible is T/m
        # Space - O(T/m) for call stack (T - target, m - min element in nums)
        # Space will be K*T/m if storage of output is considered where k is possible output combinations
        '''
        Logic is similar to subset, but here instead of 2 options we have many options to
        pick numbers to add to sum. We go down the tree same way adding numbers to combinations
        to reach the target and so on. At every node we can either add the same node again or
        just add the number ahead in the list. We discover each combination to reach target
        '''
        
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
            