class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brurte force : Use hashset to store seen time O(n), O(n) space / sort nlogn time

        # Optimal -  Floyd's cycle detection algorithm O(n), O(1)


        '''
            We assume our array is a linked list with a cycle. Each index is the node, and its value in
            the array is its next pointer (index/node). each value (pointer) takes us to the next index (node) 
            and so on. The node which is reached from more than 1 different node is technically the duplicate
            value. And its going to be the start of the cycle always

            We find start of cycle, thats the duplicate val

            No need to make linked list, just start iterating using the array with slow and fast pointer
        '''
        fast = slow = 0 # Pointers (the index)

        # Technically we want to breat fast == slow, but they are already equal before loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0 

        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2] 

        return slow   

