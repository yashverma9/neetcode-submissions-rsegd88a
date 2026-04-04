class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ### O(n^2) , O(1) ###
        # for i, num in enumerate(numbers):
        #     first = num
        #     bustInd = len(numbers)
        #     for j in range(i, bustInd):
        #         if numbers[j] + first == target:
        #             return [i+1, j+1]
        #         if numbers[j] + first > target:
        #             bustInd = j
        #             break

        ### Using 2 pointers - optimal
        
        # [1,2,3,4].  1+4 > 3. J-- 1+3 > 3 J--  1+2 = 3 return

        first = 0
        second = len(numbers) - 1
        while (first < second):
            if numbers[first] + numbers[second] == target:
                return [first+1, second+1]
            elif numbers[first] + numbers[second] > target:
                second -= 1
            else:
                first += 1        