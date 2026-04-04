import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Optimal - use a max heap of k size, which will only have k closest after popping other bigger
        # O(nlogk), O(k)
        # Un-optimal using min heap where O(n + klogn) for heapify and k pops
        res = []
        for point in points:
            x = point[0]
            y = point[1]
            dis = x*x + y*y # No need to sqt, same comparison
            heapq.heappush(res,(-dis, x, y))
            if len(res) > k:
                heapq.heappop(res)
        
        for i in range(k):
            res[i] = [res[i][1], res[i][2]]
        
        return res