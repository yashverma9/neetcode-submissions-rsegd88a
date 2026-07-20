# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxD = 0

        def dfs(node, depth):
            nonlocal maxD

            if not node:
                return 0
            
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            maxD = max(maxD, left + right)

            return 1 + max(left, right)
        
        dfs(root, 0)
        return maxD