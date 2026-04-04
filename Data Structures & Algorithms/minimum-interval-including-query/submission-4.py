import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Optimal O(nlogn + mlogm) - sorting both, heap operations are nlogn as well, space O(m + n)
        '''
        We basically use a minheap to store the minimum length and the right of an interval
        If an interval is valid (q <= r), minheap will return the shortest length for it
        else, we pop till we find valid intervals in heap. We add to heap all intervals
        which left is smaller than q (means possible valid).
        '''
        
        intervals.sort()
        res = {}
        minHeap = []

        i = 0

        for q in sorted(queries):
            while i < len(intervals)and intervals[i][0] <= q:
                heapq.heappush(minHeap,(intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]   


