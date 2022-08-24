# https://leetcode.com/problems/unique-paths/
# https://leetcode.com/problems/unique-paths/discuss/2363008/Python-oror-Detailed-Explanation-oror-Easy-Understand-oror-DP-oror-MATH

class Solution:
    # Math Solution
    # def uniquePaths(self, m: int, n: int) -> int:
    #     import math
    #     return math.comb(n + m - 2, n - 1)

    # DP Solution
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row and column to 1
        # Since the combination for 
        # dp[i][0] = dp[i-1][0]
        # dp[0][j] = dp[0][j-1]
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # df_table = [[1]*n] + [[1] + [0]*(n-1) ] * (m-1)
        dp = [[1]*n] * m

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]

    # 
m = 3
n = 7
sol = Solution()
print(sol.uniquePaths(m, n))