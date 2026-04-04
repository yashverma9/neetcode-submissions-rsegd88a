class TimeMap:
    # Brute force
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        lastVal = ""

        for i, tup in enumerate(self.store[key]):
            if tup[0] == timestamp:
                return tup[1]
            elif tup[0] > timestamp:
                return lastVal
            lastVal = tup[1]
        
        return lastVal
