class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute - using sort
        
        nums.sort(reverse = True)

        return nums[k-1]