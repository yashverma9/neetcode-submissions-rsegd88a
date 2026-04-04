# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Optimal -
        '''
         using a normal traversal, keeping prev ele and new in store, also storing the next
         in linked list in a temp to avoid breaking the chain.
         Keep assigning the next of curr to prev and then re updating curr with next (temp) and
         prev with curr

        '''
        # Note how prev is kept null/None so that new last element's next is assgined null in first iteration
        prev = None 
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
