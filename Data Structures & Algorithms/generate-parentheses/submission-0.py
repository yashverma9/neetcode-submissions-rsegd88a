class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 2 li = ["(","(",")",")"]
        res = []
        def checkValid(s: str) -> bool:
            stack = []
            i = 0
            while i < len(s):
                if s[i] == "(":
                    stack.append(s[i])
                else:
                    if not stack:
                        return False
                    if stack.pop() != '(':
                        return False
                i += 1
            if not stack:
                return True
            else:
                return False

        def genPerm(perm: str):
            if len(perm) == n*2:
                if checkValid(perm):
                    res.append(perm)
                return
            else:
                genPerm(perm + '(')
                genPerm(perm + ')')
        
        genPerm("")
        return res