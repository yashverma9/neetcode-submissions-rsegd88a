class Solution:
    # Optimal - DP - bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]

        dp[0] = 0 # 0 coins required when amount remaining is 0

        for i in range(1, amount+1):
            minCoins = float('inf')
            for value in coins:
                if i - value >= 0:
                    if dp[i-value] != -1:
                        minCoins = min(minCoins, 1 + dp[i-value])
            
            dp[i] = minCoins if minCoins != float('inf') else -1
        
        return dp[amount]