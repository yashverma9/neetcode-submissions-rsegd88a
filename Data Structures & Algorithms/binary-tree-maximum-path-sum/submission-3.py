# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Optimal - O(n), O(n)
        '''
            A path is one in which we only split nodes only once. If we split twice its not a
            path anymore. So if we split root, you need to go one path down on both sides of root.

            But, when you solve this recursively solve this for every node from root to leaves,
            we find 2 values for each node. First is max sum with considering a split on that node, 
            and second is the max value without split which we return to its parent for its calculation.

            We update the maxSum with the first value, and return the second value.  
            -- Note-- The max value with a split can just be the root node if both side are negative
            --Note-- When the left and right max are calculated recursively, if they are less that 0
            we don't need to include them as the max from left or right will then be 0 which means
            excluding the negative nodes.

        '''

        maxSum = [float('-inf')] # We use the 0th index of the list to store max value, as mutation is allowed in nested function not reassignments

        def findSum(node):
            if not node:
                return 0

            leftMax = max(findSum(node.left), 0)
            rightMax = max(findSum(node.right), 0)
            maxSplitSum = max(node.val, node.val + leftMax + rightMax)
            
            if maxSplitSum > maxSum[0]:
                maxSum[0] = maxSplitSum
            
            return node.val + max(leftMax, rightMax)

        findSum(root)

        return maxSum[0]
