class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        We always know that only 1 half will be sorted, other will have the rotation
        point. Hence, we identify half is sorted (elif or else), and if the target
        is between that half then we go in that, otherwise the other.
        '''
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid

            # Left portion sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                
            # Right sorted: nums[mid] < nums[r]
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                
                else:
                    r = mid - 1

            
        return -1


                