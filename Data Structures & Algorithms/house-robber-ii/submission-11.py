class Solution:
    # Optimal - bottom-up
    # Time - O(n), space - O(n)
    '''
    On similar lines as house robber I, just divide into 2 problem sets where one we can consider
    from 0 -> n-1 house and the other from 1 -> n houses
    '''
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)

        def solve(start, end):
            
            one = 0 # n
            two = 0 # n+1

            for i in range(end-1, start-1, -1):
                one, two = max(nums[i] + two, one), one

            return one
        
        if ln == 1:
            return nums[0]
        return max(solve(1, ln), solve(0, ln-1))