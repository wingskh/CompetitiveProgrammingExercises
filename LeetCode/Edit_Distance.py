# https://leetcode.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_length = len(word1)
        word2_length = len(word2)
        min_operation_dp = [list(range(word2_length + 1))] + [
            [i] + [0] * word2_length for i in range(1, word1_length + 1)
        ]

        for i in range(word1_length):
            for j in range(word2_length):
                extra_operation = 0 if word1[i] == word2[j] else 1
                min_operation_dp[i + 1][j + 1] = min(
                    min_operation_dp[i + 1][j] + 1,
                    min_operation_dp[i][j + 1] + 1,
                    min_operation_dp[i][j] + extra_operation,
                )

        return min_operation_dp[-1][-1]
