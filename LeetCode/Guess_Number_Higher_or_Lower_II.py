# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/1510747/python-dp-beat-9752-in-time-99-in-memory-with-explanation


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        starting_index = 1 if n % 2 == 0 else 2
        tmp_list = [i for i in range(starting_index, n, 2)]
        tmp_list_length = len(tmp_list)
        dp = [[0] * tmp_list_length for _ in range(tmp_list_length)]

        for i in range(tmp_list_length):
            dp[i][i] = tmp_list[i]

        for length in range(2, tmp_list_length + 1):
            for i in range(tmp_list_length - length + 1):
                j = i + length - 1
                dp[i][j] = float("inf")
                for k in range(i, j + 1):
                    dp_left = dp[i][k - 1] if k != 0 else 0
                    dp_right = dp[k + 1][j] if k != j else 0
                    dp[i][j] = min(dp[i][j], tmp_list[k] + max(dp_left, dp_right))

        return dp[0][-1]
