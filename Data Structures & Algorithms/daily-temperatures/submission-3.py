class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            days = 0
            for j in range(i+1, len(temperatures)):
                days += 1
                if temperatures[j] > curTemp:
                    res[i] = days
                    break
            
        return res