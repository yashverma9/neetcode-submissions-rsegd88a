class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        borderReachable = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            borderReachable[r][c] = True
            dirs = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

            for rd, cd in dirs:
                if rd in range(rows) and cd in range(cols) and board[rd][cd] == 'O' and not borderReachable[rd][cd]:
                    dfs(rd, cd)


        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
        
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)

        for c in range(cols):
            if board[rows-1][c] == 'O':
                dfs(rows-1, c)
        
        for r in range(rows):
            if board[r][cols-1] == 'O':
                dfs(r, cols-1)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and not borderReachable[i][j]:
                    board[i][j] = 'X'

        

        
