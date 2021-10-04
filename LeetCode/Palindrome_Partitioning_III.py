# https://leetcode.com/problems/palindrome-partitioning-iii/
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cal_cost(i, j):
            nonlocal s, cost_matrix

            if i > j:
                return 0

            if cost_matrix[i][j] is None:
                cost_matrix[i][j] = int(s[i] != s[j]) + cal_cost(i + 1, j - 1)
            return cost_matrix[i][j]

        s_length = len(s)
        cost_matrix = [[None] * (s_length) for _ in range(s_length)]
        if k == 1:
            return cal_cost(0, s_length - 1)
        elif s_length == k:
            return 0

        # Initial for the dp
        palindrome_partion_dp = [[cal_cost(0, 0)] + [s_length] * (k - 1)] + [
            [cal_cost(0, i + 1)] + [s_length] * (k - 1) for i in range(s_length - 1)
        ]

        # palindrome_partion_dp[i][j]: optimal ans for s[:i+1] for group j+1
        # palindrome_partion_dp[i][j] = palindrome_partion_dp[l][j - 1] + cal_cost(l + 1, i) for l in range(i)
        #                               as palindrome_partion_dp[l][j - 1] contains optimal ans for s[:l+1] with j groups
        #                               so only the palindrome operation cost of the extra jth group s[:l+1] is needed to add
        for i in range(s_length):
            for j in range(1, min(k, i + 1)):
                for l in range(i):
                    palindrome_partion_dp[i][j] = min(
                        palindrome_partion_dp[i][j],
                        palindrome_partion_dp[l][j - 1] + cal_cost(l + 1, i),
                    )

        return palindrome_partion_dp[-1][-1]
