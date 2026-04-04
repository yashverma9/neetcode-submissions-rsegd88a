class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search

        # First- perform binary search on all rows to find the row

        top = 0
        bottom = len(matrix) - 1
        mid = top + (bottom-top)//2

        while (top <= bottom):
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break            
            elif target < matrix[mid][0]:
                bottom = mid-1
            else:
                top = mid+1
            mid = top + (bottom-top)//2
        
        if top > bottom:
            return False
        
        row = mid
        left = 0
        right = len(matrix[0])-1
        mid = left + (right-left)//2 

        while (left <= right):
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                left = mid+1
            
            mid = left + (right-left)//2

        return False                

