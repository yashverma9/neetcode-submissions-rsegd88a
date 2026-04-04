# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute
        if not head:
            return
        values = []
        currOld = head
        while currOld:
            values.append(currOld.val)
            currOld = currOld.next
        
        newHead = curr = ListNode()

        mid = len(values)//2

        for i in range(mid):
            new1 = ListNode(values[i])         
            new2 = ListNode(values[len(values) - i - 1])
            new1.next = new2
            curr.next = new1
            curr = curr.next.next

        if len(values)%2 != 0:
            new = ListNode(values[mid])
            curr.next = new
            
        head.val = newHead.next.val
        head.next = newHead.next.next


