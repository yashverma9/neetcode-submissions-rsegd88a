# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Optimal O(n), O(1) - My way. Solution avoid finding lenght first, more direct solution- see video if you have time
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
        curGroupHead = cur # We store heads of each group

        res = ListNode() # Add a dummy node to start, we will return res.next in the end
        curRes = res

        i = 1
    
        while cur:
            if i%k == 0:
                temp = cur.next
                cur.next = None
                [start, end] = self.reverseList(curGroupHead)    
                curRes.next = start
                curRes = end
                # Take care of next group
                cur = temp
                curGroupHead = temp
            else:
                cur = cur.next
            i += 1
            
        curRes.next = curGroupHead
        
        return res.next
        
