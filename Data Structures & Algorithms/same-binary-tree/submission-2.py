# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative dfs: 
        '''
            Can be done using any recursive or iterative bfs/dfs. Just store both trees in stack one by one,
            check 3 things. If both are None, you skip everything and continue. If either None, then you
            are safe to return False and finally If both are not equal in value, you return False.

            Instead of using 2 stacks you can append into one using tuples (node1, node2)
        '''

        if not p and not q:
            return True
        
        if not p:
            return False
        
        if not q:
            return False

        
        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            stack1.append(node1.right)
            stack1.append(node1.left)
            stack2.append(node2.right)
            stack2.append(node2.left)
            
        return True