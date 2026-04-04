class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Optimal
        '''
            We use fixed size sliding window as its about optimal substring
            Time - O(26*n) -> technically O(n) as 26 is just any k constant
            We move the window by 1 and update the frequency of current window
            by decreasing last removed char and increasing newly added char
            Then match with counts of s1 and if they are equal you have found
            your subtstring permutation
        '''
        if len(s1) > len(s2):
            return False

        counts1 = [0 for _ in range(26)]
        counts2 = [0 for _ in range(26)]

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1

        r = len(s1) # We start one ahead of current window as first window freq already populated

        while (r < len(s2)):
            if counts1 == counts2:
                return True
            
            counts2[ord(s2[r - len(s1)]) - ord('a')] -= 1
            counts2[ord(s2[r]) - ord('a')] += 1
            r += 1

        if counts1 == counts2:
            return True

        return False    