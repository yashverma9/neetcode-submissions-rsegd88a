class Solution:
    # Optimal - DP (KADANE's algo - similar to max sub subarray)
    # Time - O(n), space - O(1)
    '''
    Similar to Kadane's algo where we kept track of current sum and max till now. If the
    sum went below 0 we would reset.

    Here, we keep track of res till now and curMin and curMax. Why curMin? Because a very
    low negative number can become a very big positive number if multiple by a negative number
    later. 

    So, at every number n we consider all 3 options, extending previous maxProduct subarray with n,
    extending previous minProduct subarray with n or else start a new subarray with n if previous
    were just useles (like negative till now, and positive n comes. Then curMax is just n)

    At end of every number, we update res for max product till now. We use a temp to store
    curMax * n for using the curMax which was there at start of the iteration and not updated with n

    0 is naturally handled, because when product becomes 0 due to a 0, it resets to n the next number
    due to 'n' being there in max and min. 

    This doesn't feel like dp but we are using previous states (max and min products) like bottom-up
    but space optimized with only 2 variables.
    
    '''
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            temp = curMax * n
            
            curMax = max(temp, curMin * n, n)
            curMin = min(temp, curMin * n, n)

            res = max(res, curMax)
        
        return res
        