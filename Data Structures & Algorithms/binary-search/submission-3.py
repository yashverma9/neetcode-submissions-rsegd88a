class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        # mid = (left + right)//2 
        # In python there is no limit to integer size, but in other languages
        # for big sizes, this could overflow when adding.Better way is using this:
        mid = left + (right-left)//2

        while (left <= right):
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

            mid = left + (right-left)//2

        return -1        