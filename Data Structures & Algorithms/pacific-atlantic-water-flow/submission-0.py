class Solution:
    # Brute - DFS from each node:
    # Time - O((m*n)^2)
    # Space - O(m*n)

    '''
    This is brute because we traverse to the oceans individually for all cells. Hence, we do a dfs
    from each cell and if ocean is reached we keep track of it and return
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        res = []

        def dfs(row, col, visited):
            visited[row][col] = True
            pacific = row == 0 or col == 0
            
            atlantic = row == rows-1 or col == cols-1
            
            directions = [[row-1,col], [row+1,col], [row,col-1], [row,col+1]]
        
            for rd, cd in directions:
                if rd in range(rows) and cd in range(cols) and not visited[rd][cd] and heights[row][col] >= heights[rd][cd]:
                    visited[rd][cd] = True
                    p, a = dfs(rd, cd, visited)
                    pacific = pacific or p
                    atlantic = atlantic or a

            return pacific, atlantic

        for row in range(rows):
            for col in range(cols):
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                p, a = dfs(row, col, visited)
            
                if p and a:
                    res.append([row,col])

        return res