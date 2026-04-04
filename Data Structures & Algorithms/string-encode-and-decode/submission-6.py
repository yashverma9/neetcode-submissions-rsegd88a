class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            lenStr = ""
            curStr = ""
            while s[i] != '#':
                lenStr += s[i]
                i += 1
            i += 1
            output.append(s[i:i+int(lenStr)])
            i = i + int(lenStr)

        return output            
            


