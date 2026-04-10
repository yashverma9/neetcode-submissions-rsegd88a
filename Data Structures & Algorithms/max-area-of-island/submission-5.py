class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Optimal -dfs iterative
        # Time - O(m*n) -similar as previous question
        # Space - O(m*n) for stack
        '''
            On the same lines as the previous questions, instead of counting unique islands,
            This time we just follow all connected lands(1) to a starting land/node(1) and
            update the max area with area once we don't have any more connected lands.

            We also mark visited nodes as '-' inplace of the input grid so that we don't
            repeat a node again while calculating area.
        '''
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
        