class Solution:
    # Brute
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = 0

        for num in nums:
            total += num
        
        # Means sum can't be divide into 2 equal halves
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