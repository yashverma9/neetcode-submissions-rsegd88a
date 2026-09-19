class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute - 2 loops except itself
        # sub-optimal - find product of all, divide by self
        # optimal

        preProd = []
        postProd = [0 for _ in range(len(nums))]

        prod = 1
        for num in nums:
            preProd.append(prod)
            prod *= num
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            postProd[i] = prod
            prod *= nums[i]
        
        res = []

        for i in range(len(nums)):
            res.append(preProd[i] * postProd[i])
        
        return res