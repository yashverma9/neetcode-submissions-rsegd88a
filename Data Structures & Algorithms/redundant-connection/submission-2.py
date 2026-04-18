from collections import defaultdict

class Solution:
    # Brute
    # Time - O(E * (E+V)) - E times because for every edge we do a dfs (each E + V)
    # Space - O(E + V) - dfs recursion stack (E) and visited (V)

    '''
    As one edge is going to cause a cycle before the end of edges list, we do a dfs on existing 
    adjacency list after adding a new edge. Whenever a cycle is detected, we return that new edge.
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        n = len(edges) # No. of edges = Nodes - 1 (as one edge is extra for cycle, n = len(edges)) 
        def isCycle(node, parent):
            if visited[node-1]:
                return True

            visited[node-1] = True
            
            for v in adjList[node]:
                if v == parent:
                    continue
                if isCycle(v, node):
                    return True

            return False            

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visited = [False for _ in range(n)]

            if isCycle(u, None):
                return [u,v]

    