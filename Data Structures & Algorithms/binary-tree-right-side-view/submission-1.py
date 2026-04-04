# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Using BFS
        '''
        
        '''
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                # This is quicker way then storing entire level
                # We just append the last node of each level which is right most
                if i == size - 1:
                    res.append(node.val)
        
        return res



        