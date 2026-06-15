class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]

        for num in prices:
            lowest = min(num, lowest)
            profit = num - lowest
            res = max(profit, res)
        return res

        