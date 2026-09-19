class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BRUTE

        for i in range(len(nums)):
            cur = nums[i]
            toFind = target - cur
        
            for j in range(i+1, len(nums)):
                if nums[j] == toFind:
                    return [i, j]