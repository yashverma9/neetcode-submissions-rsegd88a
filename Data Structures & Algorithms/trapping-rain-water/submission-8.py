class Solution:
    def trap(self, height: List[int]) -> int:
        # Optimal using 2 pointer
        
        totalArea = 0
        l = 0
        r = len(height) - 1
        maxL = height[0]
        maxR = height[len(height)-1]

        while (l < r):
            # Shift left as left is smaller and restricting, so we are capable of finding
            # the area stored on l+1
            if maxL <= maxR: 
                l += 1
                area = maxL - height[l]
                maxL = max(maxL, height[l])

            # Shift right as right is smaller and restricting, so we are capable of finding
            # the area stored on r -1
            else: 
                r -= 1
                area = maxR - height[r]
                maxR = max(maxR, height[r])
                
            
            if area > 0:
                totalArea += area
        
        return totalArea


