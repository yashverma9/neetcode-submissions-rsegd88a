# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Using recursive dfs O(n2), O(n)
        '''
            For every tree, the first node of the preorder is the root. And that node values in the
            inorder divides the left and right subtree nodes for that root
            Hence, we find the root from 0th index, then find the index of that in inorder.
            The no. of node left side of mid (root) form the left sub tree and no. of node right side
            form the side sub tree. We recursively pass the cut down preorder and inorder using the mid
            index and find subtrees and connect them to root.left and root.right accordingly.
        '''
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root