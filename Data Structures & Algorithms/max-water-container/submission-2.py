class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ### Brute force - O(n^2)

        # maxArea = 0
        # area = 0

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         leng = j-i
        #         height = min(heights[i], heights[j])
        #         area = leng*height
        #         maxArea = max(area, maxArea)

        # return maxArea

        ### Optimal O(n) using 2 pointer ###

        # This approach of shifting based on min height works
        # because min height is deciding factor we control
        # the gap between bars is anyways going to reduce when we 
        # consider all posibilities. So to maximise chance of getting maxArea
        # earlies is to adjust based on min height

        l , r = 0 , len(heights)-1
        
        maxArea = 0
        area = 0

        while (l < r):
            leng = r - l
            height = min(heights[l], heights[r])
            area = leng * height
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: # Case when both equal, doesn't matter we can shift any
                l += 1
        return maxArea
        