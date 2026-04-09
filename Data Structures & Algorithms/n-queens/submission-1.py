class Solution:
    # Optimal:
    # Time - O(n^2 * n!) - Because every step we have n choices, then <= n-1 , then <= n-2 and so on
    # Its like permutation behaviour, and n^2 for copy to res
    # Space - O(n^2) for board, O(n) for recursion stack, O(n!) for output if considered
    '''
    So we do a smart backtracking. We maintain a set for cols, diagonals (pos and neg) both
    visited. We don't need to maintain for row as for each new queen we consider a row
    at a time and then move to next row for next queen. Positive diagnals mean from left bottom
    to right top and negative mean from left top to right bottom.

    So, everytime we visit a row. We try all columns which is available and not yet
    covered as a column or diagonal. We update the sets and also the board with a Queen
    on that r,c index. And backtrack to next row. Like any other backtrack problem we remove
    those from set once the backtrack return. 

    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set() # Cols where queen is put
        posDiag = set() # + diag where queen is put
        negDiag = set() # - diagonals where queen is put

        board = [['.' for _ in range(n)] for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1) 

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

                
        backtrack(0)
        return res