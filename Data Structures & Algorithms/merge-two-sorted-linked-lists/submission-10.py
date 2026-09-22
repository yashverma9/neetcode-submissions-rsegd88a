# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        new = head = ListNode()

        while head1 and head2:
            if head1.val <= head2.val:
                new.next = head1
                new = head1
                head1 = head1.next
            
            else:
                new.next = head2
                new = head2
                head2 = head2.next
            
        if head1:
            new.next = head1
        
        if head2:
            new.next = head2
        
        return head.next
