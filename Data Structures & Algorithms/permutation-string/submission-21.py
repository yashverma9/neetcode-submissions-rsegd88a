class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # More optimal - O(n) 
        '''

        '''

        if len(s1) > len(s2): return False
    
        counts1 = [0 for _ in range(26)]
        counts2 = [0 for _ in range(26)]
        matches = 0
        n1 = len(s1)
        n2 = len(s2)

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1
        
        if matches == 26:
            return True

        # We start technically from the 2nd window as already checked 1st window
        for r in range(n1, n2):
            indOld = ord(s2[r-n1]) - ord('a')
            indNew = ord(s2[r]) - ord('a')
            
            if counts1[indOld] == counts2[indOld]:
                matches -= 1
            elif counts1[indOld] == counts2[indOld] - 1:
                matches += 1

            counts2[indOld] -= 1
            
            if counts1[indNew] == counts2[indNew] + 1:
                matches += 1
            elif counts1[indNew] == counts2[indNew]:
                matches -= 1
            
            counts2[indNew] += 1
            
            if matches == 26:
                return True

        return False
            