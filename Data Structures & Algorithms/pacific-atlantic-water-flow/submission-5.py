class Solution:
    # Optimal - dfs:
    ''' 
    Time - O(m*n) - Even though we do dfs from each ocean border 2*(m+n) nodes, 
    we visit each node (m*n) only <= 2 for both oceans traversals
    Space - O(m*n)- For recursive stack (worse case), and 2 ocean 2d arrays

    So, before we were trying to find the ocean from each cell. This time we traversal to all possible
    cells from the ocean border nodes (row 0 col 0 row n col n). Whatever cell is reachable from 
    either oceans we store it in an array. In the end we return the cells which were both reachable
    after the entire DFS traversal.

    '''
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


                
                
                