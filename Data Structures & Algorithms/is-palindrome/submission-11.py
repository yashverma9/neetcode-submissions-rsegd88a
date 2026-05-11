class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            

        i = 0
        j = len(s) - 1

        while i <= j:
            if not isAlphaNum(s[i]):
                i += 1
                continue
            
            if not isAlphaNum(s[j]):
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
             
            i += 1
            j -= 1
        
        return True
            