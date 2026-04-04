class MinStack:
    # Optimal - O(n) - one stack, O(1) 
    def __init__(self):
        self.stack = []
        self.minVal = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.minVal = val
        offset = val - self.minVal
        if offset < 0:
            self.minVal = val
        self.stack.append(offset)


    def pop(self) -> None:
        offset = self.stack.pop()
        if offset < 0:
            self.minVal = self.minVal - offset

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minVal
        return self.stack[-1] + self.minVal

    def getMin(self) -> int:
        return self.minVal
