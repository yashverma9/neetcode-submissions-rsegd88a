from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Optimal - O(n), space - O(n)
        '''
            Using a deque - monotonically decreasing deque of indexes (whose values in nums)
            We start with l and r both at 0. Initially in the loop we make sure
            all smaller values than current value at r in the nums are popped out as they will not
            be the max value ever for windows to come. So we keep popping till a bigger value is in 
            the queue. Now we add our value at r to the queue. Either it will be smaller than
            an already bigger value in the queue, or it will become the biggest value at q[0] till now.

            Now, next thing we do is pop from left side the index which is smaller than l, which means
            l has shifted to next window.

            So, the q[0] always has the biggest value till now in the window, and we add that to the 
            result list everytime our window is valid (which is when r + 1 is equal or greater to k).
            r+1 = k is the first valid window from l = 0 to r+1. Post that we always have a new window 
            till r < len(nums). So we keep appending to output and increment l. We increment r every loop.
             
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
    
