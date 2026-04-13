class Solution:
    # Optimal - dfs:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        atlantic = [[False for _ in range(cols)] for _ in range(rows)]
        pacific = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, ocean, visited):
            visited[r][c] = True
            directions = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

            for rd, cd in directions:
                if rd in range(rows) and cd in range(cols) and heights[rd][cd] >= heights[r][c] and not visited[rd][cd]:
                    if ocean == 'p':
                        pacific[rd][cd] = True
                    else:
                        atlantic[rd][cd] = True
                    dfs(rd, cd, ocean, visited)
        
        # Pacific
        r = 0
        for c in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            pacific[r][c] = True
            dfs(r,c,'p', visited)
        
        c = 0
        for r in range(rows):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            pacific[r][c] = True
            dfs(r,c,'p', visited)

        # Atlantic
        r = rows-1
        for c in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            atlantic[r][c] = True
            dfs(r,c,'a', visited)
        
        c = cols-1
        for r in range(rows):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            atlantic[r][c] = True
            dfs(r,c,'a', visited)

        res = []
            
        for i in range(rows):
            for j in range(cols):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i,j])

        
        
        return res


                
                
                