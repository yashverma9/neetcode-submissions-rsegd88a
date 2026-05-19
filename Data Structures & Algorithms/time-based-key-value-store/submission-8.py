class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # {key:  [[timestamp: value]] }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l = 0
        r = len(values) - 1
        res = ''
        while l <= r:
            mid = l + (r-l)//2
            
            if values[mid][0] == timestamp:
                return values[mid][1]
            
            elif values[mid][0] < timestamp:
                l = mid + 1
                res = values[mid][1]

            else:
                r = mid - 1

        return res
