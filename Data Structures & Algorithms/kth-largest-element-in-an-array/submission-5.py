class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using quick select
        k = len(nums) - k # k index from start
        def quickSelect(l, r):
            nonlocal nums
            nonlocal k

            pivot = r
            i = l

            for j in range(l, r):
                if nums[j] <= nums[pivot]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                
            nums[i], nums[pivot] = nums[pivot], nums[i]

            if i == k:
                return nums[i]
            elif k < i:
                return quickSelect(l, i-1)
            else: # k > i
                return quickSelect(i+1, r)
        
        return quickSelect(0, len(nums) - 1)