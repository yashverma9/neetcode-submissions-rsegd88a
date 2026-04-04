# Optimal O(1), O(n) - double linked list for O(1) deletions/additions to update recency
# We used dummy nodes on left and right extremes of list to avoid edge cases
class Node:
    def __init__ (self, key = 0, value = 0, left = None, right = None):
        self.key = key
        self.value = value
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

    def addNode(self, key, val):
        new = Node(key, val, self.rightDummy.left, self.rightDummy)
        self.rightDummy.left.right = new
        self.rightDummy.left = new
        return new

    def removeNode(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        value = node.value
        self.removeNode(node)
        new = self.addNode(key, value)
        self.cache[key] = new

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
            del self.cache[key]
        
        if len(self.cache) == self.cap:
            lru = self.leftDummy.right
            del self.cache[lru.key]
            self.removeNode(lru)

        new = self.addNode(key, value)
        self.cache[key] = new
