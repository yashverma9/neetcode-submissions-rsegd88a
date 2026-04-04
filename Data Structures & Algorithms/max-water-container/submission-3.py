class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute
        maxArea = 0
        for i in range(len(heights)-1):
            heightA = heights[i]
            for j in range(i+1, len(heights)):
                area = min(heightA, heights[j]) * (j-i)
                if area > maxArea:
                    maxArea = area

        return maxArea
