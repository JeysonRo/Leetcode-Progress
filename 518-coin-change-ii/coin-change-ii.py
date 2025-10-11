class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        dp = {} # (index, value)

        def dfs(i, v):
            if v == amount:
                return 1
            if v > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, v) in dp:
                return dp[(i, v)]
            
            dp[(i, v)] = dfs(i, v + coins[i]) + dfs(i+1, v)
            return dp[(i, v)]
            
        return dfs(0, 0)