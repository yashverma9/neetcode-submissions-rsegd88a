class Solution:
    def evalRPN(self, tokens: List[str]) -> int:  

        # The question guarentess (mentioned on leetcode) a valid RFN and no divide by 0
        # Hence, no need to validate first or edge conditions
    

        ### Using brute force  O(n^2) ###
        # while len(tokens) > 1:
        #     for i in range(len(tokens)):
        #         if tokens[i] in "+-*/":
        #             op = tokens[i]
        #             a = int(tokens[i-2])
        #             b = int(tokens[i-1])
        #             if op == "+":
        #                 res = a + b
        #             elif op == "-":
        #                 res = a - b
        #             elif op == "*":
        #                 res = a * b
        #             else:
        #                 res = int(a/b) # For truncate toward zero div
        #             tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
        #             break
        #             # This way 3 elements replaced with 1 res everytime
        #             # And loop again for next 3 till we only have 1 result left in list
                
        # return int(tokens[0])


        ### Using stack O(n), O(n) ###
        opStack = []
        i = 0
        while i < len(tokens):
            if tokens[i] in "+-/*":
                op = tokens[i]
                b = int(opStack.pop())
                a = int(opStack.pop())
                if op == "+":
                    res = a + b
                elif op == "-":
                    res = a - b
                elif op == "*":
                    res = a * b
                else:
                    res = int(a/b) # For truncate toward zero div
                opStack.append(str(res))
            else:
                opStack.append(tokens[i])
            i += 1

        return int(opStack.pop())   # In the end only 1 result will be left
        