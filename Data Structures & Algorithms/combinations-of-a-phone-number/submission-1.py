class Solution:
    # Optimal - backtracking
    # Time - O(n* 4^n) - n for new string, 4^n for backtracking with upto 4 choices per step
    # Space - O(n) for recursion depth

    '''
    At every digit we have upto 4 choices, and we backtrack all choices and add a combination
    to the res once we reach end of digits
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        digiAlpha = [
            '',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]        
        n = len(digits)
        res = []

        def backtrack(i, combination):
            if i == n:
                if combination:
                    res.append(combination)
                return
            
            for c in digiAlpha[int(digits[i])]:
                backtrack(i+1, combination + c)
            
            return

        
        backtrack(0, '')
        return res