# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        self.isBal = True
    

        def dfs (node):
            if not node or not self.isBal:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) > 1:
                self.isBal = False
            
            return 1 + max(left, right)
        
        dfs(root)

        return self.isBal