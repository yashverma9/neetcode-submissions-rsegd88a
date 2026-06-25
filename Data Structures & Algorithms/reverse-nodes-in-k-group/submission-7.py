# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
    
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return [prev, head]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head

        while cur:
            n += 1
            cur = cur.next
        
        groups = n // k
        remaining = n % k

        '''
        1-2-3

        3-2-1 

        '''
        reversedLists = [] # [[start, end]...]
        i = 0
        nextStart = head

        resStart = None
        prevEnd = None
        while i < groups:

            start = nextStart
            cur = nextStart
            for _ in range(k-1):
                cur = cur.next
            end = cur
            nextStart = cur.next
            cur.next = None
            [newStart, newEnd] = self.reverseList(start)
            i += 1
            if i == 1:
                resStart = newStart
                prevEnd = newEnd
                continue            
            prevEnd.next = newStart
            prevEnd = newEnd

        if remaining:
            prevEnd.next = nextStart

        return resStart











