class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ### Brute force O(n^3) ###
        result = set()
        nums.sort()
        for i in range(0, len(nums)):
            first = nums[i]
            for j in range(i+1, len(nums)):
                second = nums[j]
                for k in range(j+1, len(nums)):
                    third = nums[k]
                    if first + second + third == 0:
                        result.add((first, second, third))
        return [list(li) for li in result]

        ### Sorting ###
        # [-1,0,1,2,-1,-4] ->sort-> [-4,-1,-1,0,1,2]
        # -4 + -1 + -1 = -6

        # result = []
        # sortNums = sorted(nums)
        
        # for i in range(len(sortNums)):
        #     first = sortNums[i]
        #     target = 0 - first
        #     j = 0
        #     k = len(sortNums) - 1
        #     while (j < k):
        #         if (j == i):
        #             j += 1
        #             continue
        #         if (k == i):
        #             k -= 1
        #             continue
        #         if sortNums[j] + sortNums[k] == target:
        #             triplet = sorted([sortNums[i], sortNums[j], sortNums[k]])
        #             if triplet not in result:
        #                 result.append(triplet)
        #             j += 1
        #             k -= 1

        #         elif sortNums[j] + sortNums[k] < target:
        #             j += 1
        #         else: 
        #             k -= 1

        # return result

