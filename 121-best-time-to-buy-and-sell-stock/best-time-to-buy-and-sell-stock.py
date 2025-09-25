class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        lowestprice = prices[0]
        profit = 0

        while i < len(prices):
            if prices[i] <= lowestprice:
                lowestprice = prices[i]
            else:
                profit = max(prices[i] - lowestprice, profit)
            i += 1

        return profit