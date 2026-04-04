# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Using DFS recursive  
        '''
        Similar logic, we just append first node of each level
        '''

        if not root:
            return []

        res = []

        def dfs(node, depth):
            if not node:
                return
            
            # Now we just append first element of that depth/level
            # That is always the right most
            # As we are discovering each right node first below
            if len(res) == depth:
                res.append(node.val)

            # We discover right node first, hence a right node discovers a new depth
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)

        return res