# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Optimal - using Binary search logic. 
        '''
            The lowest ancestor will be the point where these 2 values are split by a node.
            As its a BST, we can just go down left or right accordingly. Where p <= node <= q, we know
            its the split point and the node is the lowest common ancestor
        '''
        if p.val > q.val:
            p , q = q , p
        
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif q.val < root.val:
                root = root.left
            elif p.val > root.val:
                root = root.right

        
            
        



    
