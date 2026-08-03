# Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2093163665/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_at = prices[0]
        sell_at = None
        for i in range(1, len(prices)):
            if prices[i] <= buy_at:
                buy_at = prices[i]
            if sell_at is None or (profit < prices[i] - buy_at):
                sell_at = prices[i]
                profit = sell_at - buy_at
        return profit