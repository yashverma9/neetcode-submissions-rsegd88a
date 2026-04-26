class Solution:
    # Brute 
    # O(n^2) - Time, O(1) - space
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                if product > maxProd:
                    maxProd = product
        
        return maxProd