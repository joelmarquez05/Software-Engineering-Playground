class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n-1):
            buy_price = prices[i]
            for j in range(i+1, n):
                sell_price = prices[j]
                max_profit = max(max_profit, sell_price - buy_price)
        return max_profit

# time complexity = O(n^2)
# space complexity = O(1)


        