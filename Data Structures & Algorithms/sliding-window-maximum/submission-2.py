from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Optimal - O(n), space - O(n)
        '''
            Using a deque - monotonically decreasing deque
             
        '''
        # The first element of q will always have the highest value of the l to r window
        q = deque() # Store index of nums
        l = r = 0
        res = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                l += 1
                res.append(nums[q[0]])
            
            r += 1
        
        return res
    
