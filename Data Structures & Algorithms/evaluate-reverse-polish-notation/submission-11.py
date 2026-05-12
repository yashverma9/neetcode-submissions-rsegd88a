class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        n = len(tokens)
        while i < n:
            if tokens[i] in '+-*/':
                second = int(stack.pop())
                first = int(stack.pop())
                op = tokens[i]
                
                if op == '+':
                    res = first + second
                
                elif op == '-':
                    res = first - second

                elif op == '*':
                    res = first * second
                
                elif op == '/':
                    res = int(first/second)
                
                stack.append(str(res))

            else:
                stack.append(tokens[i])
            i += 1
            
        return int(stack[-1])