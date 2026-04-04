class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []

        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                operand2 = evalStack.pop()
                operand1 = evalStack.pop()
                if token == '+':
                    res = operand1 + operand2
                elif token == '-':
                    res = operand1 - operand2
                elif token == '*':
                    res = operand1 * operand2
                else:
                    res = int(operand1 / operand2)
                evalStack.append(res)

            else:
                evalStack.append(int(token))
        
        return evalStack[-1]