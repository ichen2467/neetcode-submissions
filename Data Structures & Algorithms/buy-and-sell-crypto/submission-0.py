class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = 0
        profit = 0
        i = 0
        while i < len(prices):
            if prices[i] < prices[bought]:
                bought = i
            else:
                profit = max(prices[i] - prices[bought], profit)
            i += 1
        return profit
        
