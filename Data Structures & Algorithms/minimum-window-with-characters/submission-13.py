class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Optimal 
        # Time - O(n)
        # Space - O(n + m) where m is the unique chars in t, n is unique chars in s
        '''
            Instead of comparing frequency of all char at each between substring and t,
            we maintain a dict of only unique char. Once a freq is matched in the sliding window,
            we update a variable called have which store no. of character matches till now. It means
            a character's required freq is available in the substring. Once have and need which is no.
            of characters required to match is equal, then we have a substring. We note the frequency,
            and the index range of substr if its less than min. Now we start shrinking from left and 
            update the frequency and the have variable accordingly. This way we keep getting new shorter
            substrings.
        '''
        if len(s) < len(t):
            return ''

        tFreq = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            tFreq[c] += 1
        
        have, need = 0, len(tFreq)
        
        minRes, minLen = [-1,-1], float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minRes = [l, r]    
                if s[l] in tFreq and window[s[l]] == tFreq[s[l]]:
                    have -= 1
      
                window[s[l]] -= 1
                if not window[s[l]]:
                    del window[s[l]]
                    
                l += 1

        if minLen == float('inf'):
            return ''
        
        return s[minRes[0]: minRes[1] + 1]

