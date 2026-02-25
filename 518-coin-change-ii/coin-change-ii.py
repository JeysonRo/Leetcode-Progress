class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def backtrack(amount, i):
            if i >= len(coins):
                return 0
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            res = 0
            # use this denomination
            denomination = coins[i]
            res += backtrack(amount-denomination, i)
            # skip this denomination
            res += backtrack(amount, i + 1)
            return res
        
        return backtrack(amount, 0)