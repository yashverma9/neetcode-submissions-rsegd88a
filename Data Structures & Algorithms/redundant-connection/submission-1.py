from collections import defaultdict

class Solution:
    # Brute
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        n = len(edges) # No. of edges = Nodes - 1 (as one edge is extra) 
        def dfs(node, parent):
            if visited[node-1]:
                return True

            visited[node-1] = True
            
            for v in adjList[node]:
                if v == parent:
                    continue
                if dfs(v, node):
                    return True

            return False            

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            visited = [False for _ in range(n)]

            if dfs(u, None):
                return [u,v]

    