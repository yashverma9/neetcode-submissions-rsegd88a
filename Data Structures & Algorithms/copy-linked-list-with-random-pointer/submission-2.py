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

        oldToRandom = {}

        cur = head

        while cur:
            val = cur.val
            random = cur.random
            new = Node(val, None, None)

            oldToNew[cur] = new
            oldToRandom[cur] = random

            cur = cur.next
        

        first = head

        while first:
            oldToNew[first].next = oldToNew[first.next]
            oldToNew[first].random = oldToNew[oldToRandom[first]]

            first = first.next
        
        return oldToNew[head]
