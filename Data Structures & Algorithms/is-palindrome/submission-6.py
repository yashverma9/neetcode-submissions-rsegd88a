class Solution:
    def isAlphaNum(self, c: str) -> bool:
        asciVal = ord(c)
        if (
            ord('a') <= asciVal <= ord('z') or
            ord('A') <= asciVal <= ord('Z') or
            ord('0') <= asciVal <= ord('9')
        ):
            return True
        return False
    

    def isPalindrome(self, s: str) -> bool:
        cleanStr = ''
        for c in s:
            if self.isAlphaNum(c):
                cleanStr += c
        
        l = 0
        r = len(cleanStr) - 1

        while(l < r):
            if cleanStr[l].lower() != cleanStr[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

        
