class Solution:
    def trap(self, height: List[int]) -> int:
        
        ### Brute force - Suming area from each index - O(n^2) ###


        # We find max L height and max R height at any index. 
        # Then the amount of water to be stored will be given by min(maxL,maxH) - h[i]
        # This is because are area is determined by the min wall as the rest of water
        # will spill out of the region. And we can determine the area available for
        # water at that index only by first subtracting the height of that index

        # totalArea = 0
        
        # for i in range(len(height)):
        #     maxL = 0
        #     maxR = 0

        #     for j in range(0, i):
        #         if height[j] > maxL:
        #             maxL = height[j]

        #     for j in range(i+1, len(height)):
        #         if height[j] > maxR:
        #             maxR = height[j]

        #     area = min(maxL, maxR) - height[i]
        #     if area < 0:
        #         continue
        #     totalArea += area

        # return totalArea    



        ### Optimal using O(n) space ###


        lMaxStore = [0]
        rMaxStore = [0 for i in range(len(height))]

        for i in range(1, len(height)):
            lMaxStore.append(max(height[i-1], lMaxStore[-1]))
            
        for i in range(len(height)-2,-1,-1):
            rMaxStore[i] = (max(height[i+1], rMaxStore[i+1]))

        totalArea = 0

        for i in range(len(height)):
            area = min(lMaxStore[i], rMaxStore[i]) - height[i]
            if area > 0:
                totalArea += area
        
        return totalArea
