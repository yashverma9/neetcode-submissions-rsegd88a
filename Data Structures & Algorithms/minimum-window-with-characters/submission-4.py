class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Brute force

        '''
        Find every substring from a starting point till it includes all chars of t
        Find such substrings from all starting points till end of s
        Return minimum of those

        Time - O(52*n*n*n) ~ O(n3) (Another n because string concat is O(n), use ".join() instead using a list => makes is O(n2))
        Space - O(n2) (To store res which contains max n substrings of n size max)
        '''

        if len(s) < len(t):
            return ""

        tCount = [0 for _ in range(52)]

        for c in t:
            if c.islower():
                tCount[ord(c) - ord('a')] += 1
            else:
                tCount[26 + ord(c) - ord('A')] += 1
        res = []

        for l in range(len(s)):
            subStr = ""
            freq = [0 for _ in range(52)]
            for r in range(l, len(s)):
                subStr += s[r]
                if s[r].islower():
                    freq[ord(s[r]) - ord('a')] += 1
                else:
                    freq[26 + ord(s[r]) - ord('A')] += 1
                for i in range(52):
                    if tCount[i] == 0:
                        freq[i] = 0
                valid = True
                for i in range(52):
                    if freq[i] < tCount[i]:
                        valid = False
                if valid:
                    res.append(subStr)
                    break
        
        if len(res) == 0:
            return ""

        minSubStr = s

        for subStr in res:
            if len(subStr) < len(minSubStr):
                minSubStr = subStr
            
        return minSubStr

        

              