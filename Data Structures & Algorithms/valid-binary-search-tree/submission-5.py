# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Brute - 
        '''
            We assume its a BST, so whats the violation condition we can check.
            For every node, we find min most value in right subtree (node.right) and max most
            value in left subtree (node.left). Then compare with root val accordingly. The max
            of left most should be still lower than root, if not we return False. Similarly, min
            of right most should be bigger than root. If not we return. 

            Do this recusively for all left and right subtrees
        '''
        if not root:
            return True

        if root.left:
            maxLeft = self.findMax(root.left)
            if maxLeft >= root.val:
                return False
        
        if root.right:
            minRight = self.findMin(root.right)
            if minRight <= root.val:
                return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

            

    # Right most bottom node should be max for the root node in a subtree
    def findMax(self, node):
        while node.right:
            node = node.right
        return node.val

    # left most bottom node should be min for the root node in a subtree
    def findMin(self, node):
        while node.left:
            node = node.left
        return node.val
        