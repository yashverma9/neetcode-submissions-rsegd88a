class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute
        output = []
        for i in range(len(numbers)):
            if (len(output)>0):
                break
            firstInd = i
            reqNum = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if numbers[j] == reqNum:
                    output.append(firstInd+1)
                    output.append(j+1)

        return output