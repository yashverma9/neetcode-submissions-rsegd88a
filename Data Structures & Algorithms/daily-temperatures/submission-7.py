class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Optimal

        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))

            while stack and stack[-1][1] < temp:
                oldInd, oldTemp = stack.pop()
                res[oldInd] = i - oldInd
            
            stack.append((i, temp))
        
        return res