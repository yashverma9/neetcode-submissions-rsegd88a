class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Optimal, Time- O(n*2^n), space- O(n) for recursion stack, n*2^n if solution and res also included
        # Explanation at bottom
        
        res, sol = [] , []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:]) # We append a copy, otherwise it will point to reference of sol
                return
            # When we don't add the ith index sol
            backtrack(i+1)

            # When we add the ith index to sol
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res
        
        '''
        We generate all subsets using backtracking.

        At each index, we have 2 choices:
        1. Exclude the current element
        2. Include the current element

        We recursively explore both choices until we reach the end of the array.
        Each complete path represents one subset.

        We use a temporary list `sol` to build subsets and append a copy
        of it to the result when we reach the base case.

        Backtracking (pop) ensures we undo choices before exploring new ones.

        ⏱️ Time Complexity (Simple Explanation)

            👉 Total subsets = 2ⁿ

            Why?

            Each element has 2 choices
            Total combinations = 2 × 2 × ... (n times) = 2ⁿ
            🧮 Actual Time
            We generate 2ⁿ subsets
            Copying each subset takes up to O(n)

            👉 Total Time = O(n × 2ⁿ)

        📦 Space Complexity (Important)
            1. Recursion Stack
            Max depth = n (we go one level per index)

            👉 O(n)

            2. Temporary List (sol)
            Holds at most n elements

            👉 O(n)

            3. Result Storage (Main Part)
            We store 2ⁿ subsets
            Each subset can have up to n elements

            👉 O(n × 2ⁿ)
        '''
