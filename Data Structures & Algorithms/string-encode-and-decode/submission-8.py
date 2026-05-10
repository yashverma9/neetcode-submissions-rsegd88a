class Solution:

    # We need a generic pattern to encode - derive. We can write length of the next word followed
    # by a '#'. So, this way we know till when do you look for the length of next word.

    def encode(self, strs: List[str]) -> str:
        res = ''

        for string in strs:
            n = len(string)
            res += str(n) + '#' + string
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)

        curLen = 0
        i = 0
        while i < n:
            lenStr = ''
            while s[i] != '#':
                lenStr += s[i]
                i += 1
            curLen = int(lenStr)
            string = s[i+1: i+1+curLen]
            res.append(string)
            i = i+1+curLen
        
        return res