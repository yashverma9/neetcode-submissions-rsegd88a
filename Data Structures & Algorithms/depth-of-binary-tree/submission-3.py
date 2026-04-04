# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS iterative - we store depth of each node using the previous depth in stack
        # While popping just compare with max depth and just return max in the end
        if not root:
            return 0
        
        depth = 0
        stack = [(root, 1)]
        maxDepth = 0

        while stack:
            (node, curDepth) = stack.pop()
            if curDepth > maxDepth:
                maxDepth = curDepth
            if node.right: stack.append((node.right, curDepth + 1))
            if node.left: stack.append((node.left, curDepth + 1))
        
        return maxDepth

            
