class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        n = len(temperatures)
        result = [0 for _ in range(n)]

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
                continue
            
            while stack and stack[-1][0] < temp:
                oldTemp, oldInd = stack.pop()
                result[oldInd] = i - oldInd
            
            stack.append((temp, i))
        
        return result
            
