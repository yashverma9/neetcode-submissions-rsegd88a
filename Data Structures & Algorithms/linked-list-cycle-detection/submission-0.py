# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Brute - would be to just store each visited node in a hash map and check for visited
        # Optimal- slow and fast pointer (Floyd's Tortoise and Hare algo)

        '''
            Time complexity : O(n) -  
        '''

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False