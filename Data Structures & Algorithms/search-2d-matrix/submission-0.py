class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ### Brute force O(m*n)###

        # Simply iterate m*n as linear search

        ### Optimal using binary search ###

        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS*COLS - 1

        while l <= r:
            mid = l + (r-l)//2
            row, col = mid // COLS, mid % COLS  

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False