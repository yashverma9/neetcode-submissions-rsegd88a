class Solution:
    # Optimal - DP - bottom-up, space optimal
    def numDecodings(self, s: str) -> int:
        n = len(s)

        one, two = 1, 0 # two is none as n+1 makes no sense in this problem initially

        for i in range(n-1, -1, -1):
            temp = one
            
            if s[i] == '0':
                one = 0
            
            else:
                one = one
                if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                    one += two
                 
            two = temp

        return one   
        