class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ### Brute force ###
        result = []

        for i in range(len(temperatures)):
            cur = temperatures[i]
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > cur:
                    result.append(j-i)
                    found = True
                    break
            if not found:
                result.append(0)

        return result            