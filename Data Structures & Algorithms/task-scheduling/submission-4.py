from collections import deque
import heapq 

class Solution:
    # Optimal - max Heap
    # Time - O(m*n*log26) ~ O(m*n) again, but n is considered upto 100 hence smaller hence O(m), 
    # space = O(1)
    # This is more optimal because of log26 vs 26
    ''' 
        Instead of maintaining 2 hashmaps, we maintain a max heap which returns max freq at a time,
        and the deque which maintains freq of tasks and time when they will be next available
    
        In this solution, we increment time before processing. We process max freq from maxheap,
        add it to queue with one less freq (if not 0) and its next available time as time + n 
        (instead time+n+1 in brute as time incremented in beg. of iteration). 
        Then we check if a task has become available in the queue basedon the currrent time. 
        We add it to heap for later processing.

        Most optimal which is truly O(m) using a formula.

    '''
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
                
