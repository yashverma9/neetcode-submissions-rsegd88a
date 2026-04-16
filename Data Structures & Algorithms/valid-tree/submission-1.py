class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        visited = set()

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def checkCycle(node, parent):
            visited.add(node)

            for nextNode in adjList[node]:
                if nextNode not in visited:
                    if checkCycle(nextNode, node):
                        return True
                elif nextNode != parent:
                    return True
            
            return False
                
        if checkCycle(0, None):
            return False
        
        if len(visited) != n:
            return False
        
        return True


        


        

        