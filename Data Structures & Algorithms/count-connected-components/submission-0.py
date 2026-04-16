class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = {i:[] for i in range(n)}
        compCount = 0

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node):
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
    
        for node in range(n):
            if node not in visited:
                compCount += 1
                dfs(node)
            
        
        return compCount