# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Optimal - 1 pass - O(n), O(1)

        first = second = head

        count = 0

        while count != n and second and second.next:
            count += 1
            second = second.next
        
        if count != n:
            return head.next

        while second.next:
            second = second.next
            first = first.next
        
        first.next = first.next.next
        
        return head