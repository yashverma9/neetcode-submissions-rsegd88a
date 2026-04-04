# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS Iterative - In order
        '''
        We know an inorder is sorted for a bst tree because first we see left for each node, then
        the node and then the right node. Hence we keep track of prev node and compare it with next
        node's value in inorder traversal. Any node not matching the condition, we return False
        '''
        if not root.left and not root.right:
            return True

        stack = []
        cur = root
        prev = float('-inf') # Lowest value to compare with for first time as inorder is ascending order
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if cur.val <= prev:
                return False
            prev = cur.val
            cur = cur.right
    
        return True