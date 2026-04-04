class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force - we find area for all index bars by finding the left and right most
        # boundary and calculating its area with height of the bar
        maxArea = 0
        
        for i in range(len(heights)):
            curHeight = heights[i]
            left = i
            right = i

            while left >= 0 and heights[left] >= curHeight:
                left -= 1
            
            while right <= len(heights) -1 and heights[right] >= curHeight:
                right += 1
            
            # We have to do this as to consider the boundary indices we enter while loop again
            # and left becomes -1 and right become len(heights)
            # So we always do one extra operation after chcking if it valid or not
            left += 1
            right -= 1

            area = curHeight*(right-left+1)
            maxArea = max(area, maxArea)

        return maxArea