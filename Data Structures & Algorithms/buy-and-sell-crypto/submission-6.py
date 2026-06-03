class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        b = 0 # buy day

        maxProfit = 0
        
        s = 0 # sell day 
        
        while s < n: 
            # Window valid
            if prices[s] > prices[b]:
                maxProfit = max(maxProfit, prices[s] -  prices[b])
            else:
                b = s
            s += 1
        
        return maxProfit