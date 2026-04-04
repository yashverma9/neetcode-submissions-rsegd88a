import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        self.maxHeap = nums
        self.k = k

    def add(self, val: int) -> int:
         # maxHeap using a minheap with (-)tive values
        val = -val
        heapq.heappush(self.maxHeap, val)
        sort = []
        for i in range(self.k):
            val = -heapq.heappop(self.maxHeap)
            sort.append(val)
        
        for i in range(self.k):
            heapq.heappush(self.maxHeap, -sort[i])
        
        return sort[-1]
