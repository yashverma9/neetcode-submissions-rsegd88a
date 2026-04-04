# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        res = ListNode()
        headRes = res

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next
            
            res = res.next
        
        while curr1:
            res.next = curr1
            curr1 = curr1.next
            res = res.next
        
        while curr2:
            res.next = curr2
            curr2 = curr2.next
            res = res.next

        return headRes.next
        
