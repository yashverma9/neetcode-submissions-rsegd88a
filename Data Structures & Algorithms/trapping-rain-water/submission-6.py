class Solution:
    def trap(self, height: List[int]) -> int:
        # Brute - we calculate area for each ind using left heighest and right heightest bar

        totalArea = 0

        for i in range(1, len(height)-1):
            curH = height[i]
            maxL = 0
            maxR = 0
            for j in range(0, i):
                maxL = max(maxL, height[j])

            for j in range(i+1, len(height)):
                maxR = max(maxR, height[j])
            area = min(maxL, maxR) - curH
            if area > 0:
                totalArea += area
            

        return totalArea

