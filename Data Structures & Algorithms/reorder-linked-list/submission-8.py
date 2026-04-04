# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Optimal (Time - O(n), space -O(1))
        if not head:
            return
        
        # Find mid first
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Reverse 2nd half and disconnect it
        prev, curr = None, slow.next # Slow is the end of first half
        slow.next = None # Disconnect it to avoid new last element being pointed by end first half

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = head
        revCurr = prev

        # Merge both halves one at a time
        while revCurr:
            tmpCurr = curr.next
            tmpRev = revCurr.next
            curr.next = revCurr
            revCurr.next = tmpCurr
            curr = tmpCurr
            revCurr = tmpRev
        # Interesting how in case of even, the second is None in last iteration
        # which makes the last node as none automatically when loop breaks
        # For odd, anyways the last element of first half has none in the end because we delinked before
            

        
