class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ### Brute force ###

        maxArea = 0

        for i in range(len(heights)):
            area = 0
            subMaxArea = heights[i] * 1 # Area of the starting bar itself
            minH = heights[i]
            for j in range(i+1, len(heights)):
                if heights[j] == 0:
                    break
                minH = min(minH, heights[j])
                area = minH * (j-i+1)
                subMaxArea = max(subMaxArea, area)
            maxArea = max(maxArea, subMaxArea)

        return maxArea 
            
        # h[i] = 1, minH = 1, h[j] = 3 area = 2 subMaxarea = 2
        # h[i] = 1 minH = 1, h[j] = 7, area = 