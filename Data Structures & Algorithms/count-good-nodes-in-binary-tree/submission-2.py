# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS- recursive
    '''
        We maintain a max value seen till now. If ever a node during iteration is bigger or equal
        to the max val, we just increment the count. 
    '''
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxVal):
            nonlocal count

            if not node:
                return
            
            if node.val >= maxVal:
                count += 1
                maxVal = node.val

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root, root.val)
        return count