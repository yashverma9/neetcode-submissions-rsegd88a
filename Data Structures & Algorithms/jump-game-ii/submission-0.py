class Solution:
    def jump(self, nums: List[int]) -> int:
        # Brute

        jumps = float('inf')

        def dfs(i, noOfJumps):
            nonlocal jumps
            if i == len(nums) - 1:
                jumps = min(jumps, noOfJumps)
                return
            
            maxJump = min(nums[i], len(nums) - 1 - i)

            # We add a 1 to the end range to make i + maxJump inclusive
            for j in range(i + 1, i + maxJump + 1):
                dfs(j, noOfJumps + 1)

        dfs(0, 0)
        return jumps
