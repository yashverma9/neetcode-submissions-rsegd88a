class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            after = l + (r-l)//2
            before = after - 1

            if after - 1 < 0:
                before = len(nums) - 1

            if nums[before] > nums[after]:
                break
            
            elif nums[after] > nums[r]:
                l = after + 1
            else:
                r = after - 1

        return nums[after]