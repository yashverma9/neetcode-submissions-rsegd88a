class Solution:
    # Brute - Recursion

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
            