# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Optimal (Time - O(n), space -O(1))

        # Find mid first

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev, curr = None, slow.next
        slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = head
        revCurr = prev

        while revCurr:
            tmpCurr = curr.next
            tmpRev = revCurr.next
            curr.next = revCurr
            revCurr.next = tmpCurr
            curr = tmpCurr
            revCurr = tmpRev

            

        
