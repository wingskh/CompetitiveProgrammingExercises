from typing import final


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount: int) -> int:
        
        dp = [float("inf")] * amount

coins = [3,7,405,436]
amount = 8839
sol = Solution()
print(sol.coinChange(coins, amount))
