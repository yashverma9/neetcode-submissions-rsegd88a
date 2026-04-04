# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Brute force - O(n2)
        # traverse tree using dfs, then find max left and right for each node


        res = float('-inf')
    
        def findMax(node):
            if not node:
                return 0
            leftMax = max(0, findMax(node.left))
            rightMax = max(0, findMax(node.right))

            return node.val + max(leftMax, rightMax)
            
        
        def dfs(root):
            if not root:
                return None
            nonlocal res

            leftMax = max(0,findMax(root.left))
            rightMax = max(0,findMax(root.right))

            pathSum = max(root.val, leftMax + rightMax + root.val)

            if pathSum > res:
                res = pathSum
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res
