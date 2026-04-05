class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Brute
        res = []

        def checkValid(comb):
            open = 0

            for p in comb:
                if p == "(":
                    open += 1
                else:
                    open -= 1
                if open < 0:
                    return False
            if open == 0:
                return True
            return False

        def dfs(combination):
            if len(combination) == 2 * n:
                if checkValid(combination):
                    res.append(combination[:])
                return
            
            dfs(combination + "(")
            dfs(combination + ")")

            return
        
        dfs("")
        
        return res