class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            # Shortlist a row

            top = 0
            down = len(matrix) - 1
            row = -1
            while top <= down:
                mid = top + (down-top)//2

                if target > matrix[mid][-1]:
                    top = mid + 1
                
                elif target < matrix[mid][0]:
                    down = mid - 1
                
                else:
                    row = mid
                    break
            
            if row == -1:
                return False
            
            l = 0
            r = len(matrix[0]) - 1

            while l <= r:
                mid = l + (r-l)//2

                if target == matrix[row][mid]:
                    return True
                
                elif target < matrix[row][mid]:
                    r = mid - 1
                
                else:
                    l = mid + 1
            
            return False

