class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ### Brute force O(n^3) ###
        # result = []

        # for i in range(0, len(nums)):
        #     first = nums[i]
        #     for j in range(0, len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             second = nums[j]
        #         for k in range(0, len(nums)):
        #             if k == i or k == j:
        #                 continue
        #             else:
        #                 third = nums[k]
        #             if first + second + third == 0:
        #                 triplet = sorted([first,second,third])
        #                 if triplet not in result:
        #                     result.append(triplet)

        # return result

        
        ### Brute force O(n^3) - bit optimal - avoids checking for duplicates###
        # result = set()
        # nums.sort()
        # for i in range(0, len(nums)):
        #     first = nums[i]
        #     for j in range(i+1, len(nums)):
        #         second = nums[j]
        #         for k in range(j+1, len(nums)):
        #             third = nums[k]
        #             if first + second + third == 0:
        #                 # No need to sort before adding because they come in same order because
        #                 # of the sort done on the nums, and adding tuple to set will make 
        #                 # sure the triplet is unique
        #                 result.add((first, second, third))
        # return [list(li) for li in result]

        ### Sorting ###

        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            target = 0 - first
            l , r = i+1 , len(nums) - 1
            while (l < r):
                if nums[l] + nums[r] == target:
                    # Again no need to sort as already sorted (see above explain)
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while (nums[l] == nums[l-1]) and l<r:
                        l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else: 
                    r -= 1
        return result

