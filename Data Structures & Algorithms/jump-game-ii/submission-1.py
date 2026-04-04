class Solution:
    def jump(self, nums: List[int]) -> int:
        # Optimal greedy, O(n), O(1)
        levels = 0 

        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1): # To make r inclusive
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            levels += 1
        
        return levels