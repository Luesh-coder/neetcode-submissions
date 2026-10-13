class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            profit = prices[i] - minPrice
            res = max(res, profit)
        return res
            