# TRICK Question
class Solution:
    # Optimal
    # Time- O(n+p), n = no. of courses, p = no.of total prerequisites
    # Space - O(n+p) for recursive stack and visited set

    '''
    This questions looks like a weird one until you realise that its possible to do all the course
    unless there is a cycle it the graph. The courses and its prerequisites can be made into a graph
    with each course being a node pointing to its pre requisite courses. 

    We start by making an adjacency matrix to make it easy to understand the graph. Now we run
    DFS starting from each course one by one. We detect a cycle by using a visited set, if a crs
    is already visited that means its a cycle and we return false directly. Otherwise, another base
    case is added for no prerequisites and we return True as course is possible. Following the base
    cases, we just normally do bfs of all its prerequisites one by one. After doing that we remove
    the course from visited as it might be visited again for other course dfs. We also mark a possible
    course with empty list of prerequisites if its possible to avoid future rework.

    Even though we run DFS from all courses, we make sure we work on each course only once and total complexity
    is only O(n + p). If a processes course is revisited later, it returns in O(1) as it has empty
    list of prerequisites. 

    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        preMap = {i : [] for i in range(numCourses)}

        for pre in prerequisites:
            preMap[pre[0]].append(pre[1])

        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True

        


