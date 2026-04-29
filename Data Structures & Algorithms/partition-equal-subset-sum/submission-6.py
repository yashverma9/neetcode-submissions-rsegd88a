class Solution:
    # Optimal- DP - bottom-up
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