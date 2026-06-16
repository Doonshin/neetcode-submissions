class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro = 0
        lowest_price = prices[0]

        for num in prices:
            lowest_price = min(lowest_price, num)
            maxpro = max(maxpro, num - lowest_price)
        return maxpro


        