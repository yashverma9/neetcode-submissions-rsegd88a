class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('-inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped < 0:
            val = self.min
            # curMin - oldMin = popped => old min = curMin - popped
            self.min = self.min - popped

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min
        return self.stack[-1] + self.min

    def getMin(self) -> int:
        return self.min
