# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ''' 431 + 889 = 1320
        1 3 4
        9 8 8
        -----
        0 2 3 1
        '''

        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        res = dummy

        carry = 0

        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0 

            digitSum = val1 + val2 + carry
            carry = digitSum // 10
            digitSum = digitSum % 10
            new = ListNode(digitSum)

            res.next = new

            res = res.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        return dummy.next


            