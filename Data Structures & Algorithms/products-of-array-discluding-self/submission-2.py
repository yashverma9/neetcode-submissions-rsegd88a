class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using division 
        productAll = 1
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                productAll *= nums[i]
            else:
                zeroCount += 1
        if zeroCount > 1:
            return [0]*len(nums)
        
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(productAll)
            else:
                if zeroCount == 1:
                    result.append(0)
                else:
                    result.append(int(productAll/nums[i]))
        return result