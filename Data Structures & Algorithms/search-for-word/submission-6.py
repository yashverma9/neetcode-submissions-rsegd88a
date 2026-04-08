class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       # Optimal
        row = len(board)
        col = len(board[0])

        def backtrack(i, j, curInd):
            if curInd == len(word):
                return True

            if i == row or i < 0 or j == col or j < 0 or board[i][j] != word[curInd]:
                return False
            
            temp = board[i][j]
            board[i][j] = "-"

            found = (
                backtrack(i+1, j, curInd + 1) or
                backtrack(i-1, j, curInd + 1) or 
                backtrack(i, j+1, curInd + 1) or
                backtrack(i, j-1, curInd + 1)
            )
            board[i][j] = temp
            return found
            
            
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True

        return False
