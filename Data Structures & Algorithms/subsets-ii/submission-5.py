class Solution:
    # Optimal - backtracking
    # Time- O(n * 2^n), space - O(n) without output, 2^n for output
    '''
    We write this on the lines of the basic subset problem, we sort and  just makes sure 
    not to included duplicate values on one side of the decision tree as we already 
    are going to make the possible subsets with duplicates on one side. So, when we backtrack
    to the side where we don't include nums[i] we just skip all duplicate nums[i] and 
    backtrack directly to a number after duplicates.

    We generate subsets using backtracking (include / exclude pattern).
    To avoid duplicates:
    - We sort the array so duplicates are adjacent
    - When excluding a number, we skip all its duplicates

    This ensures:
    - Each subset is generated only once
    - No duplicate paths are explored
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)

        def backtrack(i, subset):
            if i == n:
                res.append(subset[:])
                return
            
            # When nums[i] is included
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # When nums[i] is not included
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1, subset)
        
        backtrack(0, [])
        return res