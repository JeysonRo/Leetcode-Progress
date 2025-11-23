class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = prices[0]
        highest_profit = 0

        for price in prices:
            profit = price - lowest_price
            lowest_price = min(lowest_price, price)
            highest_profit = max(highest_profit, profit)
        return highest_profit