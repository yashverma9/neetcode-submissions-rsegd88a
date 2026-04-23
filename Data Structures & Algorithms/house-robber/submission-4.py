class Solution:
    # Optimal - DP - Top-down
    def rob(self, nums: List[int]) -> int:
        memo = {}

        n = len(nums)

        def jump(i):
            if i >= n:
                return 0
            
            if i+2 not in memo:
                memo[i+2] = jump(i+2)
            rob = nums[i] + memo[i+2]

            if i+1 not in memo:
                memo[i+1] = jump(i+1)
            skip = memo[i+1]

            return max(rob, skip)

        return jump(0)