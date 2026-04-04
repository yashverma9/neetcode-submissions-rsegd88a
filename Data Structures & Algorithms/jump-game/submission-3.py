class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Brute - recursion
        goalReach = False

        def dfs(i):
            nonlocal goalReach
            if i == len(nums) - 1:
                goalReach = True
                return

            maxJump = min(nums[i], len(nums) - 1 - i)

            for j in range(i + 1, i + maxJump + 1):
                dfs(j)
        
        dfs(0)

        return goalReach