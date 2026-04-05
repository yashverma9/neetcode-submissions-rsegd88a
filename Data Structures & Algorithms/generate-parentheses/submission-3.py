class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(countOpen, countClose, group):
            if countOpen == n and countClose == n:
                res.append(group[:])
                return
            
            # Close bracket
            if countClose < n and countOpen > countClose:
                group += ")"
                backtrack(countOpen, countClose + 1, group)
                group = group[:-1]

            # Open backet 
            if countOpen < n: 
                group += "("
                backtrack(countOpen + 1, countClose, group)
                group = group[:-1]
                
        backtrack(0, 0, "")

        return res
        