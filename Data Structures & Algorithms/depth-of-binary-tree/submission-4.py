# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS

        if not root:
            return 0

        q = deque() 
        q.append(root)
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                cur = q.popleft()
                
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
            
        return depth



        