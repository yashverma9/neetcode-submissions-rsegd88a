class Solution:
    # Optimal - DP- Top-down

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} # memo[rem] = minCount , stores amount remaining

        def count(rem):
            # Reached amount target, means no more coins
            if rem == 0:
                return 0
            
            # Extra coins
            if rem < -1:
                return -1

            
            if rem in memo:
                return memo[rem]
            
            minCoins = float('inf')
            for value in coins:
                noCoins = count(rem - value)
                if noCoins != -1:
                    minCoins = min(minCoins, 1 + noCoins)
            
            memo[rem] = minCoins if minCoins != float('inf') else -1
            return memo[rem]

        
        return count(amount)


        
        