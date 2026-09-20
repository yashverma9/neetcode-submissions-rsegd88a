class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        buy = -1
        for price in prices:
            if buy == -1:
                buy = price
            
            if price < buy:
                buy = price
            
            else:
                maxProfit = max(price - buy, maxProfit)
        
        return maxProfit
