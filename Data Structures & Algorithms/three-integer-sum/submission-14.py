class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Optimal using two pointer
        
        nums.sort()
        
        output = []
        for i in range(len(nums)-1):
            target = 0 - nums[i]
            if nums[i] > 0:
                break # As all numbers after this are positive and all positive cant make 0 together
            if i > 0 and nums[i] == nums[i-1]:
                continue # no need to check for same starting element
            l = i+1
            r = len(nums)-1
            while (l < r):
                if nums[l] + nums[r] == target:
                    triplet = [nums[i], nums[l], nums[r]]
                    output.append(triplet)
                    l += 1
                    r -= 1
                    while(nums[l] == nums[l-1]) and l<r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return output