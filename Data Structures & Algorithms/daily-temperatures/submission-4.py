class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal

        tempStack = []
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            if not tempStack:
                tempStack.append((i, curTemp))
                continue

            while tempStack and curTemp > tempStack[-1][1]:
                popTemp = tempStack.pop()
                res[popTemp[0]] = i - popTemp[0]
            
            tempStack.append((i, curTemp))
        
        while tempStack:
            popTemp = tempStack.pop()
            res[popTemp[0]] = 0
        
        return res
