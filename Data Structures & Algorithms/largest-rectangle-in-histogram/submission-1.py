class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ### Brute force ###

        # Calculate area for all combinations of bars from ith + i+1 th -> n th
        # Find max area so far at each step
        # Return max Area

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


        ### Optimal O(n), O(n) space ###

        