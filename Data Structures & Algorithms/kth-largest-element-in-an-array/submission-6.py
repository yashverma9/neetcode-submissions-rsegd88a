class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using quick select Avg O(n), O(logn). Worst O(n2), O(n)
        '''
        We us the core logic of quick sort. We find pivot (index i ) separating elements greater than
        it and smaller/equal that it. Hence, at every iteration we have an index which is sorted

        If that index is kth from end we return the number. If not, we quickselect from left or right
        side based on position of current pivot (i) lesser or greater than k

        See DSA notion notes for more understanding 
        '''
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