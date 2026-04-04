class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Using arrays

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            
            distance = (x*x + y*y) ** (1/2)

            points[i] = (distance, x, y)
        
        points.sort()
        
        res = []

        for i in range(k):
            res.append([points[i][1], points[i][2]])
        
        return res
        