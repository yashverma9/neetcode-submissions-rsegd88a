class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Optimal - bfs
        rows = len(grid)
        cols = len(grid[0])
        
        islands = 0

        def discover(r, c):
            directions = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            for row, col in directions:
                if row in range(rows) and col in range(cols):
                    if grid[row][col] == '1':
                        grid[row][col] = '-'
                        discover(row, col)
            return
        
        for r in range(rows):
            for c in range(cols):   
                if grid[r][c] == '1':
                    islands += 1
                    discover(r, c)
    
        return islands