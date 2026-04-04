class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Optimal - greedy O(n), O(1)
        '''
        We take the problem from the end, and find the first index to left which can reach
        the goal. We shift goal to the index where we reached our last goal from
        This way in the end we make a virtual goal to goal path to the last index. If
        in the end index 0 is part of the goals, we return True. Else False
        '''
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
            
        if goal == 0:
            return True
        
        return False

        