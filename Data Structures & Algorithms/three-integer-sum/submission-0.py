class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ### Brute force O(n^3) ###
        result = []

        for i in range(0, len(nums)):
            first = nums[i]
            for j in range(0, len(nums)):
                if i == j:
                    continue
                else:
                    second = nums[j]
                for k in range(0, len(nums)):
                    if k == i or k == j:
                        continue
                    else:
                        third = nums[k]
                    if first + second + third == 0:
                        triplet = sorted([first,second,third])
                        if triplet not in result:
                            result.append(triplet)

        return result