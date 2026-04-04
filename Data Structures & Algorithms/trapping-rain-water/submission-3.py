class Solution:
    def trap(self, height: List[int]) -> int:
        
        ### Brute force - Summing area from each index - O(n^2) ###

        # We find max L height and max R height at any index. 
        # Then the amount of water to be stored will be given by min(maxL,maxH) - h[i]
        # This is because are area is determined by the min wall as the rest of water
        # will spill out of the region. And we can determine the area available for
        # water at that index only by first subtracting the height of that index

        # You must be thinking how come any max well on either sides is okay for any index ?
        # This is because we need to form a bucket to hold water. Yes if we are talking about
        # index 2 and the max L is at index 0 and max R is at index 5. So the bucket width is too big
        # But that doesnt matter to us, because we only find area of that index within the bucket
        # And we subtract by height of that index 2 just to ignore the space occupied by tower itself
        # This way area of each index within the max bucket possible is calculated and we dont care
        # if the max L and max R are directly adjacent or not


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


        ### Optimal using O(n) time, O(n) space ###

        # lMaxStore = [0]
        # rMaxStore = [0 for i in range(len(height))]

        # for i in range(1, len(height)):
        #     lMaxStore.append(max(height[i-1], lMaxStore[-1]))
       
        # for i in range(len(height)-2,-1,-1):
        #     rMaxStore[i] = (max(height[i+1], rMaxStore[i+1]))

        # totalArea = 0

        # for i in range(len(height)):
        #     area = min(lMaxStore[i], rMaxStore[i]) - height[i]
        #     if area > 0:
        #         totalArea += area
        
        # return totalArea


        ### Using only O(n) time, O(1) space - 2 pointer ###
#        L                 R
#        0,2,0,3,1,0,1,3,2,1
#        maxL = 
#        maxR = 


        left, right = 0, len(height)-1
        maxL = height[0] # as area of 0 index is 0, we start from 1 index, maxL till then is h[0]
        maxR = height[-1] # Similarly we start right side from len-2, maxR is hence h[len-1] (or -1)

        totalArea = 0

        while (left < right):
            if maxL <= maxR:
                left += 1
                area = maxL - height[left]
                maxL = max(maxL, height[left])              
            else:
                right -= 1
                area = maxR - height[right]
                maxR = max(maxR, height[right])        
            
            if area > 0:
                totalArea += area

        return totalArea