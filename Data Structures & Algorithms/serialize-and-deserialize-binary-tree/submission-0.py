# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
    
        # preorder
        def dfs(node):
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res) # Return string

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            root = nodes[i]
            if root == "N":
                i += 1
                return None
            
            node = TreeNode(int(nodes[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        root = dfs()
        return root



