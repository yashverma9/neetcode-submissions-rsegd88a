class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute - iterate twice, find product of other indexes for each index- O(n2)
        # Smart Brute- O(n) - just find entire product without 0s, each index product is total/byind - O(n)
        # Optimal - without division

        n = len(nums)
        prefix = [0 for _ in range(n)] 
        suffix = [0 for _ in range(n)]

        curProd = 1
        

        for i in range(n):
            prefix[i] = curProd
            curProd *= nums[i]

        curProd = 1    
        for i in range(n-1, -1, -1):
            suffix[i] = curProd
            curProd *= nums[i]
        

        res = []

        for i in range(n):
            res.append(suffix[i]*prefix[i])

        return res
        