from collections import deque
# Optimal - BFS:
# Time - O(m*n)
# Space - O(m*n)

'''
    This questions also follows similar logic of doing a BFS from all rotten nodes at once. 
    And BFS allows us to divide the traversal step/level by level into minutes. So, every
    for loop on the len(q) is one minute. If we keep having rotten oranges, then we keep
    running BFS.

    Why BFS over DFS? That's because multiple rotten nodes will work simulataneously and rot
    their respective adjacent oranges at the same time. If we did DFS, we would go down the path
    of one rotten orange which will take more time than actual to rot a far away orange which might
    be close to another rotten orange that will be discovered later.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        freshCount = 0
        mins = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])
                if grid[r][c] == 1:
                    freshCount += 1

        while q and freshCount > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]

                for rd, rc in directions:
                    if rd in range(rows) and rc in range(cols) and grid[rd][rc] == 1 and (rd,rc) not in visited:
                        grid[rd][rc] = 2
                        visited.add((rd,rc))
                        q.append([rd,rc])
                        freshCount -= 1
            mins += 1       
        
        return mins if freshCount == 0 else -1
        