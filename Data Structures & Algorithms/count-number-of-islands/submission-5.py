from collections import deque
class Solution:
    # Optimal - BFS iterative
    # Same time/space
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])        

        islands = 0

        # BFS
        def discover(r, c):
            q = deque()
            q.append([r,c])

            while q:
                row, col = q.popleft()
                directions = [[row+1,col], [row-1,col], [row,col-1], [row,col+1]]
                for dr, dc in directions:
                    if dr in range(rows) and dc in range(cols):
                        if grid[dr][dc] == '1':
                            grid[dr][dc] = '-'
                            q.append([dr, dc])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    grid[r][c] == '-'
                    discover(r,c)
        
        return islands
                    