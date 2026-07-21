# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0

        def dfs(node, curMax):
            nonlocal res
            if not node:
                return
            
            if node.val >= curMax:
                res += 1
            
            if node.left:
                dfs(node.left, max(curMax, node.val))
            if node.right:
                dfs(node.right, max(curMax, node.val))
            
        dfs(root, root.val)

        return res