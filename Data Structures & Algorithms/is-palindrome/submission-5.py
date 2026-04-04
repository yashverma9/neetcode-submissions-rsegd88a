class Solution:
    # Simply use .isalnum() inbuilt function
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
        
        # Remove non alphanum chars first into new string O(n) space
        # newString = ''
        # for c in s:
        #     if(self.isAlphaNum(c)):
        #          newString += c.lower()
        # if len(newString) == 0:
        #     return True
        # i = 0
        # j = len(newString)-1
        # mid = len(newString)//2

        # while (i <= mid):
        #     if newString[i] != newString[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True

        # No new variable space O(1)

        i = 0
        j = len(s)-1

        while (i < j):
            if (not s[i].isalnum()):
                i += 1
                continue
            if (not s[j].isalnum()):
                j -= 1
                continue
            if (s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1
        return True


        
            

        