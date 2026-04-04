class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Optimal - using 2 pointers
        
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while (l < r):
            heightLeft, heightRight = heights[l], heights[r]
            area = (r-l) * min(heightLeft, heightRight)
            if area > maxArea:
                maxArea = area

            if heightLeft <= heightRight:
                l += 1
            else:
                r -= 1
            
        return maxArea