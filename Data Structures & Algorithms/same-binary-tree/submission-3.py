# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        equivalent = True

        def dfs(node1, node2):
            nonlocal equivalent
            
            if not equivalent:
                return

            if not node1 and not node2:
                return
            
            if not node1 or not node2:
                equivalent = False
                return
            
            if node1.val != node2.val:
                equivalent = False

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p, q)

        return equivalent