class Solution:
    # Optimal
    # Time/Space - O(V+E), V - No. of node and E is no. of edges
    '''
    A graph is a valid tree only if its connected completely and there is no cycle

    As its (a tree) an undirected graph we add edges both ways in adj list. We start DFS from
    any node (0 just to start), and keep a track of the parent node as well. So, we keep a visited
    set to check for cycle, but when going to a neighbor list from adj list for a node, we avoid
    the parent to avoid false cycle check (as parent shouldn't be revisited). 

    In the end, if we have n nodes in visited and no cycle detected, the graph is a valid tree.

    '''
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


        


        

        