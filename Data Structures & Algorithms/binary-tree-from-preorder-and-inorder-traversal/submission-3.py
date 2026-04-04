# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Optimal - O(n), space -O(n) with hash map also
        '''
            In this approach we do the exact same thing, though instead of using lists
            we use a hash map to store index to val for inorder. This save O(n) to find the
            index of root node of a subtree in the inorder list

            Now before our base case was an empty preorder/ inorder which meant no more nodes left
            to discover in the subtree. Here, we do similar hack using the left and right index ranges
            for possible values. So, instead of slicing (again O(k), k size of slice) again and again
            to find range of preorder values subtree has, we just use a range.

            Also, the base condition becomes l > r which will either be if r drops below l making it 
            no nodes left in left tree or l growing bigger than r making it no nodes left in right
        '''
        valInorder = {}
        for i in range(len(inorder)):
            valInorder[inorder[i]] = i
        
        rootIndex = 0
        def construct(l, r):
            # Base condition when no nodes left in subtree
            if l > r:
                return None
            nonlocal rootIndex
            rootVal = preorder[rootIndex]
            root = TreeNode(rootVal)
            mid = valInorder[rootVal]
            rootIndex += 1
            root.left = construct(l, mid-1)
            root.right = construct(mid+1, r)
            return root
            

        root = construct(0, len(inorder)-1)

        return root