import heapq
class MedianFinder:
    # Brute
    '''
    if len divisible by 2:
        median = (num[(len/2) - 1] + num[len/2])/2
    else:
        median = num[len//2]
    '''
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        popped = []
        length = len(self.heap)
        if length == 0:
            return 0
        numsToPop = length//2 + 1

        for i in range(numsToPop):
            popped.append(heapq.heappop(self.heap))
        
        for num in popped:
            heapq.heappush(self.heap, num)
        if length % 2 == 0:
            return (popped[-1] + popped[-2])/2
        else:
            return popped[-1]
        