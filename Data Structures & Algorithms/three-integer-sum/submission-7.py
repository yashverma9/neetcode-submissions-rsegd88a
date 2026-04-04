class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i!=j and j!=k and i!=k and nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in output:
                            output.append(triplet)
        
        return output