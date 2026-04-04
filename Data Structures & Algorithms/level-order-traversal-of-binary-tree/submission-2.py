# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS - recursive
        self.res = []

        def dfs(node, depth):
            if not node:
                return
            
            # This means we have a new depth, and need to another empty sublist for that depth now
            # As we start depth from 0, len will always be equal to depth when a new depth comes
            if len(self.res) == depth:
                self.res.append([])
            
            self.res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return self.res