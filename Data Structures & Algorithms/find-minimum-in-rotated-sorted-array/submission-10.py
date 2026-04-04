class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute is using iteration O(n)

        # Optimal
        l = 0
        r = len(nums)-1
        minNum = float('inf')

        while (l <= r):
            # The break condition when our selection is sorted, hence l is min
            # Also prevents situtation when l to r is sorted, but we shift l to mid+1 skipping the
            # actual min element which was at l
            if nums[l] < nums[r]:
                minNum = min(nums[l], minNum)
                break
            
            mid = l + (r-l)//2
            minNum = min(minNum, nums[mid])

            # Means left side is sorted, so min cant be there - 
            # has to be in unsorted side and minimum is there which is pivot
            # We add equal because they can l and mid can be the leftmost ele
            # And that means the left side is still sorted (1 element is always sorted)
            if nums[l] <= nums[mid]: 
                l = mid + 1
            
            # When left side is not sorted, the min is there - so we eliminate the right half
            else:
                r = mid - 1
            
        return minNum