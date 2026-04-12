from collections import deque
# Optimal - BFS*

'''
Time - O(m*n)
Space - O(m*n)

Time and space just for BFS (space same for visited also)

Instead of looking for a treasure from each land cell one by one using DFS, we optimally
do it by doing a multi-source BFS from all treasures to the island cells. We add all
the treasure nodes to the queue, and divide the BFS into levels using a for on the len(q)
which at every iteration of while gives the next step (level). Hence, with every level
we increment the distance by 1 and whenever a room is found which is not visited yet we
mark it with the distance value.
'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set() 

        q = deque()
           
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for row, col in directions:
                    if row in range(rows) and col in range(cols) and (row,col) not in visited and grid[row][col] != -1:
                        q.append((row,col))
                        visited.add((row,col))
            
            dist += 1


