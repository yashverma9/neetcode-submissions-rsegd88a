class Solution:
    # Optimal - DP - Top-down
    # Time - O(n)
    # Space - O(n)
    '''
    We just use the recursive solution and store each jump(i) in the memo and reuse next time
    when needed.
    '''
    def rob(self, nums: List[int]) -> int:
        memo = {}

        n = len(nums)

        def jump(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            rob = nums[i] + jump(i+2)

            skip = jump(i+1)

            memo[i] = max(rob, skip)
            return memo[i]

        return jump(0)