class Solution:
    # Brute
    # Time - O(2^n)- as 2 branches (pick a number or not pick) upto n numbers
    # Space - O(n) recursion stack
    '''
    This problem is as simple as finding a group of numbers from nums which is exactly half the
    sum of the total sum of numbers in nums. We group such numbers by having 2 choices when
    we go through nums index by index, either pick a number in sum or skip. This way we have 2
    branches and if either of them returns True we return True.
    '''
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = 0

        for num in nums:
            total += num
        
        # Means sum can't be divide into 2 equal halves, hence not possible for nums
        if total % 2 != 0:
            return False
        
        target = total // 2

        def formSubset(i, curSum):
            if curSum == target:
                return True
            
            if i >= n or curSum > target:
                return False
            
            # Either add current index to subset and go to next, or skip to next
            return formSubset(i+1, curSum + nums[i]) or formSubset(i+1, curSum)
            
        return formSubset(0,0)