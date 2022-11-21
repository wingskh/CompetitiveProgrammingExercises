# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_before = math.inf
        max_profit = -math.inf
        if len(prices) < 2:
            return 0

        for price in prices:
            min_price_before = min(price, min_price_before)
            max_profit = max(price - min_price_before, max_profit)
        return max_profit

prices = [7,1,5,3,6,4]
sol = Solution()
result = sol.maxProfit(prices)
print(result)