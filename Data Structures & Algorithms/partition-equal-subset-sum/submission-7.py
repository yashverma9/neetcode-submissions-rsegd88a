class Solution:
    # Optimal- DP - bottom-up
    # Time - O(n * sum(or target))
    # Space - O(sum)
    '''
    A completely different approach than the brute and top-down, we maintain all possible sum 
    possible from behind using a hashset. We add a new number from behind to all existing sums,
    and also individually add it as a new sum. If we reach target ever, we return True
    '''
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total //2

        dp = set()
        n = len(nums)

        for i in range(n-1, -1, -1):
            nextDp = set() # We have to make a new one everytime as we cant update set during iter.
            for val in dp:
                nextDp.add(val + nums[i])
                nextDp.add(val) # Add the same val also as nextDp doesn't have it yet
                
            if nums[i] not in nextDp:
                nextDp.add(nums[i])
            
            if target in nextDp:
                return True
            dp = nextDp

        return False