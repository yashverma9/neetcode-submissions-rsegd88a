"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Optimal - Recursive dfs
    '''
    Time - O(V + E), V - vertices, E - edges -> As each node and edge is traversed (2*E technically)
    Spave - O(V) for vertices old to copy in hashmap

    We basically need to clone each node as well as map each clone its neighbors which
    are also clones of its original neighbors. So, we do it recursively using bfs. Every node
    which hasnt been cloned, is cloned and added to map. We then add its neighbors using same bfs
    and return a node directly if thats already cloned
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        # Recursive dfs
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            new = Node(node.val)
            oldToNew[node] = new
            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))
            
            return new
        
        start = dfs(node)
        return start