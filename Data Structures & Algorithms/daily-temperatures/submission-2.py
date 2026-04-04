class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ### Brute force O(n^2) ###
        # result = []

        # for i in range(len(temperatures)):
        #     cur = temperatures[i]
        #     found = False
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > cur:
        #             result.append(j-i)
        #             found = True
        #             break
        #     if not found:
        #         result.append(0)

        # return result            

        ### Optimal O(n) O(n)###

        # result [1,4,1,2,1,0,0] 
        # We pop if top is less than new index value
        # We subtract to get difference and now replace that value in result index for popped tuple
        # Now we check again with next top, and keep continueing until the outer is bigger
        # If not bigger anymore or stack is empty then you can push the current index

        # [(0,30)] 1,38 -> [(1,38), (2,30)] 3,36 -> [(1,38)] 3,36 ->
        # [(1,38), (3,36)] 4,35 -> [(1,38), (3,36) (4,35)] 5,40 ->
        # [(1,38), (3,36)] 5,40 -> [(1,38)] 5,40 -> [(5,40)] 6,28 -> 
        # [(5,40),(6,28)] # Now thing left, so pop pop and theirs remain 0
        
 
        result = [0 for i in range(len(temperatures))]
        stack = []

        for i, curTemp in enumerate(temperatures):
            while stack and stack[-1][1] < curTemp:
                ind = stack.pop()[0]
                diff = i - ind
                result[ind] = diff
            stack.append((i, temperatures[i]))
        
        return result