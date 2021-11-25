# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * (amount)
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = min(dp[j - i] + 1, dp[j])

        return dp[-1] if dp[-1] != float("inf") else -1


coins = [3, 7, 405, 436]
amount = 8839
# coins = [1, 2, 5]
# amount = 11
sol = Solution()
print(sol.coinChange(coins, amount))
