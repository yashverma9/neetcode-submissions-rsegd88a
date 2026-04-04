# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS O(n), O(n) ( We can use other also, DFS)
        if not root:
            return None

        node = root

        q = deque()

        q.append(node)

        while q:
            node = q.popleft()
            temp = node.right
            node.right = node.left
            node.left = temp
            
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        return root


        