class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force - find max profit possible for each buy day possible
        
        maxProfit = 0

        for buyDay in range(len(prices)):
            buyPrice = prices[buyDay]
            for sellDay in range(buyDay+1, len(prices)):
                sellPrice = prices[sellDay]
                if sellPrice < buyPrice:
                    continue
                profit = sellPrice - buyPrice
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit
        