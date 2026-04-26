class Solution:
    # Optimal - DP- Top-down
    # Time - O(n * amount) - For each amount, count is called once due to memo but each time n coins are iterated
    # Space - O(amount) - For amount no. of memo key value pairs

    '''
    Slightly tricking. But, thinking on the DP top-down lines, we need to solve for no. of coins
    required from amount remaining onwards. So, for each amount remaining we just do a 
    1 + call(remaining amount (amount - val)) and update the memo with the minimum no. of coins
    considering each value of coin.

    In the end we return memo[amount]
    '''

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

        
        