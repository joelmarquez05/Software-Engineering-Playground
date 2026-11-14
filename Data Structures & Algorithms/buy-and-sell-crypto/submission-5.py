class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        max_profit = 0
        
        for right in range(n):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right

        return max_profit




# time complexity = O(n^2)
# space complexity = O(1)

# first one is buy always
# second one is sell always
# higher sell => 5 the new sell
# worst sell => add to interval but not mark as sell
# remove highest from interval back until reaching sell (always)


        