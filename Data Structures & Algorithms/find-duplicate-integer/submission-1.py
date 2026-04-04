class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brurte force : Use hashset to store seen time O(n), O(n) space / sort nlogn time
        # Optimal -  Floyd's cycle detection algorithm O(n), O(1)
        '''
            We assume our array is a linked list with a cycle. Each index is the node, and its value in
            the array is its next pointer (index/node). each value (pointer) takes us to the next index (node) 
            and so on. The node which is reached from more than 1 different node is technically the duplicate
            value. And its going to be the start of the cycle always

            We find start of cycle, thats the duplicate val (multiple nodes have that value because a start always has multiple incoming from nodes/pointer)

            No need to make linked list, just start iterating using the array with slow and fast pointer

            The slow and fast meet in the cycle due to fast moving faster. The distance between the start
            and slow position is same as the start of linked list and the start of cycle

            Hence, we just iterate another slow pointer with current slow, they both meet only at the start
            of the cycle. Which is the duplicate - see Notion notes for Floyd's algo intuition
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

