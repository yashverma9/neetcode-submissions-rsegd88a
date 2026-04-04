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
        l = 0
        r = len(s)-1

        while(l < r):
            if (not self.isAlphaNum(s[l])):
                l += 1
                continue

            elif(not self.isAlphaNum(s[r])):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

        
