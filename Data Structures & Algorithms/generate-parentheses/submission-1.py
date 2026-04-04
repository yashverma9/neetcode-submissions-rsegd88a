class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 2 li = ["(","(",")",")"]
        
        ### Brute force 2^n ###

        # Generate all posibillities first, then check validity
        
        # res = []
        # def checkValid(s: str) -> bool:
        #     stack = []
        #     i = 0
        #     while i < len(s):
        #         if s[i] == "(":
        #             stack.append(s[i])
        #         else:
        #             if not stack:
        #                 return False
        #             if stack.pop() != '(':
        #                 return False
        #         i += 1
        #     if not stack:
        #         return True
        #     else:
        #         return False

        # def genPerm(perm: str):
        #     if len(perm) == n*2:
        #         if checkValid(perm):
        #             res.append(perm)
        #         return
        #     else:
        #         genPerm(perm + '(')
        #         genPerm(perm + ')')
        
        # genPerm("")
        # return res


        ### Optimal - conditional using pruning ###
        
        result = []
        
        def genPerm(s, openCount, closeCount):
            if len(s) == 2*n:
                result.append(s)
                return # base condition for recurssion exit

            if closeCount < openCount:
                genPerm(s+")", openCount, closeCount+1)
            if openCount < n or (openCount <= closeCount and openCount <n):
                genPerm(s+"(", openCount+1, closeCount)
        

        genPerm("", 0 , 0)
        return result