class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0

        for i in range(len(prices) - 1):
            profit = max(prices[(i + 1)::]) - prices[i]
            max_profit = max(profit, max_profit)
        
        return max_profit