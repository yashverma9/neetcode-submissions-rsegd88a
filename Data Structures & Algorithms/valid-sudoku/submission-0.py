class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {i:[] for i in range (0, 9)}
        columnHash = {i:[] for i in range(0, 9)}
        subBoxHash = {i: [] for i in range(0,9)} 

        ## how to determine index for subBoxHash ##
        # So there are total 9 boxes, we can denote using 0 -> 8 index
        # As every box is a 3x3, we can use a mathematical expression using 3
        # (row//3)*3 + (col//3)
        # We floor division row/col and get 0, 1 or 2 at max (8//3 is 2)
        # Now as every row has 3 subbox, we can multiply by 3 and add the col floor divide
        # This way we get index of the subbox. Its like Converting 9x9 into 3x3

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    subBoxIndex = (i//3)*3 + (j//3)
                    if num in rowHash[i] or num in columnHash[j] or num in subBoxHash[subBoxIndex]:
                        return False
                    rowHash[i].append(num)
                    columnHash[j].append(num)
                    subBoxHash[subBoxIndex].append(num)
        
        return True

        # Trying examples- whiteboarding
                # 0,0 -> 2,2

                # 0,3 -> 2,5
                
                # 0,3 0,4 0,5
                # 1,3 1,4 1,5
                # 2,3 2,4 2,5

                # 0,6 -> 2,8              3,3 3,4 3,5
                # 0,6 0,7 0,8.            4,3 4,4 4,5
                # 1,6 1,7 1,8             5,3 5,4 5,5
                # 2,6 2,7 2,8

                
        
