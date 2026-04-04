import heapq
class MedianFinder:
    # Optimal
    # Add - each O(logn), median - O(1) each
    '''
    We now maintain 2 heaps dividing the numbers into 2 parts which are either equal
    or not bigger than each other by more than 1. Now important thing is, we make
    left half as a max heap to find the biggest element (of left half) in O(1) and 
    right half as min-heap to find the lowest element (of right) in O(1). This way
    the median is always on top of either of them, or avg of both tops when equal halves.

    Hence, we add to left unless an element is bigger than right min. And we keep
    shifting numbers between them if either grows bigger than the other by 1. 
    This helps maintaining median always at top of these and helps us in O(1).
    '''
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
        
        