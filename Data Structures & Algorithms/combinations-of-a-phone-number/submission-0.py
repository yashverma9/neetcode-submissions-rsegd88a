class Solution:
    # Brute
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