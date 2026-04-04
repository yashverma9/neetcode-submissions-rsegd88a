import heapq
class KthLargest:
    # Using min heap
    # For Init - O(n) for heapify, n-k pops (each logn) which is nlogn (n is len nums on init)
    # For add - O(mlogk) - for m number push
    # Space is O(k) as we have only k elements in heap everytime
    '''
        We can use a min heap directly but not store all the nums in the heap
        After making the heap, if we remove numbers such that only k are there in the heap
        then we know they are the k largest numbers and the min of the heap will give the kth

        Hence, we pop till we have only k

        On add, we pop if the numbers exceed k, and return top /min
    '''
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums
        self.k = k
        while len(nums) > k:
            heapq.heappop(self.nums)
        # This can be optimized further to nlogk by adding each element to heap one by one

        '''
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        '''

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]