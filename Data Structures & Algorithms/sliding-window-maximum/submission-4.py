from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        l = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
            
        return res
            
            
