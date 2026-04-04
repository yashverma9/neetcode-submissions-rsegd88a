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
            Time complexity : O(n)
            The slow and fast always meet within O(n) is because consider they are both in 
            a circle (cycle), the slow is catching up with fast but fast will eventually catchup
            with slow if its a cycle. Hence, every step slow moves 1 ahead, but fast reduced their
            distance from the other side by 2. Hence, total fast moves by 1 ahead.
            Now max distance possible between the slow and fast from the direction of fast to slow
            is n-1. Hence it will take n-1 iterations which is ~ O(n) to meet.
        '''

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False