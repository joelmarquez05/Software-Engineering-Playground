class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_buy)
            if prices[i] < min_buy:
                min_buy = prices[i]
        return max_profit

        

# [1, 5, 10, 2]
# [10, 5, 2]
# [10, 1] -> min = 1,
# [1, 10] -> min = 1, max =