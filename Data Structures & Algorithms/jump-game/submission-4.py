class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Brute - recursion, O(2^n), o(n) for call stack 
        '''
        We expore all possible index from an index post jump, if we reach end we return True
        '''
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