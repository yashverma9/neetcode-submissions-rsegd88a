# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return
        # Find mid
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # The mid is slow, so second half starts from slow.next always (odd or even len)

                
        # Reverse 2nd half - delink it
        second = slow.next
        slow.next = None # Delinking first part from 2nd to avoid cyle

        prev, curr = None, second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Alternate b/w first and 2nd half and join

        first = head
        second = prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

    