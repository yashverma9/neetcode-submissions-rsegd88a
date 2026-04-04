class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Optimal using two pointer
        
        nums.sort()
        
        output = []
        for i in range(len(nums)-1):
            target = 0 - nums[i]
            l = i+1
            r = len(nums)-1
            while (l < r):
                if nums[l] + nums[r] == target:
                    triplet = [nums[i], nums[l], nums[r]]
                    if triplet not in output:
                        output.append(triplet)
                    l = l+1
                    r = len(nums)-1
                    
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return output