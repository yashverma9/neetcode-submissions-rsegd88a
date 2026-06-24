"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {None: None}

        cur = head

        while cur:
            val = cur.val
            new = Node(val, None, None)

            oldToNew[cur] = new
            cur = cur.next
        

        first = head

        while first:
            oldToNew[first].next = oldToNew[first.next]
            oldToNew[first].random = oldToNew[first.random]

            first = first.next
        
        return oldToNew[head]
