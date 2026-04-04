class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while (i < len(s)):
            while (s[i] != "#"):
                i += 1
            cnt = int(s[j:i])
            res.append(s[i+1:i+1+cnt]) #   3#cat2#bo
            i = i+1+cnt
            j = i
        return res
