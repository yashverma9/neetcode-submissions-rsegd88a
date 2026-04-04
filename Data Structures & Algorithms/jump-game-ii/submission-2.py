class Solution:
    def jump(self, nums: List[int]) -> int:
        # Optimal greedy, O(n), O(1)
        '''
        As the end is always reachable, we can see this as a bfs problem. We can have
        ranges which define a level of the tree. At every level (starting from 0,0) we 
        see whats the next reachable range. That is r+1 (next to last end) to farthest 
        possible to reach. And we increment the level count as we find a new range (level)
        
        In the end we break once we have reached the len(nums) - 1 index in the range. We
        have got levels count which represens the jumps.
        '''
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