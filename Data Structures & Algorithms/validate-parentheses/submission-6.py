class Solution:
    def isValid(self, s: str) -> bool:
        # What opened later, has to be closed first

        openClose = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        opens = {'(', '{', '['}
        close = {')', '}', ']'}
        stack = []

        for c in s:
            if c in opens:
                stack.append(c)
            
            if c in close:
                if not stack or openClose[c] != stack.pop():
                    return False

        
        if not stack:
            return True
        
        return False