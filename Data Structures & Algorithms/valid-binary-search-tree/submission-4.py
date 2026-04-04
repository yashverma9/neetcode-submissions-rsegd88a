# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Brute - we assume its a bst
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
        