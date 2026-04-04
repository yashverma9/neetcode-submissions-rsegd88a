# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recrusive DFS
        '''
            We use same logic of inorder traversal and keep count. Once we reach count of k
            during traversal, we have found our kth small node
            We exit recurssion quickly by checking for res having a value other than None

            BRUTE Force will be to traverse using any dfs, then sort the list and return arr[k-1]
        '''

        count = 0
        res = None

        def dfs(node):
            nonlocal count
            nonlocal res

            if res is not None or not node:
                return
            
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
            
            dfs(node.right)
        
        dfs(root)
        return res