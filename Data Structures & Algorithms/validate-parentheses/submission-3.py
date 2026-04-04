class Solution:
    def isValid(self, s: str) -> bool:
        # Brute (o(n2)):
        # while '()' in s or '{} ' or '[]' in s:
        #     s = s.replace('()','')
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        # return s == ''

        # Optimal
        if len(s) < 2 or len(s)%2 != 0:
            return False
        stack = []
        bracRelation = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        

        for c in s:
            if c in bracRelation.values():
                stack.append(c)
            elif c in bracRelation.keys():
                if len(stack) > 0 and stack[-1] == bracRelation[c]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        return True
