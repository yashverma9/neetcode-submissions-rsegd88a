# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        len1 = 0
        len2 = 0

        cur = l1
        
        while cur:
            cur = cur.next
            len1 += 1
        
        cur = l2

        while cur:
            cur = cur.next
            len2 += 1
        
        if len1 > len2:
            result = first = l1
            second = l2
        else:
            result = first = l2
            second = l1
        
        carry = 0
        
        while first:
            if not second:
                secondVal = 0
            else:
                secondVal = second.val
            digitSum = first.val + secondVal + carry
            if digitSum > 9:
                carry = 1
                first.val = digitSum - 10
            else:
                carry = 0
                first.val = digitSum
            if second:
                second = second.next
            prevFirst = first
            first = first.next
        
        if carry:
            prevFirst.next = ListNode(1)

        return result
        
        

    