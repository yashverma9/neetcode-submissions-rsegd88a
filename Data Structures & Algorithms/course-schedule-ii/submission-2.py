class Solution:
    # Optimal
    # Time - O(n + p)
    # Space - O(n + p)
    '''
    Very similar question as the last one. Instead of just detecting cycle, we also store the
    order in which courses should be done (basically like post order dfs). We use something called
    topological sort. So, now we maintain to sets. One for detecting if a course is visited twice
    during a cycle, and another set for overall processed/visited courses.

    Once, a node is visited it means it has been added to result. We return result if no cycle detect.
    or empty list if detected.
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        visited = set() # Stores processed courses(nodes) overall, added to the result
        cycle = set() # Stores processed courses(nodes) visited in the same dfs cycle.
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res