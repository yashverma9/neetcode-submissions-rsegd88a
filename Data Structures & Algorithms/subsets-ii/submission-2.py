class Solution:
    # Brute - backtracking
    # Time- O(n * 2^n),  Space - O(n) without output

    '''
    We do the normal subsets, just store in a set as tuples to avoid duplicates. Later
    convert tuples to list and return
    '''
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        def backtrack(i, subset):
            if i == n:
                res.add(tuple(subset))
                return

            # When nums[i] included
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # When nums[i] not included
            backtrack(i + 1, subset)
        
        backtrack(0, [])

        output = [list(subset) for subset in res]
        return output
            

    
