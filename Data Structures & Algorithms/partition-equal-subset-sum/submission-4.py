class Solution:
    # Optimal - DP - Top-down
    # Time - O(n * target) - As for each index possible (n) we have 2 options making it 2n and
    # we can arrive to formSubset(i, curSum) with curSum upto target. Hence, n * target
    # Space - O(n * target) - Similarly we have n * target unique states possible
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total//2
        
        memo = {} # memo[(i, sum)]

        def formSubset(i, curSum):
            if curSum == target:
                return True

            if i >= n or curSum > target:
                return False

            if (i, curSum) in memo:
                return memo[(i,curSum)]
            
            res = formSubset(i+1, curSum + nums[i]) or formSubset(i+1, curSum)
            memo[(i, curSum)] = res
            return res
        
        return formSubset(0,0)

                   