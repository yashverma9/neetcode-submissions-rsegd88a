# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS Iterative - In order
        if not root.left and not root.right:
            return True

        stack = []
        cur = root
        inorder = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            inorder.append(cur.val)
            cur = cur.right
        
        for i in range(1, len(inorder)):
            if inorder[i-1] >= inorder[i]:
                return False
        
        return True