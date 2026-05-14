class Solution:
    def findMin(self, nums: List[int]) -> int:
        # EASIER TO UNDERSTAND/MEMORIZE SOLUTION
        '''
        Basically we find a middle and figure out its position based on the
        last number of the l - r. So, if the middle number is more than the 
        right most number, that means the array's pivot(/min) lies in the right
        half of mid. Hence, we move l = mid + 1

        Else, if the mid is smaller than the right number, that means the pivot
        or min of array is either mid or left of mid. Hence, r = mid

        In the end our loop breaks when l = r and 
        '''
        l = 0 
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid
            
        
        return nums[r]