class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            first = num
            bustInd = len(numbers)
            for j in range(i, bustInd):
                if numbers[j] + first == target:
                    return [i+1, j+1]
                if numbers[j] + first > target:
                    bustInd = j
                    break

        