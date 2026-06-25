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
        while i < groups:
            i += 1
            start = nextStart
            cur = nextStart
            for _ in range(k-1):
                cur = cur.next
            end = cur
            nextStart = cur.next
            cur.next = None
            reversedLists.append(self.reverseList(start))

        if remaining:
            reversedLists.append([nextStart, None])

        resStart = None
        curEnd = None
        for i in range(len(reversedLists)):
            if i == 0:
                resStart = reversedLists[0][0]
                curEnd = reversedLists[i][1]
                continue
            
            curEnd.next = reversedLists[i][0]
            curEnd = reversedLists[i][1]
        
        return resStart











