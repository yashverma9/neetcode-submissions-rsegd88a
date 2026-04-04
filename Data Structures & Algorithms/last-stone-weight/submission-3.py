import heapq
class Solution:
    # Optimal - using heap
    # O(nlogn) - As we pop n times each taking logn
    # O(1) extra space
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first == second:
                continue
            else:
                newStone = first - second
            
            heapq.heappush(stones, -newStone)
        
        if len(stones) == 0:
            return 0
        
        return -stones[0]
            