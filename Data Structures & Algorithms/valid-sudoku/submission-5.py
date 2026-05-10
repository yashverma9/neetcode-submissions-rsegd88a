from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowFreq = [set() for _ in range(9)]
        colFreq = [set() for _ in range(9)]
        boxFreq = [set() for _ in range(9)]


        for row in range(9):
            for col in range(9):
                num = board[row][col] 
                boxNo = (row//3)*3 + col//3
                if num != '.' and (num in rowFreq[row] or num in colFreq[col] or num in boxFreq[boxNo]):
                    return False
                rowFreq[row].add(num)
                colFreq[col].add(num)
                boxFreq[boxNo].add(num)

        return True


            
            