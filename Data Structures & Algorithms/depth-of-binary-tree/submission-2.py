# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive dfs - We cound no. of node on each side of node and recursivelly add.
        # Base case is 0 for None node, and otherwise 1 + max(left, right)
         
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0
            
            return 1 + max(dfs(node.left), dfs(node.right))

        depth = dfs(root)

        return depth

