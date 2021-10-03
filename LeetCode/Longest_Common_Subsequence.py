# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = "!" + text1
        text2 = "." + text2
        text1_length, text2_length = len(text1), len(text2)

        max_length_dp = [[0] * text2_length for _ in range(text1_length)]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    max_length_dp[i][j] = max_length_dp[i - 1][j - 1] + 1
                else:
                    max_length_dp[i][j] = max(
                        max_length_dp[i - 1][j],
                        max_length_dp[i][j - 1],
                    )
        return max_length_dp[-1][-1]
