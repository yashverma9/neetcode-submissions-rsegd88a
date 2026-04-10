class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        # DFS iterative
        def discover(r, c):
            nonlocal maxArea
            area = 0
            stack = [[r,c]]
            grid[r][c] = '-'
            while stack:
                row, col = stack.pop()
                area += 1
                directions = [[row+1,col], [row-1,col], [row,col+1], [row,col-1]]
                for rd, cd in directions:
                    if rd in range(rows) and cd in range(cols):
                        if grid[rd][cd] == 1:
                            stack.append([rd,cd])
                            grid[rd][cd] = '-'
            if area > maxArea:
                maxArea = area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    discover(row, col)
        
        return maxArea
        