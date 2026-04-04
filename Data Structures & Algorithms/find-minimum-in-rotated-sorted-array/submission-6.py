class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute is using iteration O(n)

        # Optimal
        l = 0
        r = len(nums)-1
        minNum = float('inf')

        while (l <= r):
            if nums[l] < nums[r]:
                minNum = min(nums[l], minNum)
                break
            
            mid = l + (r-l)//2
            minNum = min(minNum, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            
            else:
                r = mid - 1
            
        return minNum