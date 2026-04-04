class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Optimal
        '''
            We use fixed size sliding window as its about optimal substring
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