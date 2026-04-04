# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursive dfs 
        '''
            We calculate left and right height for each node using DFS, compare at every node. If more than 1
            difference for any node we update the res member variable to false. In the end we return res
        '''
        self.res = True

        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(right - left) > 1:
                self.res = False

            return 1 + max(left, right)
        
        dfs(root)

        return self.res