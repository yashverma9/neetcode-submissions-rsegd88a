class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in '+-*/':
                    first = tokens[i-2]
                    second = tokens[i-1]
                    op = tokens[i]

                    if op == '+':
                        res = int(first) + int(second)
                    
                    elif op == '-':
                        res = int(first) - int(second)
                    
                    elif op == '*':
                        res = int(first) * int(second)
                    
                    elif op == '/':
                        res = int(int(first) / int(second))
                    
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    break
                
        return int(tokens[0])