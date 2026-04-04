class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute
        if len(s1) > len(s2):
            return False
        
        size = len(s1)
        
        l = 0
        # Time complexity?
        while (l <= len(s2) - size):
            subStr = s2[l : l + size]
            for c in s1:
                subStr = subStr.replace(c, "", 1)
            if subStr == "":
                return True
            l += 1
        return False