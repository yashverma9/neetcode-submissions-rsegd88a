class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Brute using iteration
        while len(tokens) != 1:
            for i in range(len(tokens)):
                if tokens[i] in '+-*/':
                    op1 = int(tokens[i-2])
                    op2 = int(tokens[i-1])
                    if tokens[i] == "+":
                        res = op1 + op2
                    elif tokens[i] == '-':
                        res = op1 - op2
                    elif tokens[i] == "*":
                        res = op1 * op2
                    else:
                        res = int(op1/op2)
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    break
            
        return int(tokens[0])
        
        