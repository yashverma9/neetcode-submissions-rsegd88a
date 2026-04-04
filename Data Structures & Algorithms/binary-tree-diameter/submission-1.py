# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Using recursive DFS - we calculate max of left and right depth(height), then sum it to find the
        # diameter for that specific nodes. We keep the max diameter in a member variable (acts a global
        # variable) to maintain. At the same time we keep returning max of left and right of node to get max
        # depth from a node and so on till root.

        if not root:
            return 0
        
        self.res = 0 # Important to maintain a member variable otherwise it can't be accessed within dfs func

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right
            self.res = max(self.res, diameter)
            return 1 + max(left, right)

        dfs(root)
        return self.res

    