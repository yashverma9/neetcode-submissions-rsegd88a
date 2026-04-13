class Solution:
    # Optimal - dfs:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        atlantic = [[False for _ in range(cols)] for _ in range(rows)]
        pacific = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, ocean):
            ocean[r][c] = True
            directions = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

            for rd, cd in directions:
                if rd in range(rows) and cd in range(cols) and heights[rd][cd] >= heights[r][c] and not ocean[rd][cd]:
                    dfs(rd, cd, ocean)
        
        # Pacific
        r = 0
        for c in range(cols):
            dfs(r,c, pacific)
        
        c = 0
        for r in range(rows):
            dfs(r,c,pacific)

        # Atlantic
        r = rows-1
        for c in range(cols):
            dfs(r,c,atlantic)
        
        c = cols-1
        for r in range(rows):
            dfs(r,c,atlantic)

        res = []
            
        for i in range(rows):
            for j in range(cols):
                if atlantic[i][j] and pacific[i][j]:
                    res.append([i,j])

        
        
        return res


                
                
                