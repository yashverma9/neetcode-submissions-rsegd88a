# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS - recursive
        '''
            We maintain a depth variable using the function parameters. Everytime a new depth
            is reached, we add an empty list at that depth index of res and keep updating values of
            current node into that depth list

            Same can be done using iterative dfs with a stack maintaining nodes, and also depth of
            each node as we push into stack
        '''
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