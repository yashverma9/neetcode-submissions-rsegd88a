class TimeMap:
    # Optimal - Same set, binary search get
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l = 0
        r = len(self.store[key]) - 1

        if timestamp < self.store[key][l][0]:
            return ""

        lastVal = ""
        while l <= r:
            mid = l + (r-l)//2
            midTup = self.store[key][mid]
            if midTup[0] > timestamp:
                lastVal = self.store[key][mid-1][1] 
            else: 
                lastVal = midTup[1]
            if midTup[0] == timestamp:
                return midTup[1]
            elif midTup[0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
            
        return lastVal

