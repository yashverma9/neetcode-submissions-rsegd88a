class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ### Binary search O(nlogn) ###

        # 1, 2, 5, 10, 23, 25 -  target = 23
        # l = 0, r = 5, mid = 2 
        # l = 3, r = 5, mid = 4
        
        l, r = 0, len(nums) - 1

        while (l <= r):
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1
        