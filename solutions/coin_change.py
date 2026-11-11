"""Coin Change (LeetCode 322). Scan amounts forward to permit reuse of each denomination."""

class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for c in range(coin, amount + 1):
                dp[c] = min(dp[c], dp[c - coin] + 1)
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1
