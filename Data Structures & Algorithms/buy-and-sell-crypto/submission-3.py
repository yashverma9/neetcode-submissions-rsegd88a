class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimal
        if len(prices) < 2:
            return 0
        maxProfit = 0
        buy = prices[0]
        sellDay = 1
        while (sellDay < len(prices)):
            sell = prices[sellDay]
            if sell < buy:
                buy = sell
            else:
                profit = sell - buy
                maxProfit = max(maxProfit, profit)
            sellDay += 1

        
        return maxProfit