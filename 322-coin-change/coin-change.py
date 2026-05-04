class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)] # amount : used
        dp[0] = 0
        for i in range(amount+1):
            for denom in coins:
                if i - denom >= 0:
                    dp[i] = min(dp[i], dp[i-denom] + 1)
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]