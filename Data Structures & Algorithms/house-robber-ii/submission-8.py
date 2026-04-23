class Solution:
    # Dp - top-down
    # Time - O(n), space - O(n)
    '''
    This time we smartly broke the problem into 2 ranges, one 0 -> n-1 and other 1 -> n. So, 
    basically we maintain different memo as well due to different problems. Using same
    memo we would lose values for same ith in case of including last or not. 

    We also need to handle an edge case when only 1 house is there.
    '''

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def jump(i, last, memo):
            if i >= last:
                return 0
            
            if i in memo:
                return memo[i]

            rob = nums[i] + jump(i+2, last, memo)
            skip = jump(i+1, last, memo)

            memo[i] = max(rob, skip)
            
            return memo[i]
        
        # Edge case - v. imp
        if n == 1:
            return nums[0]
        return max(jump(0, n-1, {}), jump(1, n, {}))
            