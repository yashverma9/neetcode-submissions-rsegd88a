class Solution:
    def trap(self, height: List[int]) -> int:
        # BRUTE
        n = len(height)
        total = 0
        for i in range(n):
            maxL = 0
            maxR = 0
            cur = height[i]
            for j in range(0, i):
                if height[j] > cur:
                    maxL = max(maxL, height[j])

            for j in range(i+1, n):
                if height[j] > cur:
                    maxR = max(maxR, height[j])
            
            area = min(maxL, maxR) - cur
            if area > 0:
                total += area
        
        return total