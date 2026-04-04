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
        
        if not head:
            return None
        
        oldToCopy = {None: None}
        
        cur = head

        while cur:
            new = Node(cur.val)
            oldToCopy[cur] = new
            cur = cur.next
        
        cur = head

        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
   
            cur = cur.next
        
        return oldToCopy[head]
        
    
            


