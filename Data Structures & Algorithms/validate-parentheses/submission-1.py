class Solution:
    def isValid(self, s: str) -> bool:
        # ([{}])

        if (len(s) == 1):
            return False
        
        bracketPair = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for b in s:
            if b == '(' or b == '{' or b == '[':
                stack.append(b)
            elif b == ')' or b == '}' or b == ']':
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if bracketPair[popped] != b:
                    return False
        if len(stack) != 0:
            return False
        return True