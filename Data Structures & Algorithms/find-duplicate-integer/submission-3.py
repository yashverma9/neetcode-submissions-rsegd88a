class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        0 -> 1 -> 2 -> 3 
                  | <__|
        '''

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
            
        slow2 = 0

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow