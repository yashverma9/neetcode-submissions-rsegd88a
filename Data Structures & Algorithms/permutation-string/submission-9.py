class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute
        '''
        Time - O(m*n), m - length of big string s2 and n - length of small string to permute for substrings
        Space - O(1) - to store hash map of 26 alphabets only everytime, which is constant
        Even array[26] can be used with index as ord(char) -  ord('a')
        In this approach we consider all substrings of size s1 in s2 one by one, and just count freq
        of each char in subtring, and compare it with originally stored freq of each char in s1
        if they match, then we have a valid inclusion
        '''
        if len(s1) > len(s2):
            return False
        
        size = len(s1)

        s1Map = {}
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1
        
        l = 0
        while (l <= len(s2) - size):
            subStr = s2[l : l + size]
            breakFlag = False
            subMap = {}
            for c in subStr:
                subMap[c] = subMap.get(c, 0) + 1
            for c in s1Map:
                if c not in subMap:
                    breakFlag = True
                    break
                else:
                    subMap[c] -= s1Map[c]
            for c in subMap:
                if subMap[c] != 0:
                    breakFlag = True
                    break
            if not breakFlag:
                return True
            l += 1
        return False