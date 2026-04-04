class LRUCache:
    # Brute solution - O(n) to update recency using an array of the keys, space O(n)
    def __init__(self, capacity: int):
        self.memory = {} # You can directly use an array storing key, val pairs
        self.arr = [] 
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.memory:
            return -1 
        
        self.arr.remove(key)
        self.arr.append(key)
        return self.memory[key]


    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            self.arr.remove(key)
        
        if len(self.arr) == self.capacity:
            keyToPop = self.arr.pop(0)
            self.memory.pop(keyToPop, None)

        self.arr.append(key)
        self.memory[key] = value