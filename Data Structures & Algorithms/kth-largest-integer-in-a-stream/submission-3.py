import heapq
class KthLargest:
    # Using basic array and sort O(nlogn) for each add call, O(m) extra space over orignal nums size
    # m is no. of extra nums added
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums) - self.k]

