class Solution:
    def isValid(self, s: str) -> bool:
        
        opens = "({["
        closes = ")}]"

        closeOpen = {
            '}': "{",
            ")": "(",
            "]": "["
        }
        
        stack = []

        for c in s:
            if c in opens:
                stack.append(c)

            elif c in closes:
                if not stack:
                    return False
                if closeOpen[c] != stack.pop():
                    return False
            
        if stack:
            return False
        
        return True
