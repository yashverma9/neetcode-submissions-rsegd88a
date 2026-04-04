from collections import deque
import heapq 

class Solution:
    # Optimal - max Heap
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque() # [freq, nextAvailableTime]
        freq = {}  
        maxHeap = []

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for f in freq.values():
            maxHeap.append(-f)
        
        heapq.heapify(maxHeap)

        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                frq = 1 + heapq.heappop(maxHeap)
                if frq:
                    q.append([frq, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time                                 
                
