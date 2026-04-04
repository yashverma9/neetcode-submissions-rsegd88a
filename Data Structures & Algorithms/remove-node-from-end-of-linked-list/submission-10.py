# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Optimal - 1 pass - O(n), O(1)

        dummy = ListNode(0, head)
        left = dummy # We add a dummy node to handle first element deletions directly and return dummy.next later
        right = head

        # This allows right to reach n+1 ahead of left
        while n > 0:
            right = right.next
            n -= 1
        
        # We break when right is null
        while right:
            left = left.next
            right = right.next
        
        # When right reaches null, left is 1 before nth from end, We delete that
        left.next = left.next.next

        # Now remove dummy node and return rest of list
        return dummy.next
            

        # My approach
        # first = second = head

        # count = 0

        # while count != n and second and second.next:
        #     count += 1
        #     second = second.next
        
        # if count != n:
        #     return head.next

        # while second.next:
        #     second = second.next
        #     first = first.next
        
        # first.next = first.next.next
        
        # return head