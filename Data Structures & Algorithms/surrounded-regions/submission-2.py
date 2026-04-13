# TRICK QUESTION
class Solution:
    # Optimal
    '''
    Time - O(m*n)
    Space - O(m*n)

    This question is quite similar to all the graph problems. However, there is one logical trick to
    its intuition and getting to the solution. 'O's can be surrounded only if they are no connecting
    vertically or horizontally 'O's on the borders. If the border 'O's can't reach any of the
    internal 'O's, then the internal ones are surrounded. And, if there is even one 'O' on the border
    reachable to an 'O' in the middle (excluding border), then its not surrounded anymore.

    So, in our solution we travserse from all 'O's on the border of the board. If any 'O' is reached
    using DFS, we mark it as reachable (either in new grid, or in place). In the end whatever was not
    reachable was marked as 'X'.
    '''
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

        

        
