class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force - lets find all possible areas, then the max out of them
        maxArea = 0
        
        for i in range(len(heights)):
            curHeight = heights[i]
            left = i
            right = i

            while left >= 0 and heights[left] >= curHeight:
                left -= 1
            
            while right <= len(heights) -1 and heights[right] >= curHeight:
                right += 1
            
            left += 1
            right -= 1

            area = curHeight*(right-left+1)
            maxArea = max(area, maxArea)

        return maxArea