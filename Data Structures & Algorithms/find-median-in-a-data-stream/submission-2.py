import heapq
class MedianFinder:
    # Optimal
    def __init__(self):
        self.left = [] # max-heap
        self.right = [] # min-heap

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num) #(-)tive as maxheap
        
        if len(self.left) > len(self.right) + 1:
            top = -heapq.heappop(self.left)
            heapq.heappush(self.right, top)
        elif len(self.left) + 1 < len(self.right):
            top = heapq.heappop(self.right)
            heapq.heappush(self.left, -top)  

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2
        
        elif len(self.left) > len(self.right):
            return -self.left[0]
        
        else:
            return self.right[0]
        
        