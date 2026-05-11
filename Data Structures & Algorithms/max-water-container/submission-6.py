class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute
        res = 0
        n = len(heights)

        for i in range(n):
            for j in range(i+1, n):
                h = min(heights[i], heights[j])
                l = j - i
                area = h*l
                if area > res:
                    res = area

        return res    
        