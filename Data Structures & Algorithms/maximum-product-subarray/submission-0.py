class Solution:
    # Brute
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product > maxProd:
                    maxProd = product
        
        return maxProd