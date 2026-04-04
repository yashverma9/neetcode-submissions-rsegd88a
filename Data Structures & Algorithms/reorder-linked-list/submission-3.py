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

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i = 0
        j = len(nodes) - 1

        while (i < j):
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        
        # We know last element is ith because in case of odd len, both j = i and we break
        # and in case of even, the loop exits with i += 1 and it breaks so we have i at the
        # end element now due to the break increment
        nodes[i].next = None 



