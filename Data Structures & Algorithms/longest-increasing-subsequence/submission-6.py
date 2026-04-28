class Solution:
    # Optimal - DP - top-down
    # Time - O(n^2), space - O(n)
    '''
    We store memo[i] for max count possible from subsequence starting from i. Hence, anytime
    we reach i again we reuse memo[i]. We initialize count with 1 because every index has itself
    as 1 valid subsequence. And we also do 1 + findNext(j) because 1 is for itself + whatever is 
    valid j onwards. 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {} # memo[i] stores max count i onwards

        def findNext(i):
            if i in memo:
                return memo[i]

            count = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    count = max(count, 1 + findNext(j))
            
            memo[i] = count
            return count
        
        res = 0
        for i in range(n):
            res = max(res, findNext(i))
        
        return res