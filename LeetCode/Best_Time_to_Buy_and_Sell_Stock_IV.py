# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
import math


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        total_days = len(prices)
        if total_days == 0:
            return 0
        total_transaction_index = k + 1
        no_stock = [[-math.inf] * total_transaction_index for _ in range(total_days)]
        have_stock = [[-math.inf] * total_transaction_index for _ in range(total_days)]

        for i in range(total_transaction_index):
            no_stock[0][i] = 0
            have_stock[0][i] = -prices[0]

        for day in range(total_days):
            no_stock[day][0] = 0
            have_stock[day][0] = max(have_stock[day - 1][0], -prices[day])

        for day in range(1, total_days):
            for i in range(1, total_transaction_index):
                no_stock[day][i] = max(
                    no_stock[day - 1][i], have_stock[day - 1][i - 1] + prices[day]
                )
                have_stock[day][i] = max(
                    no_stock[day - 1][i] - prices[day], have_stock[day - 1][i]
                )
        return max([no_stock[day][i] for i in range(total_transaction_index)])

    # # Backtracking
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     def daily_option(day, k, can_sell):
    #         nonlocal prices, total_days
    #         if k == 0 or day == total_days:
    #             return 0

    #         if can_sell:
    #             return max(
    #                 prices[day] + daily_option(day + 1, k - 1, False),
    #                 daily_option(day + 1, k, True),
    #             )
    #         else:
    #             return max(
    #                 -prices[day] + daily_option(day + 1, k, True),
    #                 daily_option(day + 1, k, False),
    #             )

    #     total_days = len(prices)
    #     return daily_option(0, k, False)
