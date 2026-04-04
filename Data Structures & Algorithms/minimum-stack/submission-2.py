class MinStack:

    ### Brute force ###

    # Find min from the stack everytime, not O(1)
    #
    #

    ### Using 2 stacks O(1) and O(n) space ###

    # def __init__(self):
    #     self.stack= []
    #     self.minStack = [] # This will keep the min uptill the number of elements in the stack

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     val = min(val, self.minStack[-1] if len(self.minStack)>0 else val)
    #     self.minStack.append(val) # This way top always has min of all elements till now in stack
    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minStack[-1]


    ### Using an extra variable instead of stack (less space) ###

    def __init__(self):
        self.stack= []
        self.min = float('inf') # we can assign min value as infinity initially as 
        # nothing will be more than that
        # At every push, we store offset (delta from min) value
        # We keep min value in another value 
        # so (actual pop value) is actually found by adding min value to offset
        # Also, you can say whenever the offset becomes negative while pushing,
        # then that means we have a new min and hence update the min to that
        # So, while popping if the val is negative, we can get the updated min
        # after pop by adding the current min to it. And the number to pop
        # is actually the current min


    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(val-self.min)
        else:
            offset = val-self.min
            self.stack.append(offset)
            if offset < 0:
                self.min = val

    def pop(self) -> None:
        offset = self.stack.pop()
        if (offset < 0):
            self.min = self.min - offset # because in that case top is the min, 
            # and adding to offset will give previous min
            # While pushing this we would have got the new min
            # And that time offset would be,  offset = val - oldMin
            # Here is val is new min so, offset = newMin - oldMin
            # Hence as we pop newMin, we need oldMin = newMin - offset

    def top(self) -> int:
        if (self.stack[-1] < 0):
            return self.min # Because in case of negative, the top is the min
        return self.stack[-1] + self.min # to get original val, we add the min

    def getMin(self) -> int:
        return self.min