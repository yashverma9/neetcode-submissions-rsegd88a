class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Brute
        # Time - O(2^(2n) * n) ~ O(4^n * n), 2 decisions 2n times depth and n for checking validity
        # Space - O(2n) ~ O(n) extra space for recursion call stack, otherwise O(4^n * n)

        '''
        Instead of smartly generating combinations, we just randomly dfs into all possible
        combinations and once we reach a length equal to 2x n, we just check if its a valid
        combination and add to result if valid.
        '''
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