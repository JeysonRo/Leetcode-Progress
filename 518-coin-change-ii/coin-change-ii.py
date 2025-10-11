class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        # dp[amount][denominations]

        for a in range(1, amount + 1):
            for d in range(len(coins)):
                if coins[d] > a:
                    if d == 0:
                        continue
                    dp[a][d] = dp[a][d-1]
                else:
                    if d == 0:
                        dp[a][d] = dp[a - coins[d]][d]
                    else:
                        dp[a][d] = dp[a][d-1] + dp[a - coins[d]][d]
        return dp[amount][len(coins)-1]
