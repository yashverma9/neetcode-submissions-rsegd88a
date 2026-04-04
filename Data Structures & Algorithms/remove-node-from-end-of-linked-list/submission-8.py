# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute would be to store all in array Time O(n), space O(n)
        # 2 pass pointer -  O(n)
        # We pass the linked list twice, first to find the length of linked list, next to remove len-nth

        length = 0

        curr = head

        while curr:
            curr = curr.next
            length += 1
        
        # To handle situtations when first element to be removed
        if length - n == 0:
            return head.next
        count = 1
        curr = head
        while count != length - n:
            count += 1
            curr = curr.next
        
        curr.next = curr.next.next

        return head