class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)

        b = 0 # buy day

        maxProfit = 0
        
        s = 0
        
        while s < n: # sell day 
            # Window valid
            while s < n and prices[s] > prices[b]:
                maxProfit = max(maxProfit, prices[s] -  prices[b])
                s += 1

            b = s
            s += 1
        
        return maxProfit