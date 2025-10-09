class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(amount+1):
            for j in coins:
                if j > i:
                    continue
                if dp[i-j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i-j] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-j] + 1)
        return dp[amount]