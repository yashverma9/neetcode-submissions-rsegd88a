class Solution:
    def evalRPN(self, tokens: List[str]) -> int:    
        ### Using brute force ###
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    op = tokens[i]
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if op == "+":
                        res = a + b
                    elif op == "-":
                        res = a - b
                    elif op == "*":
                        res = a * b
                    else:
                        res = int(a/b)
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    break
                    # This way 3 elements replaced with 1 res everytime
                    # And loop again for next 3 till we only have 1 result left in list
                
        return int(tokens[0])
        