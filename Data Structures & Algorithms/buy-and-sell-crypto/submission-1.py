class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxProfit = 0
        while r < len(prices):
            # check future prices until current price (r) drops below buy price (l)
            while r < len(prices) and prices[r] >= prices[l]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
                r += 1

            # once prices[r] < prices[l], new best buy point found
            l = r

        return maxProfit


        