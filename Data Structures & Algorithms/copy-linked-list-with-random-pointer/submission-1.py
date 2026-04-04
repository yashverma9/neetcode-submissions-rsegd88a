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
        # Optimal - O(n), O(n) 
        '''
            We cannot directly deep copy the nodes as what if the random points to a node
            not yet formed in the new list. Hence, we take 2 passes. First we initialize each
            new node with a value of respective nodes, and map each old node to new in a hashmap
            for O(1) retrievals later

            Now in the next pass, we map the next and random each from the hash map as now we know
            all nodes have been defined
        '''

        if not head:
            return None
        
        oldToCopy = {None: None} # Because the null nodes wouldn't be added by iteration
        
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
        
    
            


