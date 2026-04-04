class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Smart Brute (using division)#
        zeroCount = 0
        totalProduct = 1

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                totalProduct *= num

        if zeroCount > 1:
            return [0 for _ in range(len(nums))]
        
        output = []
        
        if zeroCount == 1:
            for num in nums:
                if num == 0:
                    output.append(totalProduct)
                else:
                    output.append(0)
        else:        
            for num in nums:
                if num == 0:
                    output.append(totalProduct)
                else:
                    output.append(int(totalProduct/num))
        
        return output
            
