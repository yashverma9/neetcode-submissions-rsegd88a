class MinStack:

    ### Brute force ###

    # Find min from the stack everytime, not O(1)

    ### Using 2 stacks O(1) and O(n) space ###

    def __init__(self):
        self.stack= []
        self.minStack = [] # This will keep the min uptill the number of elements in the stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if len(self.minStack)>0 else val)
        self.minStack.append(val) # This way top always has min of all elements till now in stack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
