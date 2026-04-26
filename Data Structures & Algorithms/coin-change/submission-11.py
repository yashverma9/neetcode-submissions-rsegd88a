class Solution:
    # Optimal - DP - bottom-up
    # Time - O(amount * n) - as for each remaing amount possible we do n coins iteration
    # Space - O(amount) for dp cache

    '''
    Very similar to any bottom up, just in case instead of going from end (which we do in top-down),
    we start from beginning to end. As, initially amount remaining is 0 index which means 0 coins 
    required. And so onwards we keep using older dp states for a remaining amount i and updating
    dp[i] using those.

    Space optimizing O(1) is not possible for this problem unlike others because the current
    state depends on many other previous states and not just one or 2
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)] # Amount remaining for each total i

        dp[0] = 0 # 0 coins required when amount remaining is 0

        for i in range(1, amount+1):
            minCoins = float('inf')
            for value in coins:
                if i - value >= 0:
                    if dp[i-value] != -1:
                        minCoins = min(minCoins, 1 + dp[i-value])
            
            dp[i] = minCoins if minCoins != float('inf') else -1
        
        return dp[amount]