class Solution:
    # Optimal - dp - bottom-up - space optimized
    # Time - O(n)
    # Space - O(1)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        nextHouse = 0 # n+1 house
        curHouse = 0 # n house

        for i in range(n-1,-1,-1):
            temp = curHouse
            curHouse = max(nums[i]+nextHouse, curHouse)
            nextHouse = temp
        
        return curHouse