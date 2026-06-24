class Node:
    def __init__(self, key = None, val = None, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        
        self.leftDummy = Node()
        self.rightDummy = Node()
        
        self.leftDummy.right = self.rightDummy
        self.rightDummy.left = self.leftDummy

    # Linked list helpers
    def addNode(self, node):
        self.rightDummy.left.right = node
        node.left = self.rightDummy.left
        node.right = self.rightDummy
        self.rightDummy.left = node

    # Linked list helpers
    def removeNode(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.removeNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.removeNode(node)
            self.addNode(node)
            
            return
        
        if len(self.cache) == self.cap:
             toRemove = self.leftDummy.right
             keyToRemove = toRemove.key
             del self.cache[keyToRemove]
             self.removeNode(toRemove)
    
        new = Node(key, value)
        self.addNode(new)
        self.cache[key] = new
        
        

        
