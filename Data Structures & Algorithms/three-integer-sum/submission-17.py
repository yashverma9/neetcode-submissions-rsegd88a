class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        nums.sort()

        for i in range(n-1):
            # Means all positive numbers ahead, hence cant make 0 without -tive no.s
            if nums[i] > 0:
                break
            
            # Means duplicate first number of the triplet, we skip to avoid duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = 0 - nums[i]
            
            l = i + 1
            r = n - 1 

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 # As we cant use same start again
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                            l += 1
                    
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res



