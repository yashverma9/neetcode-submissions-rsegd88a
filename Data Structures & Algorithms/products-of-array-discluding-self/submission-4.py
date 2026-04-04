class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #### Using division ####
        # productAll = 1
        # zeroCount = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         productAll *= nums[i]
        #     else:
        #         zeroCount += 1
        # if zeroCount > 1:
        #     return [0]*len(nums)
        
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         result.append(productAll)
        #     else:
        #         if zeroCount == 1:
        #             result.append(0)
        #         else:
        #             result.append(int(productAll/nums[i]))
        # return result



        #### Without division - using prefix and suffix products ####
        
        # [1, 1, 2, 8] - prefix
        # [48, 24, 6, 1] - suffix
        # [48, 24, 12, 8] - product

        # [1, -1, 0, 0, 0] - prefix
        # [0, 6, 6, 3, 1] - suffix
        # [0, -6, 0, 0, 0] - product
        
    
        prefix = [1 for num in nums]
        suffix = [1 for num in nums]

        prevProduct = 1
        for i in range(len(nums)):
            prefix[i] = prevProduct
            prevProduct *= nums[i]
        
        prevProduct = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = prevProduct
            prevProduct *= nums[i]
        
        product = []
        for i in range(len(nums)):
            product.append(prefix[i]*suffix[i])

        return product


        


