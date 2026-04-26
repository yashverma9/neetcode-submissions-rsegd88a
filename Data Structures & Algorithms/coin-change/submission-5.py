class Solution:
    # Optimal - DP- Top-down

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} # memo[rem] = minCount , stores amount remaining

        def count(rem):
            # Reached amount target, means no more coins
            if rem == 0:
                return 0
        
            if rem in memo:
                return memo[rem]
            
            minCoins = float('inf')
            for value in coins:
                if rem - value >= 0:
                    minCoins = min(minCoins, 1 + count(rem - value))
            
            memo[rem] = minCoins
            return memo[rem]

        res = count(amount)

        return -1 if res == float('inf') else res

        
        