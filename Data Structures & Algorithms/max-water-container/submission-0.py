class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        area = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                leng = j-i
                height = min(heights[i], heights[j])
                area = leng*height
                maxArea = max(area, maxArea)

        return maxArea

        # l , r = 0 , len(heights)-1
        
        # maxArea = 0
        # area = 0

        # while (l < r):
        #     leng = r - l
        #     height = min(heights[l], heights[r])
        #     area = leng * height
        #     i
        