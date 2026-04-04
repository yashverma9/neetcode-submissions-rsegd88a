# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        prev, cur = None, head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        end = head
        start = prev

        return [start, end]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur = head

        n = 0
        while cur:
            n += 1
            cur = cur.next
        
        count = n//k # Will give total no. of groups to reverse


        cur = head
        groups = [cur] # We store heads of each group

        i = 1

        while cur:
            if i%k == 0:
                groups.append(cur.next)
                temp = cur.next
                cur.next = None
                cur = temp
            else:
                cur = cur.next
            i += 1

        res = ListNode() # Add a dummy node to start, we will return res.next in the end
        cur = res

        for i in range(count):
            [start, end] = self.reverseList(groups[i])  
            res.next = start
            res = end

        res.next = groups[i+1]
        
        return cur.next
        
