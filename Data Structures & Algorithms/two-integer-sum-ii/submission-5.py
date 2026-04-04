class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sub-optimal would be using binary search as sorted, or hash map storing each number index
        # Optimal - using 2 pointers

        l = 0
        r = len(numbers) - 1

        while(l < r):
            left = numbers[l]
            right = numbers[r]

            if left + right == target:
                return [l+1, r+1]
            elif left + right < target:
                l += 1
            else: # When more than target)
                r -= 1

        return [] # Not possible in this question as mentioned but safe