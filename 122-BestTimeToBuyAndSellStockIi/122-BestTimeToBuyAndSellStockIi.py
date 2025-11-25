# Last updated: 11/25/2025, 5:01:54 PM
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0

        c = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                c += prices[i] - prices[i-1]

        return c
