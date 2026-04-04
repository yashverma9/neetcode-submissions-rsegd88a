class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowDigits = [{} for _ in range(9)]
        colDigits = [{} for _ in range(9)]
        subBoxDigits = [{} for _ in range(9)]

        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                subBoxIndex = (row//3)*3 + col//3
                if digit != ".":
                    rowDigits[row][digit] = rowDigits[row].get(digit, 0) + 1
                    colDigits[col][digit] = colDigits[col].get(digit, 0) + 1
                    subBoxDigits[subBoxIndex][digit] = subBoxDigits[subBoxIndex].get(digit, 0) + 1

        for row in rowDigits:
            for count in row.values():
                if count > 1:
                    return False

        for col in colDigits:
            for count in col.values():
                if count > 1:
                    return False

        for subBox in subBoxDigits:
            for count in subBox.values():
                if count > 1:
                    return False

        return True