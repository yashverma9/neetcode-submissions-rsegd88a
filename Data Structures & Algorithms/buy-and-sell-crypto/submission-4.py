class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(prices[j]-prices[i], maxProfit)
        
        return maxProfit