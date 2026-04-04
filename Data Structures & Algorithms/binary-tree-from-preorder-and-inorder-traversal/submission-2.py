# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        valInorder = {}
        for i in range(len(inorder)):
            valInorder[inorder[i]] = i
        
        rootIndex = 0
        def construct(l, r):
            # Base condition when no nodes left in subtree
            if l > r:
                return None
            nonlocal rootIndex
            rootVal = preorder[rootIndex]
            root = TreeNode(rootVal)
            mid = valInorder[rootVal]
            rootIndex += 1
            root.left = construct(l, mid-1)
            root.right = construct(mid+1, r)
            return root
            

        root = construct(0, len(inorder)-1)

        return root