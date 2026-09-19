class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)-1):
            cur = nums[i]

            if cur > 0: 
                break
            
            if i > 0 and nums[i-1] == nums[i]:  # skip duplicates
                continue

            target = 0 - cur
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([cur, nums[l], nums[r]])
                    l += 1 # As same wont be used again
                    r -= 1 # as l changed, same r is not relevant anymore
                
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                
                elif nums[l] + nums[r] < target:
                    l += 1
                
                else:
                    r -= 1
            
        return res

            