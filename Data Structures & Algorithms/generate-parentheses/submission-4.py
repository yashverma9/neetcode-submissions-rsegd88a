class Solution:
    # Optimal- backtracking
    # Time - O(n* Cn) = O(4^n/root(n)) -> There are catalan number valid combination and 2n for each combination
    # Space - O(n) for depth, total O(Cn * n ) of result included
    '''
    Just like other backtracking problems, we divide the decision tree into 2 options,
    either to open a parenthesis or close it based on conditions. Eventually add a combination
    into the result when the no. of parenthesis have reached n pairs
    '''
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
        