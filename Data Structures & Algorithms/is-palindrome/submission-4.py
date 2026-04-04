class Solution:
    def isAlphaNum(self, c):
        if not (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9') ):
            return False
        return True
        
    def isPalindrome(self, s: str) -> bool:
        #abcba i = 0  j = 4 mid = 5//2 = 2
        #abccba i = 0 j = 5 mid = 6//2 = 3

        # Remove non alphanum chars first
        newString = ''
        for c in s:
            if(self.isAlphaNum(c)):
                 newString += c.lower()
        if len(newString) == 0:
            return True
        i = 0
        j = len(newString)-1
        mid = len(newString)//2

        while (i <= mid):
            if newString[i] != newString[j]:
                return False
            i+=1
            j-=1
        return True
        