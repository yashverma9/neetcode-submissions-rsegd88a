class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## Optimal solution - without division ##
        prefixProduct = [1 for _ in range(len(nums))]
        suffixProduct = [1 for _ in range(len(nums))]

        currentProduct = 1
        for i in range(len(nums)):
            prefixProduct[i] = currentProduct
            currentProduct *= nums[i]


        currentProduct = 1
        for i in range(len(nums)-1,-1,-1):
            suffixProduct[i] = currentProduct
            currentProduct *= nums[i]

        output = []
        for i in range(len(nums)):
            output.append(prefixProduct[i]*suffixProduct[i])
        
        return output