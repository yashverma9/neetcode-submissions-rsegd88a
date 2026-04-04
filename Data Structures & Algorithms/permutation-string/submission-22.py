class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # More optimal - O(n) 
        '''
        In this we dont have to match the frequencies everytime and use extra O(26)
        Instead we maintain a match variable which counts the no. of matches till now
        We update it based on the removal of the char after sliding and addition of a
        char in the new fixed window
        If ever our matches are 26 (meaning all alpha match), we find our true substring perm.
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
        
        # Our break condition when freq of all alphabets match which is 26
        if matches == 26:
            return True

        # We start technically from the 2nd window as already checked 1st window
        for r in range(n1, n2):
            indOld = ord(s2[r-n1]) - ord('a')
            indNew = ord(s2[r]) - ord('a')
            
            # We decrease match if they were matching before as now that freq is going to decrease in 2
            if counts1[indOld] == counts2[indOld]:
                matches -= 1

            # We increase match if after removing that char after sliding match the freq
            elif counts1[indOld] == counts2[indOld] - 1:
                matches += 1

            counts2[indOld] -= 1
            
            # We increase the match if addition of new index char matches freq
            if counts1[indNew] == counts2[indNew] + 1:
                matches += 1
            # We decrease the match if they matched before but addtion of new index char doesnt match freq now
            elif counts1[indNew] == counts2[indNew]:
                matches -= 1
            
            counts2[indNew] += 1
            
            if matches == 26:
                return True

        return False
            