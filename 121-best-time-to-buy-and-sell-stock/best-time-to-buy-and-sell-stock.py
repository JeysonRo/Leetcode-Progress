class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        res = 0

        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            profit = prices[i] - lowest
            res = max(res, profit)

        return res